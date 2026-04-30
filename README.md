# CS2 Skins API

A lightweight FastAPI backend for Counter-Strike 2 weapon skins.

**Base URL:** `https://cs2-api-espb.onrender.com`

## Data Structure
Each skin object returned by the API looks like this:

```json
{
  "name": "MP7 | Whiteout",
  "weapon": "MP7",
  "rarity": "Mil-Spec",
  "imageid": "10",
  "description": "Versatile but expensive...",
  "category": "SMGs",
  "collection": "The Office Collection",
  "image_url": "https://rubengullborg.github.io/cs2-images/images/10.png"
}
```

## Endpoints

These are the current endpoints available from this API:

### 1. Health Check
Checks if the API is online.
- **URL:** `/`
- **Method:** `GET`
- **Response:** `{"message": "CS2 Skins API is running!"}`

### 2. Get All Skins (with Filters)
Fetch the full list of skins or filter by specific attributes.
- **URL:** `/api/skins`
- **Method:** `GET`
- **Query Parameters:**
  | Parameter | Type | Description | Example |
  | :--- | :--- | :--- | :--- |
  | `weapon` | `string` | Filter by weapon name | `MP7`, `AK-47` |
  | `rarity` | `string` | Filter by rarity grade | `Mil-Spec`, `Covert` |
  | `category` | `string` | Filter by category | `Rifle`, `Heavy` |

- **Example Request:**
  `GET /api/skins?weapon=MP7&rarity=Mil-Spec`

### 3. Get Skin by ID
Retrieve the full details of a specific skin using its `imageid`.
- **URL:** `/api/skins/{imageid}`
- **Method:** `GET`
- **Path Parameter:** `imageid` (The unique ID or Steam hash from the data)
- **Example Request:** 
  `GET /api/skins/10`

---

> **Note on Images:** The `image_url` is automatically generated. If the `imageid` is a number, it points to your GitHub Pages hosting. If it's a full URL, the API provides the direct Steam CDN link.



### Important: We're on Free Tier
Since this is hosted on **Render's Free Tier**, the server "sleeps" after 15 minutes of inactivity. The first request after a break may take **40-60 seconds** to return a response, while the server boots up. Subsequent requests will be faster.


## Local Development

If you want to run this repo locally for any reason, you need to do the following:

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
2. **Run the server:**
   ```bash
   uvicorn main:app --reload
   ```
3. **Access locally:** `http://127.0.0.1:8000`

Make sure you're in the root of the directory, when running the above commands.

## Interactive Documentation
FastAPI automatically generates interactive documentation. You can test every endpoint directly from your browser at:
* **Swagger UI:** `https://cs2-api-espb.onrender.com/docs`
