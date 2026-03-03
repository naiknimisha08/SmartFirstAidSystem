from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pymongo import MongoClient

# ==============================
# MongoDB Atlas Connection
# ==============================
MONGO_URL = "mongodb+srv://naiknimisha2007_db_user:NaiknimishaDB08@smartfirstaidcluster.b8w3m7q.mongodb.net/SmartFirstAidDB?retryWrites=true&w=majority"
client = MongoClient(MONGO_URL, tls=True)
db = client["SmartFirstAidDB"]
collection = db["tips"]

# ==============================
# FastAPI App
# ==============================
app = FastAPI(title="AI Cloud Smart First Aid System", version="2.0")

# ==============================
# CORS
# ==============================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For local dev. Can restrict to frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ==============================
# Existing Endpoints
# ==============================
@app.get("/firstaid/guidance", tags=["firstaid"])
def guidance():
    data = list(collection.find({}, {"_id": 0, "condition": 1, "solution": 1}))
    return JSONResponse(content=data)

@app.get("/firstaid/symptoms", tags=["firstaid"])
def symptoms():
    data = list(collection.find({}, {"_id": 0, "condition": 1, "symptoms": 1}))
    return JSONResponse(content=data)

@app.get("/firstaid/treatment", tags=["firstaid"])
def treatment():
    data = list(collection.find({}, {"_id": 0, "condition": 1, "solution": 1}))
    return JSONResponse(content=data)

# ==============================
# 🔹 New Full Search Endpoint
# ==============================
@app.get("/firstaid", tags=["firstaid"])
def search_tip(query: str = Query(..., description="Search first aid tip by condition, symptoms, or solution")):
    """
    Search tips by condition, symptoms, or solution (case-insensitive, partial match).
    Returns all matching tips from the 'tips' collection.
    """
    # MongoDB OR query for condition, symptoms, or solution fields
    result = list(
        collection.find(
            {
                "$or": [
                    {"condition": {"$regex": query, "$options": "i"}},
                    {"symptoms": {"$regex": query, "$options": "i"}},
                    {"solution": {"$regex": query, "$options": "i"}}
                ]
            },
            {"_id": 0}  # Exclude MongoDB _id
        )
    )
    return JSONResponse(content=result)