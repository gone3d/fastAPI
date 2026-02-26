"""
Simple FastAPI Template
A minimal FastAPI application with example endpoints and Swagger documentation.

This is the main application file that sets up FastAPI and registers all routers.
For a well-organized structure:
- config.py - Application configuration and version
- Models are in the models/ directory
- Routes are in the routers/ directory
- This file handles app configuration and middleware
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config import VERSION, APP_TITLE, APP_DESCRIPTION, CORS_ORIGINS, CORS_CREDENTIALS, CORS_METHODS, CORS_HEADERS
from routers import items, health

# Initialize FastAPI app
app = FastAPI(
    title=APP_TITLE,
    description=APP_DESCRIPTION,
    version=VERSION,
    docs_url="/docs",  # Swagger UI
    redoc_url=None,  # Disable ReDoc (Swagger UI provides full documentation)
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGINS,
    allow_credentials=CORS_CREDENTIALS,
    allow_methods=CORS_METHODS,
    allow_headers=CORS_HEADERS,
)

# Include routers
app.include_router(health.router)  # Root and health endpoints
app.include_router(items.router)  # Items CRUD endpoints

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
