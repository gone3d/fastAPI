"""
Health and root endpoints
"""
from fastapi import APIRouter
from fastapi.responses import FileResponse
from datetime import datetime

from config import VERSION

# Create router
router = APIRouter(tags=["Root"])


@router.get("/")
async def root():
    """
    Root endpoint - returns basic API information
    """
    return {
        "message": "Welcome to FastAPI Template",
        "version": VERSION,
        "docs": "/docs",
        "health": "/health",
        "landing_page": "/index.html"
    }


@router.get("/index.html")
async def index():
    """
    Serve the landing page
    """
    return FileResponse("index.html")


@router.get("/health", tags=["Health"])
async def health_check():
    """
    Health check endpoint
    """
    return {
        "status": "healthy",
        "version": VERSION,
        "timestamp": datetime.now()
    }
