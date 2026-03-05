from pymongo import MongoClient
import json

# 1️⃣ Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")  # Replace with your Mongo URI
db = client["smartfirstaiddb"]                       # Replace with your DB name
collection = db["injuries"]                         # Replace with your collection name

# 2️⃣ Load Hindi JSON
with open("injuries_hi.json", "r", encoding="utf-8") as f:
    hindi_data = json.load(f)

# 3️⃣ Update each document by type
for doc in hindi_data:
    result = collection.update_one(
        {"type": doc["type"]},  # Match English document
        {"$set": {
            "name_hi": doc["name_hi"],
            "description_hi": doc["description_hi"],
            "symptoms_hi": doc["symptoms_hi"],
            "immediate_steps_hi": doc["immediate_steps_hi"]
        }}
    )
    if result.matched_count > 0:
        print(f"✅ Updated: {doc['type']}")
    else:
        print(f"⚠️ Type not found in DB: {doc['type']}")

print("🎉 All Hindi data added successfully!")