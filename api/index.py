# api/index.py
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pymongo import MongoClient
import os

app = FastAPI(title="Smart First Aid Backend")

# MongoDB connection
MONGO_URL = os.getenv("MONGODB_URI")
client = MongoClient(MONGO_URL, tls=True)
db = client["SmartFirstAidDB"]
collection = db["injuries_structured"]

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Smart First Aid Backend is live!"}

@app.get("/firstaid/guidance")
def guidance(lang: str = Query("en")):
    data = list(collection.find({}, {"_id": 0}))
    return JSONResponse(content=data)