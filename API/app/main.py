from fastapi import FastAPI
from app.routers import inference, training

def create_app():
    """
    API app creation function
    """
    app_ = FastAPI(title="AI Services App", version="1.0")

    # Include the routes
    app_.include_router(inference.router, prefix="/api/v1")
    app_.include_router(training.router, prefix="/api/v1")

    return app_

app = create_app()