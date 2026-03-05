import json
from copy import deepcopy

try:
    print("Loading export.json...")
    with open("export.json", "r", encoding="utf-8") as f:
        base_tips = json.load(f)

    print(f"Loaded {len(base_tips)} base tips")

    # Remove _id
    for tip in base_tips:
        tip.pop("_id", None)

    expanded_tips = []
    counter = 1

    while len(expanded_tips) < 1000:
        for tip in base_tips:
            if len(expanded_tips) >= 1000:
                break

            new_tip = deepcopy(tip)
            new_tip["name"] = f"{tip['name']} Variant {counter}"
            expanded_tips.append(new_tip)
            counter += 1

    with open("1000_firstaid_tips.json", "w", encoding="utf-8") as f:
        json.dump(expanded_tips, f, indent=2)

    print("✅ Successfully generated 1000 tips!")

except Exception as e:
    print("❌ ERROR:", e)