# main.py
import os
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pymongo import MongoClient

# ==============================
# MongoDB Atlas Connection
# ==============================
import os
from pymongo import MongoClient

# Get MongoDB URI from environment variables
MONGO_URL = os.getenv("MONGODB_URI")
client = MongoClient(MONGO_URL, tls=True)
db = client["SmartFirstAidDB"]
collection = db["injuries_structured"]

# ==============================
# FastAPI App
# ==============================
app = FastAPI(title="AI Cloud Smart First Aid System", version="2.0")

# ==============================
# CORS (allow frontend requests)
# ==============================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Dev only, restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Root endpoint for testing
@app.get("/")
def root():
    return {"message": "Smart First Aid Backend is live!"}
# ==============================
# Projection helper for lang
# ==============================
def get_projection(lang: str):
    if lang.lower() == "hi":
        return {
            "_id": 0,
            "type": 1,
            "name_hi": 1,
            "description_hi": 1,
            "symptoms_hi": 1,
            "immediate_steps_hi": 1
        }
    else:
        return {
            "_id": 0,
            "type": 1,
            "name": 1,
            "description": 1,
            "symptoms": 1,
            "immediate_steps": 1
        }

# ==============================
# Frontend card endpoints
# ==============================
@app.get("/firstaid/guidance", tags=["firstaid"])
def guidance(lang: str = Query("en", description="Language: en or hi")):
    data = list(collection.find({}, get_projection(lang)))
    return JSONResponse(content=data)

@app.get("/firstaid/symptoms", tags=["firstaid"])
def symptoms(lang: str = Query("en", description="Language: en or hi")):
    data = list(collection.find({}, get_projection(lang)))
    return JSONResponse(content=data)

@app.get("/firstaid/treatment", tags=["firstaid"])
def treatment(lang: str = Query("en", description="Language: en or hi")):
    data = list(collection.find({}, get_projection(lang)))
    return JSONResponse(content=data)

# ==============================
# Search endpoint
# ==============================
@app.get("/search/", tags=["firstaid"])
def search_injury(q: str = Query(..., description="Search term"), lang: str = Query("en")):
    projection = get_projection(lang)
    # 1️⃣ Exact / starts-with match on name
    name_field = "name_hi" if lang.lower() == "hi" else "name"
    name_matches = list(
        collection.find(
            {name_field: {"$regex": f"^{q}", "$options": "i"}},
            projection
        )
    )
    if name_matches:
        return JSONResponse(content=name_matches)

    # 2️⃣ If no name match, search description
    desc_field = "description_hi" if lang.lower() == "hi" else "description"
    desc_matches = list(
        collection.find(
            {desc_field: {"$regex": q, "$options": "i"}},
            projection
        )
    )
    return JSONResponse(content=desc_matches)

# ==============================
# Single injury endpoint
# ==============================
@app.get("/injury/{name}", tags=["firstaid"])
def get_injury(name: str, lang: str = Query("en")):
    projection = get_projection(lang)
    name_field = "name_hi" if lang.lower() == "hi" else "name"
    injury = collection.find_one({name_field: {"$regex": name, "$options": "i"}}, projection)
    if injury:
        return injury
    return {"error": "Injury not found"}

# ==============================
# Debug / test endpoint
# ==============================
@app.get("/debug", tags=["firstaid"])
def debug_db():
    docs = list(collection.find({}, {"_id": 0}))
    return {"count": len(docs), "sample": docs[:3]}