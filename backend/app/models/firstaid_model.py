from pydantic import BaseModel

class SymptomRequest(BaseModel):
    symptom: str

class FirstAidResponse(BaseModel):
    advice: str
    severity: int
