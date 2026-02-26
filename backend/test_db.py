from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Get Mongo URI
MONGO_URI = os.getenv("MONGO_URI")

# Connect to MongoDB
client = MongoClient(MONGO_URI)

# Select database and collection
db = client["SmartFirstAidDB"]
collection = db["tips"]

# Count total documents
count = collection.count_documents({})
print("Total tips in DB:", count)

# Get one random tip
random_tip = list(collection.aggregate([{"$sample": {"size": 1}}]))

# Convert ObjectId to string (important)
if random_tip:
    random_tip[0]["_id"] = str(random_tip[0]["_id"])

print("Random tip:", random_tip)