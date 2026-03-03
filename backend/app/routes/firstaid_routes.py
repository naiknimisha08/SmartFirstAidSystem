from fastapi import APIRouter
from fastapi.responses import JSONResponse

# Router with /firstaid prefix
router = APIRouter(prefix="/firstaid")

# Guidance endpoint
@router.get("/guidance", response_class=JSONResponse, tags=["Guidance"])
def guidance():
    return {
        "injury": "Burn",
        "advice": "Cool the burn under running water for 20 minutes. Do not apply ice.",
        "emergency": "If severe, go to hospital immediately."
    }

# Symptoms endpoint
@router.get("/symptoms", response_class=JSONResponse, tags=["Symptoms"])
def symptoms():
    return {
        "burn": ["redness", "pain", "blister"],
        "cut": ["bleeding", "pain", "swelling"]
    }

# Treatment endpoint
@router.get("/treatment", response_class=JSONResponse, tags=["Treatment"])
def treatment():
    return {
        "burn": "Run under cold water, apply sterile dressing",
        "cut": "Clean wound, apply antiseptic, cover with bandage"
    }