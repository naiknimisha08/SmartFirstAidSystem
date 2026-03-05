import json
import random

# A base pool of realistic first‑aid situations
base_entries = [
    {
        "name": "Burn",
        "description": "Skin damage caused by heat, chemicals, electricity, or radiation.",
        "symptoms": ["Redness", "Blisters", "Pain", "Swelling"],
        "immediate_steps": ["Cool the burn with running water", "Cover with sterile cloth", "Do not apply ice", "Seek medical help if severe"]
    },
    {
        "name": "Cut",
        "description": "Small break in the skin caused by sharp objects.",
        "symptoms": ["Bleeding", "Pain", "Redness"],
        "immediate_steps": ["Clean with water", "Apply antiseptic", "Cover with sterile bandage", "Seek help if deep"]
    },
    {
        "name": "Fracture",
        "description": "A break or crack in a bone.",
        "symptoms": ["Pain", "Swelling", "Bruising", "Loss of normal function"],
        "immediate_steps": ["Immobilize the limb", "Apply ice", "Seek urgent medical attention"]
    },
    {
        "name": "Sprain",
        "description": "Stretching or tearing of ligaments around a joint.",
        "symptoms": ["Pain", "Swelling", "Difficulty moving"],
        "immediate_steps": ["Rest the joint", "Apply ice", "Elevate limb", "Seek medical help if painful"]
    },
    {
        "name": "Choking",
        "description": "Airway obstruction due to a foreign object.",
        "symptoms": ["Difficulty breathing", "Coughing", "Unable to speak"],
        "immediate_steps": ["Encourage cough", "Perform Heimlich maneuver", "Get emergency help if needed"]
    },
    {
        "name": "Nosebleed",
        "description": "Bleeding from the nostrils.",
        "symptoms": ["Bleeding from nose", "Feeling of pressure"],
        "immediate_steps": ["Sit upright", "Pinch nose", "Lean forward", "Seek care if severe"]
    },
    {
        "name": "Allergic Reaction",
        "description": "Immune response to allergens causing swelling or rash.",
        "symptoms": ["Swelling", "Rash", "Difficulty breathing"],
        "immediate_steps": ["Remove allergen", "Administer antihistamine", "Seek urgent help if severe"]
    },
    {
        "name": "Heat Stroke",
        "description": "Body overheats due to prolonged high temperature.",
        "symptoms": ["High temperature", "Dizziness", "Confusion"],
        "immediate_steps": ["Move to cool place", "Hydrate if conscious", "Cool body", "Seek emergency help"]
    },
    {
        "name": "Hypothermia",
        "description": "Dangerously low body temperature.",
        "symptoms": ["Shivering", "Slow breathing", "Weak pulse"],
        "immediate_steps": ["Warm the body gradually", "Remove wet clothes", "Seek medical help"]
    },
    {
        "name": "Poisoning",
        "description": "Harmful ingestion of toxic substances.",
        "symptoms": ["Vomiting", "Dizziness", "Abdominal pain"],
        "immediate_steps": ["Call poison control", "Do not induce vomiting unless advised", "Seek urgent help"]
    }
]

all_entries = []
counter = 1

# Generate 1000 entries by repeating the pool with slight variance
while len(all_entries) < 1000:
    base = random.choice(base_entries)
    new_entry = {
        "name": f"{base['name']} #{counter}",
        "description": base["description"],
        "symptoms": base["symptoms"],
        "immediate_steps": base["immediate_steps"]
    }
    all_entries.append(new_entry)
    counter += 1

# Save the file
with open("firstaid_dataset_1000.json", "w") as f:
    json.dump(all_entries, f, indent=2)

print(f"Success — generated {len(all_entries)} entries!")