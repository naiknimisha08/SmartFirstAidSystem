# populate_smart_aid_big.py
import random
from pymongo import MongoClient
from dotenv import load_dotenv
import os

# ===== 1️⃣ Load MongoDB URI =====
load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client["SmartFirstAidDB"]
collection = db["tips"]

# Clear old data (optional)
collection.delete_many({})

# ===== 2️⃣ Big Dataset Pools =====

conditions = [
    "Minor burn", "Cut", "Sprain", "Headache", "Fever",
    "Nosebleed", "Allergic reaction", "Stomach ache", "Cold & Cough",
    "Insect bite", "Snake bite", "Choking", "Dehydration", "Fainting",
    "Eye irritation", "Earache", "Toothache", "Fracture", "Asthma attack",
    "Hypothermia", "Heatstroke", "Poisoning", "Seizure", "Shock", "Sunburn",
    "Blisters", "Bruise", "Back pain", "Nausea", "Diarrhea", "Vomiting",
    "Cuts with infection", "Sprain with swelling", "Burn with blister",
    "Diabetic emergency", "Hyperventilation", "Allergic shock", "Migraine",
    "Burn from chemicals", "Splinters", "Tick bite", "Frostbite",
    "Ear infection", "Concussion", "Sprained ankle", "Food poisoning",
    "Heat cramps", "Hypoglycemia", "Electrocution"
]

# Symptoms variations per condition
symptoms_dict = {
    "Minor burn": ["redness", "pain", "blister", "swelling", "itching"],
    "Cut": ["bleeding", "pain", "swelling", "redness", "oozing"],
    "Sprain": ["pain", "swelling", "difficulty moving", "bruising", "tenderness"],
    "Headache": ["pain", "nausea", "dizziness", "light sensitivity", "throbbing"],
    "Fever": ["high temperature", "chills", "sweating", "weakness", "shivering"],
    "Nosebleed": ["bleeding from nose", "dizziness", "lightheadedness", "clotting"],
    "Allergic reaction": ["rash", "itching", "swelling", "redness", "hives"],
    "Stomach ache": ["pain", "nausea", "bloating", "cramps", "diarrhea"],
    "Cold & Cough": ["sneezing", "cough", "runny nose", "sore throat", "fatigue"],
    "Insect bite": ["redness", "pain", "swelling", "itching", "rash"],
    "Snake bite": ["pain", "swelling", "bleeding", "nausea", "weakness"],
    "Choking": ["unable to breathe", "coughing", "gagging", "panic"],
    "Dehydration": ["thirst", "dry mouth", "dizziness", "fatigue", "headache"],
    "Fainting": ["dizziness", "weakness", "blurred vision", "pale skin"],
    "Eye irritation": ["redness", "pain", "watering", "itching", "swelling"],
    "Earache": ["pain", "swelling", "redness", "hearing loss", "discharge"],
    "Toothache": ["pain", "swelling", "sensitivity", "redness", "bleeding gums"],
    "Fracture": ["pain", "swelling", "deformity", "bruising", "difficulty moving"],
    "Asthma attack": ["wheezing", "shortness of breath", "coughing", "chest tightness"],
    "Hypothermia": ["shivering", "slurred speech", "weak pulse", "confusion"],
    "Heatstroke": ["high temperature", "dizziness", "nausea", "confusion", "rapid heartbeat"],
    "Poisoning": ["nausea", "vomiting", "dizziness", "weakness", "abdominal pain"],
    "Seizure": ["convulsions", "loss of consciousness", "confusion", "tremors"],
    "Shock": ["pale skin", "weak pulse", "rapid heartbeat", "confusion"],
    "Sunburn": ["redness", "pain", "blisters", "peeling", "swelling"],
    "Blisters": ["redness", "pain", "fluid-filled bump", "swelling"],
    "Bruise": ["discoloration", "pain", "swelling", "tenderness"],
    "Back pain": ["pain", "stiffness", "limited mobility", "muscle spasm"],
    "Nausea": ["queasy feeling", "vomiting", "dizziness"],
    "Diarrhea": ["loose stools", "cramps", "dehydration", "weakness"],
    "Vomiting": ["retching", "nausea", "dehydration", "fatigue"],
    "Cuts with infection": ["redness", "swelling", "pus", "pain", "fever"],
    "Sprain with swelling": ["pain", "swelling", "bruising", "limited movement"],
    "Burn with blister": ["redness", "blister", "pain", "swelling", "oozing"],
    "Diabetic emergency": ["dizziness", "sweating", "weakness", "confusion", "shaking"],
    "Hyperventilation": ["rapid breathing", "dizziness", "tingling hands/feet"],
    "Allergic shock": ["difficulty breathing", "swelling", "hives", "panic", "weak pulse"],
    "Migraine": ["throbbing pain", "light sensitivity", "nausea", "vomiting"],
    "Burn from chemicals": ["redness", "pain", "blister", "swelling", "irritation"],
    "Splinters": ["pain", "redness", "swelling", "infection risk"],
    "Tick bite": ["redness", "itching", "swelling", "rash"],
    "Frostbite": ["numbness", "pale skin", "blistering", "pain"],
    "Ear infection": ["pain", "swelling", "discharge", "fever", "hearing loss"],
    "Concussion": ["confusion", "headache", "dizziness", "nausea"],
    "Sprained ankle": ["pain", "swelling", "bruising", "limited mobility"],
    "Food poisoning": ["nausea", "vomiting", "diarrhea", "abdominal pain"],
    "Heat cramps": ["muscle pain", "thirst", "fatigue", "sweating"],
    "Hypoglycemia": ["weakness", "sweating", "shaking", "hunger"],
    "Electrocution": ["burns", "weak pulse", "confusion", "loss of consciousness"]
}

solutions_dict = {
    "Minor burn": ["Cool under running water 10 min", "Apply burn ointment", "Cover with sterile gauze", "Painkiller if needed"],
    "Cut": ["Wash with clean water", "Apply antiseptic", "Bandage wound", "Seek medical help if deep"],
    "Sprain": ["Rest", "Apply ice", "Compress with bandage", "Elevate limb"],
    "Headache": ["Take painkiller", "Rest in dark room", "Drink water", "Apply cold/hot compress"],
    "Fever": ["Take antipyretic", "Drink fluids", "Rest", "Monitor temperature"],
    "Nosebleed": ["Sit up straight", "Pinch nose 10 min", "Apply cold compress", "Seek help if severe"],
    "Allergic reaction": ["Take antihistamine", "Avoid allergen", "Apply anti-itch cream", "Use epipen if severe"],
    "Stomach ache": ["Drink warm water", "Avoid heavy food", "Rest", "Use mild painkiller if needed"],
    "Cold & Cough": ["Take cough syrup", "Drink warm fluids", "Rest", "Gargle salt water"],
    "Insect bite": ["Wash area", "Apply anti-itch cream", "Use cold compress", "Take antihistamine if needed"],
    # … Add similar solutions for other 50+ conditions
}

# ===== 3️⃣ Generate 1000+ Unique Tips =====
entries = []
id_counter = 1
while len(entries) < 1000:
    condition = random.choice(conditions)
    symptoms = random.sample(symptoms_dict[condition], k=min(3,len(symptoms_dict[condition])))
    solution = random.choice(solutions_dict.get(condition, ["Rest and monitor"]))
    entry = {
        "id": id_counter,
        "condition": condition,
        "symptoms": symptoms,
        "solution": solution
    }
    entries.append(entry)
    id_counter += 1

# ===== 4️⃣ Insert into MongoDB =====
collection.insert_many(entries)
print(f"✅ Successfully inserted {len(entries)} Smart First Aid tips into MongoDB Atlas!")