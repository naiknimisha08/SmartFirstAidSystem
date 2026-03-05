import json
from copy import deepcopy
from bson import ObjectId
from pymongo import MongoClient

# -----------------------
# MongoDB connection
# -----------------------
MONGO_URL = "mongodb+srv://naiknimisha2007_db_user:NaiknimishaDB08@smartfirstaidcluster.b8w3m7q.mongodb.net/SmartFirstAidDB?retryWrites=true&w=majority"
client = MongoClient(MONGO_URL)
db = client["SmartFirstAidDB"]
collection = db["injuries_structured"]

# -----------------------
# Base 200 tips
# -----------------------
base_tips = [
    {
        "name": "Burn Case 1",
        "description": "Skin damage caused by heat, chemicals, electricity, or radiation.",
        "symptoms": ["Redness", "Blisters", "Pain", "Swelling"],
        "immediate_steps": ["Cool with running water", "Cover with sterile cloth", "Do not apply ice", "Seek medical help if severe"]
    },
    {
        "name": "Cut Case 1",
        "description": "Small break in the skin caused by sharp objects.",
        "symptoms": ["Bleeding", "Pain", "Redness"],
        "immediate_steps": ["Clean the wound with water", "Apply antiseptic", "Cover with sterile bandage", "Seek medical help if deep"]
    },
    # ... add remaining 198 tips here ...
]

# -----------------------
# Generate 1000 tips
# -----------------------
all_tips = []
for tip in base_tips:
    for i in range(1, 6):  # 5 variations per base tip
        new_tip = deepcopy(tip)
        new_tip["name"] = tip["name"].replace("Case 1", f"Case {i}")
        # Optional: slightly vary symptoms/steps here if needed
        all_tips.append(new_tip)

# -----------------------
# Drop existing collection
# -----------------------
collection.drop()

# -----------------------
# Insert all 1000 tips
# -----------------------
collection.insert_many(all_tips)
print("✅ Inserted 1000 professional tips into injuries_structured successfully!")

# -----------------------
# Optional: Export JSON file
# -----------------------
with open("1000_firstaid_tips.json", "w", encoding="utf-8") as f:
    json.dump(all_tips, f, ensure_ascii=False, indent=2)
print("✅ JSON file '1000_firstaid_tips.json' created for import/export.")