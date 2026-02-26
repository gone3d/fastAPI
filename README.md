# FastAPI Template

A simple, production-ready FastAPI template with example endpoints, Swagger documentation, and easy setup for local development.

## Features

- FastAPI application with example CRUD endpoints
- Automatic interactive API documentation (Swagger UI)
- CORS middleware configured
- Pydantic models for request/response validation
- Health check endpoint
- Simple HTML landing page

## Project Structure

```
fastAPI/
├── main.py              # Main application entry point
├── config.py            # Configuration and version (single source of truth)
├── requirements.txt     # Python dependencies
├── README.md           # This file
├── index.html          # Landing page with links to docs
├── models/             # Pydantic models for validation
│   ├── __init__.py
│   └── item.py         # Item model
└── routers/            # API route handlers
    ├── __init__.py
    ├── items.py        # Items CRUD endpoints
    └── health.py       # Health and root endpoints
```

### Architecture Overview

This project follows FastAPI best practices:

- **config.py** - Single source of truth for version and app configuration
- **main.py** - Application initialization, middleware setup, and router registration
- **models/** - Pydantic models for request/response validation
- **routers/** - Organized endpoint handlers using APIRouter
  - Each router handles a specific domain (items, health, etc.)
  - Easy to add new routers without cluttering main.py

**Benefits of this structure:**
- Easy to maintain and extend
- Clear separation of concerns
- Single source of truth for configuration (like package.json in Node.js)
- Simple to add new endpoints (just create a new router)
- Scalable for larger applications

**Version Management:**
- Update `config.py` to change the version across the entire application
- Version appears in Swagger docs, health endpoint, and root endpoint automatically

## Prerequisites

### macOS

1. **Install Python 3.8 or higher**
   ```bash
   # Check if Python is installed
   python3 --version

   # If not installed, install via Homebrew
   brew install python3
   ```

2. **Install pip (usually comes with Python)**
   ```bash
   python3 -m pip --version
   ```

### Windows

1. **Install Python 3.8 or higher**
   - Download from [python.org](https://www.python.org/downloads/)
   - During installation, check "Add Python to PATH"
   - Verify installation:
     ```cmd
     python --version
     pip --version
     ```

### Linux (Ubuntu/Debian)

1. **Install Python 3.8 or higher**
   ```bash
   # Update package list
   sudo apt update

   # Install Python 3 and pip
   sudo apt install python3 python3-pip python3-venv

   # Verify installation
   python3 --version
   pip3 --version
   ```

### Linux (Fedora/RHEL/CentOS)

1. **Install Python 3.8 or higher**
   ```bash
   # Install Python 3 and pip
   sudo dnf install python3 python3-pip

   # Verify installation
   python3 --version
   pip3 --version
   ```

## Quick Start

### 1. Create Virtual Environment

#### macOS/Linux
```bash
# Navigate to the fastAPI directory
cd fastAPI

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate
```

#### Windows (Command Prompt)
```cmd
# Navigate to the fastAPI directory
cd fastAPI

# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate
```

#### Windows (PowerShell)
```powershell
# Navigate to the fastAPI directory
cd fastAPI

# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\Activate.ps1
```

### 2. Install Dependencies

Once your virtual environment is activated, install the required packages:

```bash
# macOS/Linux
pip3 install -r requirements.txt

# Windows
pip install -r requirements.txt
```

### 3. Run the Application

#### Option A: Using uvicorn directly (recommended)

```bash
# macOS/Linux
uvicorn main:app --reload --host 0.0.0.0 --port 8000

# Windows
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

#### Option B: Using Python

```bash
# macOS/Linux
python3 main.py

# Windows
python main.py
```

The `--reload` flag enables auto-reload during development (changes to code will automatically restart the server).

### 4. Access the Application

Once the server is running, you can access:

- **Landing Page**: [http://localhost:8000/index.html](http://localhost:8000/index.html)
- **API Root**: [http://localhost:8000/](http://localhost:8000/)
- **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **Health Check**: [http://localhost:8000/health](http://localhost:8000/health)
- **Items API**: [http://localhost:8000/api/items](http://localhost:8000/api/items)

## API Endpoints

### Root Endpoints
- `GET /` - API information
- `GET /health` - Health check

### Items CRUD
- `GET /api/items` - Get all items
- `GET /api/items/{item_id}` - Get specific item
- `POST /api/items` - Create new item
- `PUT /api/items/{item_id}` - Update item
- `DELETE /api/items/{item_id}` - Delete item

## Example Usage

### Create an Item

```bash
curl -X POST "http://localhost:8000/api/items" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Example Item",
    "description": "This is a test item",
    "price": 29.99
  }'
```

### Get All Items

```bash
curl -X GET "http://localhost:8000/api/items"
```

## Development Tips

### Stopping the Server

Press `Ctrl+C` in the terminal where the server is running.

### Deactivating Virtual Environment

```bash
deactivate
```

### Viewing Logs

The uvicorn server outputs logs directly to the terminal. Watch for:
- Request logs (GET, POST, etc.)
- Error messages
- Server restart notifications (when using `--reload`)

## Troubleshooting

### Port Already in Use

If port 8000 is already in use, you can use a different port:

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8001
```

### Permission Errors on Linux/macOS

If you encounter permission errors, try:

```bash
python3 -m pip install --user -r requirements.txt
```

### Windows PowerShell Execution Policy Error

If you get an error when activating the virtual environment in PowerShell:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Module Not Found Errors

Make sure your virtual environment is activated before running the application:
- You should see `(venv)` at the beginning of your terminal prompt
- If not, re-run the activation command for your OS

## Next Steps

### Deploying to Production

This template is designed for local development. For production deployment, consider:

1. **Cloud Platforms**:
   - AWS (Elastic Beanstalk, Lambda, ECS)
   - Google Cloud Platform (Cloud Run, App Engine)
   - Azure (App Service, Container Instances)
   - Railway, Render, Fly.io

2. **Containerization**:
   - Create a `Dockerfile`
   - Use Docker Compose for local testing
   - Deploy to Kubernetes

3. **Production Considerations**:
   - Use environment variables for configuration
   - Replace in-memory storage with a real database
   - Add authentication/authorization
   - Implement rate limiting
   - Set up logging and monitoring
   - Use a production ASGI server configuration

### Adding New Endpoints

This section shows you how to add new endpoints to your API. We'll create a complete example with a "Users" resource.

#### Step-by-Step Example: Adding User Endpoints

**Step 1: Create the Pydantic Model**

Create `models/user.py`:

```python
"""
User-related Pydantic models
"""
from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    """
    User model for CRUD operations
    """
    id: Optional[int] = None
    username: str
    email: str
    full_name: Optional[str] = None
```

**Step 2: Update models/__init__.py**

Add the new model to `models/__init__.py`:

```python
"""
Pydantic models for request/response validation
"""
from .item import Item, Message
from .user import User

__all__ = ["Item", "Message", "User"]
```

**Step 3: Create the Router**

Create `routers/users.py`:

```python
"""
Users router - CRUD operations for users
"""
from fastapi import APIRouter, HTTPException
from typing import List

from models.user import User

# Create router
router = APIRouter(
    prefix="/api/users",
    tags=["Users"],
)

# In-memory storage (for demo purposes)
users_db: List[User] = []
user_counter = 1


@router.get("", response_model=List[User])
async def get_users():
    """
    Get all users
    """
    return users_db


@router.get("/{user_id}", response_model=User)
async def get_user(user_id: int):
    """
    Get a specific user by ID
    """
    for user in users_db:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")


@router.post("", response_model=User)
async def create_user(user: User):
    """
    Create a new user
    """
    global user_counter
    user.id = user_counter
    users_db.append(user)
    user_counter += 1
    return user


@router.delete("/{user_id}")
async def delete_user(user_id: int):
    """
    Delete a user
    """
    for idx, user in enumerate(users_db):
        if user.id == user_id:
            users_db.pop(idx)
            return {"message": "User deleted successfully"}
    raise HTTPException(status_code=404, detail="User not found")
```

**Step 4: Register the Router in main.py**

Update `main.py` to include the new router:

```python
from routers import items, health, users  # Add users import

# ... (rest of the code)

# Include routers
app.include_router(health.router)
app.include_router(items.router)
app.include_router(users.router)  # Add this line
```

**Step 5: Test Your New Endpoints**

1. Restart your server (if not using `--reload`):
   ```bash
   uvicorn main:app --reload
   ```

2. Visit [http://localhost:8000/docs](http://localhost:8000/docs)

3. You'll see a new "Users" section with all your endpoints!

4. Try creating a user:
   ```bash
   curl -X POST "http://localhost:8000/api/users" \
     -H "Content-Type: application/json" \
     -d '{
       "username": "johndoe",
       "email": "john@example.com",
       "full_name": "John Doe"
     }'
   ```

5. Get all users:
   ```bash
   curl -X GET "http://localhost:8000/api/users"
   ```

#### Quick Reference: Adding Any Endpoint

The pattern is always the same:

1. **Model** (optional): Create in `models/` and update `models/__init__.py`
2. **Router**: Create in `routers/` with `APIRouter`
3. **Register**: Import and include router in `main.py`
4. **Test**: Check Swagger UI at `/docs`

**Common Router Patterns:**

```python
# Simple GET endpoint
@router.get("/example")
async def example():
    return {"message": "Hello"}

# GET with path parameter
@router.get("/example/{item_id}")
async def get_example(item_id: int):
    return {"id": item_id}

# GET with query parameters
@router.get("/example")
async def search_example(q: str = "", limit: int = 10):
    return {"query": q, "limit": limit}

# POST with request body
@router.post("/example")
async def create_example(data: MyModel):
    return data

# PUT for updates
@router.put("/example/{item_id}")
async def update_example(item_id: int, data: MyModel):
    return {"id": item_id, "data": data}

# DELETE
@router.delete("/example/{item_id}")
async def delete_example(item_id: int):
    return {"message": "Deleted"}
```

### Extending the Template

- Add database integration (PostgreSQL, MongoDB, etc.)
- Implement authentication (JWT, OAuth2)
- Add background tasks (Celery, FastAPI BackgroundTasks)
- Set up testing (pytest)
- Add environment configuration (.env files)
- Create service layer for business logic
- Add dependency injection for database connections

## Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Uvicorn Documentation](https://www.uvicorn.org/)
- [Pydantic Documentation](https://docs.pydantic.dev/)

## License

This template is provided as-is for educational and development purposes.
