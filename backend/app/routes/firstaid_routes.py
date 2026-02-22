from fastapi import APIRouter
from pydantic import BaseModel
from app.services.firstaid_service import get_first_aid_recommendation

router = APIRouter()


# Request Model
class FirstAidRequest(BaseModel):
    symptom: str
    severity: int  # Scale 1–10
    location: str


@router.post("/emergency")
def handle_emergency(request: FirstAidRequest):
    result = get_first_aid_recommendation(
        symptom=request.symptom,
        severity=request.severity,
        location=request.location
    )
    return result