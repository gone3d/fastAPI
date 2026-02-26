"""
Application configuration
Single source of truth for app settings and version
"""

# Application version - update this when releasing new versions
VERSION = "1.0.0"

# Application metadata
APP_TITLE = "FastAPI Template"
APP_DESCRIPTION = "A simple FastAPI template with example endpoints"

# API Configuration
API_PREFIX = "/api"

# CORS settings
CORS_ORIGINS = ["*"]
CORS_CREDENTIALS = True
CORS_METHODS = ["*"]
CORS_HEADERS = ["*"]
