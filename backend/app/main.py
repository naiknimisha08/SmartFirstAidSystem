from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from app.routes.firstaid_routes import router as firstaid_router

# Initialize FastAPI app
app = FastAPI(
    title="AI Cloud Smart First Aid System",
    version="1.0.0",
    description="API for Smart First Aid Tips and Solutions"
)

# Include first aid routes
app.include_router(firstaid_router)

# Redirect root URL to Swagger UI
@app.get("/", include_in_schema=False)
def root():
    """
    Redirect root '/' to Swagger UI at '/docs'
    """
    return RedirectResponse(url="/docs")