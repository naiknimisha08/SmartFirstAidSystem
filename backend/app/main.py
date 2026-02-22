from fastapi import FastAPI
from app.routes.firstaid_routes import router as firstaid_router

app = FastAPI(
    title="AI Cloud Smart First Aid System",
    version="1.0.0"
)

# Include routes
app.include_router(firstaid_router)

@app.get("/")
def root():
    return {"message": "Smart First Aid System API is running successfully"}
