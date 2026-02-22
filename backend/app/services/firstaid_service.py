from datetime import datetime

# Base weights for different emergency types
SYMPTOM_WEIGHTS = {
    "burn": 20,
    "cut": 15,
    "fracture": 40,
    "snake bite": 60,
    "electric shock": 50,
    "choking": 55
}

# First aid instructions
FIRST_AID_GUIDE = {
    "burn": "Cool the burn under running water for 10 minutes. Do not apply ice. Cover with clean cloth.",
    "cut": "Apply pressure to stop bleeding. Clean with antiseptic. Cover with sterile bandage.",
    "fracture": "Do not move injured area. Immobilize using splint and seek medical attention immediately.",
    "snake bite": "Keep person calm. Do not suck venom. Immobilize limb and rush to hospital immediately.",
    "electric shock": "Disconnect power source immediately. Do not touch victim directly if power is active. Call emergency services.",
    "choking": "Encourage coughing if possible. Perform Heimlich maneuver if airway is blocked."
}


def calculate_risk_score(symptom: str, severity: int):
    base_weight = SYMPTOM_WEIGHTS.get(symptom.lower(), 10)
    risk_score = base_weight * severity

    if risk_score > 100:
        risk_score = 100

    return risk_score


def classify_risk(risk_score: int):
    if risk_score <= 20:
        return "Low"
    elif 21 <= risk_score <= 50:
        return "Medium"
    elif 51 <= risk_score <= 80:
        return "High"
    else:
        return "Critical"


def get_first_aid_recommendation(symptom: str, severity: int, location: str):
    risk_score = calculate_risk_score(symptom, severity)
    risk_level = classify_risk(risk_score)

    recommendation = FIRST_AID_GUIDE.get(
        symptom.lower(),
        "Basic first aid guidance not available. Seek medical help if condition worsens."
    )

    emergency_action = "Monitor condition at home."
    if risk_level == "High":
        emergency_action = "Visit nearest clinic as soon as possible."
    elif risk_level == "Critical":
        emergency_action = "Call emergency services immediately!"

    return {
        "symptom": symptom,
        "severity_input": severity,
        "risk_score": risk_score,
        "risk_level": risk_level,
        "location": location,
        "first_aid_instruction": recommendation,
        "emergency_action": emergency_action,
        "timestamp": datetime.utcnow().isoformat()
    }