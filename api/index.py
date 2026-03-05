from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient
import os

# MongoDB connection
MONGO_URI = os.getenv("MONGO_URI")  # Set this in Vercel Environment Variables
client = MongoClient(MONGO_URI)
db = client.get_database()  # default DB from URI
injuries_collection = db["injuries_structured"]

# FastAPI app
app = FastAPI()

# Allow CORS for your frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change "*" to your frontend URL in production
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Smart Backend is live"}

@app.get("/api/injuries")
def get_all_injuries():
    injuries = list(injuries_collection.find({}, {"_id": 0}))
    return {"count": len(injuries), "data": injuries}

@app.get("/api/injuries/{injury_type}")
def get_injury(injury_type: str):
    injury = injuries_collection.find_one({"type": injury_type}, {"_id": 0})
    if not injury:
        raise HTTPException(status_code=404, detail="Injury not found")
    return injury