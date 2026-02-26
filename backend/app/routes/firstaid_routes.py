from fastapi import APIRouter, HTTPException
from pymongo import MongoClient
from dotenv import load_dotenv
import os

# ---------------- Router ----------------
router = APIRouter(
    prefix="/firstaid",
    tags=["firstaid"]
)

# ---------------- Load ENV ----------------
load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")

# ---------------- MongoDB Connection ----------------
client = MongoClient(MONGO_URI)
db = client["SmartFirstAidDB"]
collection = db["tips"]

# ---------------- 1️⃣ Get All Tips ----------------
@router.get("/tips")
def get_all_tips():
    try:
        tips = list(collection.find({}, {"_id": 0}))  # remove _id
        return {
            "count": len(tips),
            "tips": tips
        }
    except Exception as e:
        print("Error in /tips:", e)
        raise HTTPException(status_code=500, detail="Internal Server Error")


# ---------------- 2️⃣ Get Random Tip ----------------
@router.get("/tips/random")
def get_random_tip():
    try:
        tip_cursor = collection.aggregate([
            {"$sample": {"size": 1}},
            {"$project": {"_id": 0}}  # remove _id to prevent JSON error
        ])

        tip_list = list(tip_cursor)

        if not tip_list:
            raise HTTPException(status_code=404, detail="No tips found")

        return tip_list[0]

    except Exception as e:
        print("Error in /tips/random:", e)
        raise HTTPException(status_code=500, detail="Internal Server Error")


# ---------------- 3️⃣ Search by Condition ----------------
@router.get("/tips/search")
def get_tips_by_condition(condition: str):
    try:
        tips = list(collection.find(
            {"condition": {"$regex": condition, "$options": "i"}},
            {"_id": 0}
        ))

        if not tips:
            return {"message": f"No tips found for '{condition}'"}

        return {
            "count": len(tips),
            "tips": tips
        }

    except Exception as e:
        print("Error in /tips/search:", e)
        raise HTTPException(status_code=500, detail="Internal Server Error")