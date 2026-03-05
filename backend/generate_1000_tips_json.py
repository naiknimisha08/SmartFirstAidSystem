import json
from copy import deepcopy

# Example base tips (replace with your real 200 tips if needed)
base_tips = [
    {
        "name": "Burn Case 1",
        "description": "Skin damage caused by heat, chemicals, electricity, or radiation.",
        "symptoms": ["Redness", "Blisters", "Pain", "Swelling"],
        "immediate_steps": [
            "Cool with running water",
            "Cover with sterile cloth",
            "Do not apply ice",
            "Seek medical help if severe"
        ]
    }
]

all_tips = []

for tip in base_tips:
    for i in range(1, 6):
        new_tip = deepcopy(tip)
        new_tip["name"] = tip["name"].replace("Case 1", f"Case {i}")
        all_tips.append(new_tip)

# Save file safely (NO _id)
with open("1000_firstaid_tips.json", "w", encoding="utf-8") as f:
    json.dump(all_tips, f, indent=2)

print("✅ JSON file created successfully.")