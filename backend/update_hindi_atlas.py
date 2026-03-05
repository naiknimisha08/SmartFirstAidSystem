from pymongo import MongoClient
import json

# MongoDB Atlas connection
MONGO_URI = "mongodb+srv://naiknimisha2007_db_user:NaiknimishaDB08@smartfirstaidcluster.b8w3m7q.mongodb.net/SmartFirstAidDB?retryWrites=true&w=majority"
client = MongoClient(MONGO_URI)

# Connect to your database and collection
db = client["SmartFirstAidDB"]
collection = db["injuries_structured"]  # make sure this matches your collection name in Atlas

# Load Hindi JSON file
with open("hindi_firstaid.json", "r", encoding="utf-8") as f:
    hindi_data = json.load(f)

# Update each English document with Hindi fields
for item in hindi_data:
    type_value = item["type"]
    update_fields = {
        "name_hi": item["name_hi"],
        "description_hi": item["description_hi"],
        "symptoms_hi": item["symptoms_hi"],
        "immediate_steps_hi": item["immediate_steps_hi"]
    }
    result = collection.update_one(
        {"type": type_value},    # find English document by type
        {"$set": update_fields}  # add Hindi fields
    )
    print(f"Updated: {type_value} -> Matched {result.matched_count}, Modified {result.modified_count}")

print("✅ All Hindi fields updated successfully!")