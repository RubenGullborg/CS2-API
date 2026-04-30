from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI(title="CS2-Skins-API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

GITHUB_BASE_URL = "https://rubengullborg.github.io/cs2-images/images/"

skins_data = []

with open("skins.jsonl", "r", encoding="utf-8") as file:
    for line in file:
        if line.strip():
            skin = json.loads(line)
            image_id = str(skin.get("imageid", ""))

            # CASE 1: imageid is a Steam URL
            if image_id.startswith("http"):
                skin["image_url"] = image_id
            
            # CASE 2: imageid is just a number
            elif image_id:
                skin["image_url"] = f"{GITHUB_BASE_URL}{image_id}.png"
            
            # CASE 3: Fallback if imageid is missing
            else:
                skin["image_url"] = None

            skins_data.append(skin)

@app.get("/")
def root():
    return {"message": "CS2 Skins API is running!"}

@app.get("/api/skins")
def get_skins(
    weapon: str = Query(None, description="Filter by weapon (e.g., MP7, AK-47...)"),
    rarity: str = Query(None, description="Filter by rarity (e.g., Mil-Spec, Covert...)"),
    category: str = Query(None, description="Filter by category (e.g., Rifle, SMGs, Heavy...)")
):
    results = skins_data
    
    if weapon:
        results = [skin for skin in results if skin.get("weapon", "").lower() == weapon.lower()]
    if rarity:
        results = [skin for skin in results if skin.get("rarity", "").lower() == rarity.lower()]
    if category:
        results = [skin for skin in results if skin.get("category", "").lower() == category.lower()]
        
    return {"total": len(results), "skins": results}

@app.get("/api/skins/{imageid}")
def get_skin_by_id(imageid: str):
    for skin in skins_data:
        if str(skin.get("imageid")) == str(imageid):
            return skin
    return {"error": "Skin not found"}