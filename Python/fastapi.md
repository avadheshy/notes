# FastAPI Comprehensive Guide - All Questions Answered

## Question 1: Explain the concept of asynchronous programming in Python

Asynchronous programming in Python allows you to write concurrent code that can handle multiple operations without blocking the execution thread. It's particularly useful for I/O-bound operations like network requests, database queries, or file operations.

### Key Concepts:

**1. Event Loop**: The core of async programming that manages and executes asynchronous tasks.

**2. Coroutines**: Functions defined with `async def` that can be paused and resumed.

**3. await**: Keyword used to pause execution until an awaitable object completes.

**4. asyncio**: Python's built-in library for asynchronous programming.

```python
import asyncio
import aiohttp

async def fetch_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()

async def main():
    # Sequential execution
    data1 = await fetch_data("https://api.example1.com")
    data2 = await fetch_data("https://api.example2.com")
    
    # Concurrent execution
    data1, data2 = await asyncio.gather(
        fetch_data("https://api.example1.com"),
        fetch_data("https://api.example2.com")
    )

# Run the async function
asyncio.run(main())
```

## Question 2: How does FastAPI leverage asynchronous programming for performance?

FastAPI is built on top of Starlette and uses ASGI (Asynchronous Server Gateway Interface) to handle asynchronous operations efficiently.

### How FastAPI Uses Async:

**1. Non-blocking I/O Operations**: Database queries, API calls, and file operations don't block other requests.

**2. Concurrent Request Handling**: Multiple requests can be processed simultaneously on a single thread.

**3. Automatic Async/Sync Detection**: FastAPI automatically detects whether your endpoint is async or sync.

```python
from fastapi import FastAPI
import asyncio
import httpx

app = FastAPI()

# Async endpoint
@app.get("/async-endpoint")
async def async_endpoint():
    # Non-blocking database query
    async with httpx.AsyncClient() as client:
        response = await client.get("https://api.external.com/data")
    return {"data": response.json()}

# Sync endpoint (FastAPI runs it in a thread pool)
@app.get("/sync-endpoint")
def sync_endpoint():
    # Blocking operation
    import time
    time.sleep(1)
    return {"message": "Completed"}
```

## Question 3: What are the benefits of using asynchronous programming in FastAPI?

### Performance Benefits:

**1. Higher Throughput**: Handle more concurrent requests with fewer resources.

**2. Better Resource Utilization**: CPU isn't idle during I/O operations.

**3. Scalability**: Better performance under high load.

**4. Reduced Memory Usage**: No need for multiple threads for I/O-bound operations.

```python
from fastapi import FastAPI
import asyncio
import time

app = FastAPI()

@app.get("/performance-comparison")
async def performance_test():
    start_time = time.time()
    
    # Simulate concurrent database queries
    tasks = [simulate_db_query(i) for i in range(10)]
    results = await asyncio.gather(*tasks)
    
    end_time = time.time()
    return {
        "results": results,
        "execution_time": end_time - start_time,
        "message": "10 queries executed concurrently"
    }

async def simulate_db_query(query_id):
    await asyncio.sleep(0.1)  # Simulate database delay
    return f"Query {query_id} completed"
```

## Question 4: How does dependency injection simplify code organization and testing in FastAPI?

Dependency injection in FastAPI allows you to:

**1. Separate Concerns**: Keep business logic separate from request handling.

**2. Reuse Code**: Share common functionality across multiple endpoints.

**3. Easy Testing**: Mock dependencies easily for unit testing.

**4. Configuration Management**: Handle database connections, authentication, etc.

```python
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from typing import Annotated

app = FastAPI()

# Database dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Authentication dependency
def get_current_user(token: str = Header(...)):
    # Validate token and return user
    if not validate_token(token):
        raise HTTPException(status_code=401, detail="Invalid token")
    return get_user_from_token(token)

# Using dependencies
@app.get("/users/{user_id}")
async def get_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    user = db.query(User).filter(User.id == user_id).first()
    return user
```

## Question 5: Provide an example of using dependency injection in FastAPI

```python
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Annotated

app = FastAPI()

# Database session dependency
class DatabaseManager:
    def __init__(self):
        self.session = SessionLocal()
    
    def get_session(self):
        return self.session
    
    def close(self):
        self.session.close()

def get_database():
    db_manager = DatabaseManager()
    try:
        yield db_manager.get_session()
    finally:
        db_manager.close()

# Service layer dependency
class UserService:
    def __init__(self, db: Session = Depends(get_database)):
        self.db = db
    
    def get_user(self, user_id: int):
        return self.db.query(User).filter(User.id == user_id).first()
    
    def create_user(self, user_data: UserCreate):
        db_user = User(**user_data.dict())
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

# Using nested dependencies
@app.get("/users/{user_id}")
async def get_user(
    user_id: int,
    user_service: UserService = Depends()
):
    user = user_service.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.post("/users/")
async def create_user(
    user_data: UserCreate,
    user_service: UserService = Depends()
):
    return user_service.create_user(user_data)
```

## Question 6: What are path operations in FastAPI?

Path operations in FastAPI are functions that handle HTTP requests to specific URL paths. They combine:

**1. Path**: The URL endpoint (e.g., `/users/{user_id}`)
**2. Operation**: HTTP method (GET, POST, PUT, DELETE, etc.)
**3. Function**: The Python function that handles the request

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    description: str = None

# Path operation components:
# - Path: /items/{item_id}
# - Operation: GET
# - Function: read_item
@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

# Multiple path operations for the same path
@app.post("/items/")
async def create_item(item: Item):
    return item

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.dict()}
```

## Question 7: Discuss different types of path operations (GET, POST, PUT, DELETE, etc.)

### HTTP Methods and Their Uses:

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Item(BaseModel):
    id: int = None
    name: str
    price: float
    description: str = None

# In-memory storage for demo
items_db = {}

# GET - Retrieve data
@app.get("/items/", response_model=List[Item])
async def get_items():
    """Retrieve all items"""
    return list(items_db.values())

@app.get("/items/{item_id}", response_model=Item)
async def get_item(item_id: int):
    """Retrieve a specific item"""
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return items_db[item_id]

# POST - Create new resource
@app.post("/items/", response_model=Item, status_code=201)
async def create_item(item: Item):
    """Create a new item"""
    item_id = len(items_db) + 1
    item.id = item_id
    items_db[item_id] = item
    return item

# PUT - Update entire resource
@app.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: int, item: Item):
    """Update an entire item"""
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    item.id = item_id
    items_db[item_id] = item
    return item

# PATCH - Partial update
@app.patch("/items/{item_id}", response_model=Item)
async def patch_item(item_id: int, item_update: dict):
    """Partially update an item"""
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    
    stored_item = items_db[item_id]
    update_data = item_update
    
    for field, value in update_data.items():
        if hasattr(stored_item, field):
            setattr(stored_item, field, value)
    
    return stored_item

# DELETE - Remove resource
@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    """Delete an item"""
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    
    del items_db[item_id]
    return {"message": "Item deleted successfully"}

# HEAD - Get headers only
@app.head("/items/{item_id}")
async def head_item(item_id: int):
    """Check if item exists"""
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return {}

# OPTIONS - Get allowed methods
@app.options("/items/{item_id}")
async def options_item(item_id: int):
    """Get allowed methods for item"""
    return {"allowed_methods": ["GET", "PUT", "PATCH", "DELETE", "HEAD", "OPTIONS"]}
```

## Question 8: Demonstrate how to create a path operation using FastAPI

```python
from fastapi import FastAPI, Query, Path, Body, Header, Cookie, Form, File, UploadFile
from pydantic import BaseModel, Field
from typing import List, Optional
from enum import Enum

app = FastAPI()

# Enum for path parameters
class ItemType(str, Enum):
    electronics = "electronics"
    clothing = "clothing"
    books = "books"

# Pydantic models
class Item(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    price: float = Field(..., gt=0)
    description: Optional[str] = Field(None, max_length=500)
    tags: List[str] = []

class User(BaseModel):
    username: str
    email: str

# Basic path operation
@app.get("/")
async def root():
    return {"message": "Hello World"}

# Path parameters with validation
@app.get("/items/{item_id}")
async def get_item(
    item_id: int = Path(..., title="The ID of the item", ge=1),
    item_type: ItemType = Path(..., title="The type of the item")
):
    return {"item_id": item_id, "item_type": item_type}

# Query parameters with validation
@app.get("/search/")
async def search_items(
    q: Optional[str] = Query(None, min_length=3, max_length=50),
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    tags: List[str] = Query([])
):
    return {
        "q": q,
        "skip": skip,
        "limit": limit,
        "tags": tags
    }

# Request body
@app.post("/items/")
async def create_item(item: Item):
    return {"message": "Item created", "item": item}

# Multiple parameters
@app.put("/items/{item_id}")
async def update_item(
    item_id: int = Path(..., ge=1),
    item: Item = Body(...),
    user: User = Body(...),
    priority: int = Body(..., gt=0, le=5)
):
    return {
        "item_id": item_id,
        "item": item,
        "user": user,
        "priority": priority
    }

# Headers and cookies
@app.get("/headers/")
async def read_headers(
    user_agent: Optional[str] = Header(None),
    x_token: Optional[str] = Header(None),
    session_id: Optional[str] = Cookie(None)
):
    return {
        "user_agent": user_agent,
        "x_token": x_token,
        "session_id": session_id
    }

# Form data
@app.post("/form/")
async def handle_form(
    username: str = Form(...),
    password: str = Form(...),
    remember_me: bool = Form(False)
):
    return {
        "username": username,
        "password": "***",
        "remember_me": remember_me
    }

# File upload
@app.post("/upload/")
async def upload_file(
    file: UploadFile = File(...),
    description: Optional[str] = Form(None)
):
    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "size": len(await file.read()),
        "description": description
    }
```

## Question 9: Explain the importance of data validation in API development

Data validation is crucial in API development for several reasons:

### Why Data Validation is Important:

**1. Security**: Prevents injection attacks and malicious input
**2. Data Integrity**: Ensures data consistency and correctness
**3. Error Prevention**: Catches issues early before they cause problems
**4. API Contract**: Enforces the expected data structure
**5. User Experience**: Provides clear error messages for invalid input

### Common Validation Scenarios:

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, validator, root_validator
from typing import Optional, List
from datetime import datetime
import re

app = FastAPI()

class UserRegistration(BaseModel):
    username: str = Field(..., min_length=3, max_length=20)
    email: str = Field(..., regex=r'^[\w\.-]+@[\w\.-]+\.\w+$')
    password: str = Field(..., min_length=8)
    age: int = Field(..., ge=13, le=120)
    phone: Optional[str] = Field(None, regex=r'^\+?1?\d{9,15}$')
    
    @validator('username')
    def validate_username(cls, v):
        if not re.match(r'^[a-zA-Z0-9_]+$', v):
            raise ValueError('Username can only contain letters, numbers, and underscores')
        return v
    
    @validator('password')
    def validate_password(cls, v):
        if not re.search(r'[A-Z]', v):
            raise ValueError('Password must contain at least one uppercase letter')
        if not re.search(r'[a-z]', v):
            raise ValueError('Password must contain at least one lowercase letter')
        if not re.search(r'\d', v):
            raise ValueError('Password must contain at least one digit')
        return v
    
    @root_validator
    def validate_user_data(cls, values):
        username = values.get('username')
        email = values.get('email')
        
        if username and email and username.lower() in email.lower():
            raise ValueError('Username should not be part of email')
        
        return values

@app.post("/register/")
async def register_user(user: UserRegistration):
    # Additional business logic validation
    if await username_exists(user.username):
        raise HTTPException(status_code=400, detail="Username already exists")
    
    if await email_exists(user.email):
        raise HTTPException(status_code=400, detail="Email already registered")
    
    return {"message": "User registered successfully", "username": user.username}

async def username_exists(username: str) -> bool:
    # Database check logic
    return False

async def email_exists(email: str) -> bool:
    # Database check logic
    return False
```

## Question 10: How does FastAPI use Pydantic for data validation?

FastAPI integrates seamlessly with Pydantic for automatic data validation, serialization, and documentation generation.

### How FastAPI Uses Pydantic:

**1. Automatic Validation**: Request data is automatically validated against Pydantic models
**2. Type Conversion**: Automatic type conversion and coercion
**3. Error Handling**: Detailed validation error messages
**4. Documentation**: Automatic OpenAPI schema generation

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, validator, constr, conint
from typing import Optional, List, Union
from datetime import datetime
from enum import Enum

app = FastAPI()

class Priority(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"

class Task(BaseModel):
    id: Optional[int] = None
    title: constr(min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    priority: Priority = Priority.medium
    completed: bool = False
    due_date: Optional[datetime] = None
    tags: List[str] = Field(default_factory=list)
    
    @validator('due_date')
    def validate_due_date(cls, v):
        if v and v < datetime.now():
            raise ValueError('Due date cannot be in the past')
        return v
    
    @validator('tags')
    def validate_tags(cls, v):
        if len(v) > 10:
            raise ValueError('Maximum 10 tags allowed')
        return [tag.lower().strip() for tag in v]

class TaskUpdate(BaseModel):
    title: Optional[constr(min_length=1, max_length=100)] = None
    description: Optional[str] = Field(None, max_length=500)
    priority: Optional[Priority] = None
    completed: Optional[bool] = None
    due_date: Optional[datetime] = None
    tags: Optional[List[str]] = None

# Response models
class TaskResponse(Task):
    id: int
    created_at: datetime
    updated_at: datetime

# Create task with validation
@app.post("/tasks/", response_model=TaskResponse)
async def create_task(task: Task):
    # Pydantic automatically validates the input
    task_dict = task.dict()
    task_dict['id'] = 1  # Simulate database ID generation
    task_dict['created_at'] = datetime.now()
    task_dict['updated_at'] = datetime.now()
    
    return TaskResponse(**task_dict)

# Update task with partial validation
@app.patch("/tasks/{task_id}", response_model=TaskResponse)
async def update_task(task_id: int, task_update: TaskUpdate):
    # Only validate provided fields
    update_data = task_update.dict(exclude_unset=True)
    
    # Simulate fetching existing task
    existing_task = {
        "id": task_id,
        "title": "Existing Task",
        "description": "Existing description",
        "priority": "medium",
        "completed": False,
        "due_date": None,
        "tags": [],
        "created_at": datetime.now(),
        "updated_at": datetime.now()
    }
    
    # Update with new data
    existing_task.update(update_data)
    existing_task['updated_at'] = datetime.now()
    
    return TaskResponse(**existing_task)
```

## Question 11: Provide examples of validating request and response data in FastAPI

```python
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field, validator, EmailStr
from typing import Optional, List, Dict, Any
from datetime import datetime, date
import re

app = FastAPI()

# Request validation models
class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=20, regex=r'^[a-zA-Z0-9_]+$')
    email: EmailStr
    password: str = Field(..., min_length=8)
    full_name: str = Field(..., min_length=2, max_length=100)
    birth_date: Optional[date] = None
    
    @validator('password')
    def validate_password_strength(cls, v):
        if not re.search(r'[A-Z]', v):
            raise ValueError('Password must contain uppercase letter')
        if not re.search(r'[a-z]', v):
            raise ValueError('Password must contain lowercase letter')
        if not re.search(r'\d', v):
            raise ValueError('Password must contain digit')
        return v
    
    @validator('birth_date')
    def validate_age(cls, v):
        if v and (date.today() - v).days < 13 * 365:
            raise ValueError('Must be at least 13 years old')
        return v

class ProductCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=200)
    price: float = Field(..., gt=0, le=10000)
    category: str = Field(..., min_length=1, max_length=50)
    tags: List[str] = Field(default_factory=list, max_items=10)
    specifications: Dict[str, Any] = Field(default_factory=dict)
    
    @validator('tags')
    def validate_tags(cls, v):
        return [tag.strip().lower() for tag in v if tag.strip()]

# Response validation models
class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    full_name: str
    birth_date: Optional[date]
    created_at: datetime
    is_active: bool = True
    
    class Config:
        from_attributes = True  # For SQLAlchemy compatibility

class ProductResponse(BaseModel):
    id: int
    name: str
    price: float
    category: str
    tags: List[str]
    specifications: Dict[str, Any]
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

# Endpoints with request/response validation
@app.post("/users/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate):
    """Create a new user with validation"""
    # Simulate user creation
    user_data = user.dict()
    user_data.update({
        'id': 1,
        'created_at': datetime.now(),
        'is_active': True
    })
    
    # Response automatically validated against UserResponse model
    return UserResponse(**user_data)

@app.post("/products/", response_model=ProductResponse)
async def create_product(product: ProductCreate):
    """Create a new product with validation"""
    product_data = product.dict()
    product_data.update({
        'id': 1,
        'created_at': datetime.now(),
        'updated_at': datetime.now()
    })
    
    return ProductResponse(**product_data)

# List response with validation
@app.get("/users/", response_model=List[UserResponse])
async def get_users(skip: int = 0, limit: int = 10):
    """Get users list with response validation"""
    # Simulate database query
    users_data = [
        {
            'id': 1,
            'username': 'johndoe',
            'email': 'john@example.com',
            'full_name': 'John Doe',
            'birth_date': date(1990, 1, 1),
            'created_at': datetime.now(),
            'is_active': True
        }
    ]
    
    return [UserResponse(**user) for user in users_data]

# Custom response model with computed fields
class UserStats(BaseModel):
    user: UserResponse
    posts_count: int
    followers_count: int
    following_count: int
    account_age_days: int

@app.get("/users/{user_id}/stats", response_model=UserStats)
async def get_user_stats(user_id: int):
    """Get user statistics with complex response validation"""
    # Simulate user data
    user_data = {
        'id': user_id,
        'username': 'johndoe',
        'email': 'john@example.com',
        'full_name': 'John Doe',
        'birth_date': date(1990, 1, 1),
        'created_at': datetime(2020, 1, 1),
        'is_active': True
    }
    
    # Calculate account age
    account_age = (datetime.now() - user_data['created_at']).days
    
    stats_data = {
        'user': UserResponse(**user_data),
        'posts_count': 25,
        'followers_count': 150,
        'following_count': 100,
        'account_age_days': account_age
    }
    
    return UserStats(**stats_data)

# Error handling for validation
@app.exception_handler(ValueError)
async def validation_exception_handler(request, exc):
    return HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=str(exc)
    )
```

## Question 12: Explain the concept of WebSockets and their use cases

WebSockets provide a persistent, full-duplex communication channel between client and server, allowing real-time data exchange.

### Key Characteristics:

**1. Persistent Connection**: Connection stays open after initial handshake
**2. Bi-directional**: Both client and server can send messages
**3. Low Latency**: No HTTP overhead for each message
**4. Real-time**: Immediate message delivery

### Common Use Cases:

- Chat applications
- Live notifications
- Real-time gaming
- Live data feeds (stock prices, sports scores)
- Collaborative editing
- Live streaming
- IoT device communication

```python
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from typing import List, Dict
import json
import asyncio
from datetime import datetime

app = FastAPI()

class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []
        self.user_connections: Dict[str, WebSocket] = {}
        self.room_connections: Dict[str, List[WebSocket]] = {}
    
    async def connect(self, websocket: WebSocket, user_id: str = None):
        await websocket.accept()
        self.active_connections.append(websocket)
        if user_id:
            self.user_connections[user_id] = websocket
    
    def disconnect(self, websocket: WebSocket, user_id: str = None):
        self.active_connections.remove(websocket)
        if user_id and user_id in self.user_connections:
            del self.user_connections[user_id]
    
    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)
    
    async def send_to_user(self, message: str, user_id: str):
        if user_id in self.user_connections:
            websocket = self.user_connections[user_id]
            await websocket.send_text(message)
    
    async def broadcast(self, message: str):
        for connection in self.active_connections:
            try:
                await connection.send_text(message)
            except:
                # Remove disconnected clients
                self.active_connections.remove(connection)
    
    async def broadcast_to_room(self, message: str, room: str):
        if room in self.room_connections:
            for connection in self.room_connections[room]:
                try:
                    await connection.send_text(message)
                except:
                    self.room_connections[room].remove(connection)

manager = ConnectionManager()

# Basic WebSocket endpoint
@app.websocket("/ws/{user_id}")
async def websocket_endpoint(websocket: WebSocket, user_id: str):
    await manager.connect(websocket, user_id)
    try:
        while True:
            # Receive message from client
            data = await websocket.receive_text()
            message = json.loads(data)
            
            # Process different message types
            if message['type'] == 'chat':
                chat_message = {
                    'type': 'chat',
                    'user_id': user_id,
                    'message': message['content'],
                    'timestamp': datetime.now().isoformat()
                }
                await manager.broadcast(json.dumps(chat_message))
            
            elif message['type'] == 'private':
                private_message = {
                    'type': 'private',
                    'from': user_id,
                    'message': message['content'],
                    'timestamp': datetime.now().isoformat()
                }
                await manager.send_to_user(
                    json.dumps(private_message),
                    message['to_user']
                )
    
    except WebSocketDisconnect:
        manager.disconnect(websocket, user_id)
        disconnect_message = {
            'type': 'user_disconnect',
            'user_id': user_id,
            'timestamp': datetime.now().isoformat()
        }
        await manager.broadcast(json.dumps(disconnect_message))
```

## Question 13: Demonstrate how to implement WebSockets in FastAPI

```python
from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Depends
from fastapi.responses import HTMLResponse
from typing import List, Dict, Optional
import json
import asyncio
from datetime import datetime
import uuid

app = FastAPI()

# HTML client for testing
html_client = """
<!DOCTYPE html>
<html>
<head>
    <title>WebSocket Chat</title>
</head>
<body>
    <h1>WebSocket Chat</h1>
    <div id="messages"></div>
    <input type="text" id="messageInput" placeholder="Type a message...">
    <button onclick="sendMessage()">Send</button>
    
    <script>
        const ws = new WebSocket("ws://localhost:8000/ws/user123");
        const messages = document.getElementById('messages');
        
        ws.onmessage = function(event) {
            const message = JSON.parse(event.data);
            const messageElement = document.createElement('div');
            messageElement.textContent = `${message.user}: ${message.text}`;
            messages.appendChild(messageElement);
        };
        
        function sendMessage() {
            const input = document.getElementById('messageInput');
            const message = {
                type: 'chat',
                text: input.value,
                timestamp: new Date().toISOString()
            };
            ws.send(JSON.stringify(message));
            input.value = '';
        }
        
        document.getElementById('messageInput').addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                sendMessage();
            }
        });
    </script>
</body>
</html>
"""

@app.get("/")
async def get_client():
    return HTMLResponse(html_client)

# Advanced WebSocket implementation with rooms and authentication
class ChatRoom:
    def __init__(self, room_id: str):
        self.room_id = room_id
        self.connections: Dict[str, WebSocket] = {}
        self.message_history: List[Dict] = []
    
    async def add_user(self, user_id: str, websocket: WebSocket):
        self.connections[user_id] = websocket
        
        # Send message history to new user
        for message in self.message_history[-50:]:  # Last 50 messages
            await websocket.send_text(json.dumps(message))
        
        # Notify others about new user
        join_message = {
            'type': 'user_joined',
            'user_id': user_id,
            'room_id': self.room_id,
            'timestamp': datetime.now().isoformat(),
            'message': f'{user_id} joined the room'
        }
        await self.broadcast_message(join_message, exclude_user=user_id)
    
    async def remove_user(self, user_id: str):
        if user_id in self.connections:
            del self.connections[user_id]
            
            # Notify others about user leaving
            leave_message = {
                'type': 'user_left',
                'user_id': user_id,
                'room_id': self.room_id,
                'timestamp': datetime.now().isoformat(),
                'message': f'{user_id} left the room'
            }
            await self.broadcast_message(leave_message)
    
    async def broadcast_message(self, message: Dict, exclude_user: str = None):
        self.message_history.append(message)
        
        # Keep only last 100 messages in memory
        if len(self.message_history) > 100:
            self.message_history = self.message_history[-100:]
        
        disconnected_users = []
        for user_id, websocket in self.connections.items():
            if user_id != exclude_user:
                try:
                    await websocket.send_text(json.dumps(message))
                except:
                    disconnected_users.append(user_id)
        
        # Clean up disconnected users
        for user_id in disconnected_users:
            del self.connections[user_id]
    
    def get_active_users(self) -> List[str]:
        return list(self.connections.keys())

class ChatManager:
    def __init__(self):
        self.rooms: Dict[str, ChatRoom] = {}
    
    def get_room(self, room_id: str) -> ChatRoom:
        if room_id not in self.rooms:
            self.rooms[room_id] = ChatRoom(room_id)
        return self.rooms[room_id]
    
    async def join_room(self, room_id: str, user_id: str, websocket: WebSocket):
        room = self.get_room(room_id)
        await room.add_user(user_id, websocket)
        return room
    
    async def leave_room(self, room_id: str, user_id: str):
        if room_id in self.rooms:
            await self.rooms[room_id].remove_user(user_id)
            
            # Remove empty rooms
            if not self.rooms[room_id].connections:
                del self.rooms[room_id]

chat_manager = ChatManager()

# Authentication dependency (simplified)
async def get_current_user(token: str = None) -> str:
    # In real implementation, validate JWT token
    if not token:
        return f"anonymous_{uuid.uuid4().hex[:8]}"
    return token

# WebSocket endpoint with room support
@app.websocket("/ws/{room_id}/{user_id}")
async def websocket_chat_room(
    websocket: WebSocket,
    room_id: str,
    user_id: str
):
    await websocket.accept()
    room = await chat_manager.join_room(room_id, user_id, websocket)
    
    try:
        while True:
            # Receive message from client
            data = await websocket.receive_text()
            message_data = json.loads(data)
            
            # Create message object
            message = {
                'type': message_data.get('type', 'chat'),
                'user_id': user_id,
                'room_id': room_id,
                'text': message_data.get('text', ''),
                'timestamp': datetime.now().isoformat(),
                'message_id': str(uuid.uuid4())
            }
            
            # Handle different message types
            if message['type'] == 'chat':
                await room.broadcast_message(message)
            
            elif message['type'] == 'typing':
                typing_message = {
                    'type': 'typing',
                    'user_id': user_id,
                    'room_id': room_id,
                    'is_typing': message_data.get('is_typing', False)
                }
                await room.broadcast_message(typing_message, exclude_user=user_id)
            
            elif message['type'] == 'get_users':
                users_message = {
                    'type': 'active_users',
                    'users': room.get_active_users(),
                    'room_id': room_id
                }
                await websocket.send_text(json.dumps(users_message))
    
    except WebSocketDisconnect:
        await chat_manager.leave_room(room_id, user_id)

# WebSocket endpoint for real-time notifications
class NotificationManager:
    def __init__(self):
        self.user_connections: Dict[str, WebSocket] = {}
    
    async def connect_user(self, user_id: str, websocket: WebSocket):
        await websocket.accept()
        self.user_connections[user_id] = websocket
    
    async def disconnect_user(self, user_id: str):
        if user_id in self.user_connections:
            del self.user_connections[user_id]
    
    async def send_notification(self, user_id: str, notification: Dict):
        if user_id in self.user_connections:
            try:
                await self.user_connections[user_id].send_text(json.dumps(notification))
                return True
            except:
                del self.user_connections[user_id]
                return False
        return False
    
    async def broadcast_notification(self, notification: Dict, user_ids: List[str] = None):
        target_users = user_ids or list(self.user_connections.keys())
        sent_count = 0
        
        for user_id in target_users:
            if await self.send_notification(user_id, notification):
                sent_count += 1
        
        return sent_count

notification_manager = NotificationManager()

@app.websocket("/notifications/{user_id}")
async def websocket_notifications(websocket: WebSocket, user_id: str):
    await notification_manager.connect_user(user_id, websocket)
    
    try:
        while True:
            # Keep connection alive and handle ping/pong
            data = await websocket.receive_text()
            if data == "ping":
                await websocket.send_text("pong")
    
    except WebSocketDisconnect:
        await notification_manager.disconnect_user(user_id)

# REST endpoint to send notifications
@app.post("/send-notification/")
async def send_notification(
    user_id: str,
    title: str,
    message: str,
    notification_type: str = "info"
):
    notification = {
        'type': 'notification',
        'title': title,
        'message': message,
        'notification_type': notification_type,
        'timestamp': datetime.now().isoformat(),
        'id': str(uuid.uuid4())
    }
    
    sent = await notification_manager.send_notification(user_id, notification)
    return {
        'sent': sent,
        'user_id': user_id,
        'notification': notification
    }

# WebSocket endpoint for live data streaming
@app.websocket("/live-data/{data_type}")
async def websocket_live_data(websocket: WebSocket, data_type: str):
    await websocket.accept()
    
    try:
        while True:
            # Simulate live data based on type
            if data_type == "stock_prices":
                data = {
                    'type': 'stock_update',
                    'symbol': 'AAPL',
                    'price': 150.00 + (asyncio.get_event_loop().time() % 10),
                    'timestamp': datetime.now().isoformat()
                }
            elif data_type == "system_metrics":
                data = {
                    'type': 'metrics',
                    'cpu_usage': 45.5,
                    'memory_usage': 67.8,
                    'disk_usage': 23.4,
                    'timestamp': datetime.now().isoformat()
                }
            else:
                data = {
                    'type': 'generic_data',
                    'value': f"Live data for {data_type}",
                    'timestamp': datetime.now().isoformat()
                }
            
            await websocket.send_text(json.dumps(data))
            await asyncio.sleep(1)  # Send data every second
    
    except WebSocketDisconnect:
        pass

## Question 14: Discuss challenges and best practices for WebSocket development

### Common Challenges:

**1. Connection Management**: Handling connection drops and reconnections
**2. Scalability**: Managing thousands of concurrent connections
**3. Message Ordering**: Ensuring message delivery order
**4. Error Handling**: Graceful handling of network issues
**5. Authentication**: Securing WebSocket connections
**6. Resource Management**: Memory leaks from unclosed connections

### Best Practices:

```python
from fastapi import FastAPI, WebSocket, WebSocketDisconnect, HTTPException
import asyncio
import logging
import json
from typing import Dict, Set
import time
import weakref

app = FastAPI()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class WebSocketConnection:
    def __init__(self, websocket: WebSocket, user_id: str):
        self.websocket = websocket
        self.user_id = user_id
        self.connected_at = time.time()
        self.last_ping = time.time()
        self.message_queue = asyncio.Queue(maxsize=100)
    
    async def send_safe(self, message: str) -> bool:
        """Safely send message with error handling"""
        try:
            await self.websocket.send_text(message)
            return True
        except Exception as e:
            logger.error(f"Failed to send message to {self.user_id}: {e}")
            return False
    
    async def ping(self) -> bool:
        """Send ping to keep connection alive"""
        try:
            await self.websocket.send_text(json.dumps({"type": "ping"}))
            self.last_ping = time.time()
            return True
        except:
            return False
    
    def is_alive(self) -> bool:
        """Check if connection is still alive"""
        return time.time() - self.last_ping < 60  # 60 seconds timeout

class RobustConnectionManager:
    def __init__(self):
        self.connections: Dict[str, WebSocketConnection] = {}
        self.room_connections: Dict[str, Set[str]] = {}
        self._cleanup_task = None
        self._heartbeat_task = None
    
    async def start_background_tasks(self):
        """Start background maintenance tasks"""
        self._cleanup_task = asyncio.create_task(self._cleanup_dead_connections())
        self._heartbeat_task = asyncio.create_task(self._heartbeat_monitor())
    
    async def stop_background_tasks(self):
        """Stop background tasks"""
        if self._cleanup_task:
            self._cleanup_task.cancel()
        if self._heartbeat_task:
            self._heartbeat_task.cancel()
    
    async def connect(self, websocket: WebSocket, user_id: str, room_id: str = None):
        """Connect user with proper error handling"""
        try:
            await websocket.accept()
            
            # Disconnect existing connection for the same user
            if user_id in self.connections:
                await self.disconnect(user_id)
            
            connection = WebSocketConnection(websocket, user_id)
            self.connections[user_id] = connection
            
            # Add to room if specified
            if room_id:
                if room_id not in self.room_connections:
                    self.room_connections[room_id] = set()
                self.room_connections[room_id].add(user_id)
            
            logger.info(f"User {user_id} connected to room {room_id}")
            
            # Send welcome message
            welcome_msg = {
                "type": "welcome",
                "message": f"Welcome {user_id}!",
                "timestamp": time.time()
            }
            await connection.send_safe(json.dumps(welcome_msg))
            
        except Exception as e:
            logger.error(f"Failed to connect user {user_id}: {e}")
            raise HTTPException(status_code=500, detail="Connection failed")
    
    async def disconnect(self, user_id: str):
        """Safely disconnect user"""
        if user_id in self.connections:
            connection = self.connections[user_id]
            
            try:
                await connection.websocket.close()
            except:
                pass  # Connection might already be closed
            
            del self.connections[user_id]
            
            # Remove from all rooms
            for room_users in self.room_connections.values():
                room_users.discard(user_id)
            
            logger.info(f"User {user_id} disconnected")
    
    async def send_to_user(self, user_id: str, message: Dict) -> bool:
        """Send message to specific user with retry logic"""
        if user_id not in self.connections:
            return False
        
        connection = self.connections[user_id]
        message_str = json.dumps(message)
        
        # Try to send with retry
        for attempt in range(3):
            if await connection.send_safe(message_str):
                return True
            
            await asyncio.sleep(0.1 * (attempt + 1))  # Exponential backoff
        
        # Failed to send, disconnect user
        await self.disconnect(user_id)
        return False
    
    async def broadcast_to_room(self, room_id: str, message: Dict, exclude_user: str = None):
        """Broadcast message to all users in room"""
        if room_id not in self.room_connections:
            return 0
        
        sent_count = 0
        failed_users = []
        
        for user_id in self.room_connections[room_id]:
            if user_id != exclude_user:
                if await self.send_to_user(user_id, message):
                    sent_count += 1
                else:
                    failed_users.append(user_id)
        
        # Remove failed users from room
        for user_id in failed_users:
            self.room_connections[room_id].discard(user_id)
        
        return sent_count
    
    async def _cleanup_dead_connections(self):
        """Background task to clean up dead connections"""
        while True:
            try:
                dead_users = []
                
                for user_id, connection in self.connections.items():
                    if not connection.is_alive():
                        dead_users.append(user_id)
                
                for user_id in dead_users:
                    await self.disconnect(user_id)
                
                await asyncio.sleep(30)  # Check every 30 seconds
                
            except Exception as e:
                logger.error(f"Error in cleanup task: {e}")
                await asyncio.sleep(30)
    
    async def _heartbeat_monitor(self):
        """Background task to send heartbeat pings"""
        while True:
            try:
                for connection in self.connections.values():
                    await connection.ping()
                
                await asyncio.sleep(30)  # Ping every 30 seconds
                
            except Exception as e:
                logger.error(f"Error in heartbeat task: {e}")
                await asyncio.sleep(30)

# Initialize connection manager
connection_manager = RobustConnectionManager()

@app.on_event("startup")
async def startup_event():
    await connection_manager.start_background_tasks()

@app.on_event("shutdown")
async def shutdown_event():
    await connection_manager.stop_background_tasks()

# Rate limiting for WebSocket messages
class RateLimiter:
    def __init__(self, max_messages: int = 10, window_seconds: int = 60):
        self.max_messages = max_messages
        self.window_seconds = window_seconds
        self.user_messages: Dict[str, list] = {}
    
    def is_allowed(self, user_id: str) -> bool:
        now = time.time()
        
        if user_id not in self.user_messages:
            self.user_messages[user_id] = []
        
        # Remove old messages outside the window
        self.user_messages[user_id] = [
            msg_time for msg_time in self.user_messages[user_id]
            if now - msg_time < self.window_seconds
        ]
        
        # Check if under limit
        if len(self.user_messages[user_id]) < self.max_messages:
            self.user_messages[user_id].append(now)
            return True
        
        return False

rate_limiter = RateLimiter()

@app.websocket("/ws/robust/{room_id}/{user_id}")
async def robust_websocket(websocket: WebSocket, room_id: str, user_id: str):
    await connection_manager.connect(websocket, user_id, room_id)
    
    try:
        while True:
            data = await websocket.receive_text()
            
            # Rate limiting
            if not rate_limiter.is_allowed(user_id):
                error_msg = {
                    "type": "error",
                    "message": "Rate limit exceeded"
                }
                await websocket.send_text(json.dumps(error_msg))
                continue
            
            try:
                message = json.loads(data)
                
                # Handle different message types
                if message.get('type') == 'chat':
                    chat_message = {
                        'type': 'chat',
                        'user_id': user_id,
                        'room_id': room_id,
                        'text': message.get('text', ''),
                        'timestamp': time.time()
                    }
                    await connection_manager.broadcast_to_room(
                        room_id, chat_message, exclude_user=user_id
                    )
                
                elif message.get('type') == 'pong':
                    # Update last ping time
                    if user_id in connection_manager.connections:
                        connection_manager.connections[user_id].last_ping = time.time()
                
            except json.JSONDecodeError:
                error_msg = {
                    "type": "error",
                    "message": "Invalid JSON format"
                }
                await websocket.send_text(json.dumps(error_msg))
    
    except WebSocketDisconnect:
        await connection_manager.disconnect(user_id)
    except Exception as e:
        logger.error(f"WebSocket error for user {user_id}: {e}")
        await connection_manager.disconnect(user_id)

## Question 15: Explain background tasks and their use cases

Background tasks in FastAPI allow you to run operations after returning a response to the client, without making the client wait.

### Common Use Cases:

**1. Email Sending**: Send confirmation emails after user registration
**2. File Processing**: Process uploaded files asynchronously
**3. Database Cleanup**: Clean up expired records
**4. Logging and Analytics**: Record user activities
**5. Cache Warming**: Pre-populate cache with frequently accessed data
**6. Notifications**: Send push notifications to mobile devices

```python
from fastapi import FastAPI, BackgroundTasks, HTTPException
from pydantic import BaseModel, EmailStr
import smtplib
import logging
import asyncio
import os
from email.mime.text import MimeText
from email.mime.multipart import MimeMultipart
from typing import List

app = FastAPI()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Models
class UserRegistration(BaseModel):
    username: str
    email: EmailStr
    password: str

class EmailData(BaseModel):
    recipient: EmailStr
    subject: str
    body: str

# Background task functions
async def send_email(email_data: EmailData):
    """Send email in background"""
    try:
        # Email configuration (use environment variables in production)
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        sender_email = os.getenv("SENDER_EMAIL")
        sender_password = os.getenv("SENDER_PASSWORD")
        
        # Create message
        message = MimeMultipart()
        message["From"] = sender_email
        message["To"] = email_data.recipient
        message["Subject"] = email_data.subject
        message.attach(MimeText(email_data.body, "plain"))
        
        # Send email
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        text = message.as_string()
        server.sendmail(sender_email, email_data.recipient, text)
        server.quit()
        
        logger.info(f"Email sent successfully to {email_data.recipient}")
        
    except Exception as e:
        logger.error(f"Failed to send email to {email_data.recipient}: {e}")

def log_user_activity(user_id: int, activity: str, details: dict = None):
    """Log user activity for analytics"""
    try:
        # Simulate logging to database or external service
        log_entry = {
            'user_id': user_id,
            'activity': activity,
            'details': details or {},
            'timestamp': asyncio.get_event_loop().time()
        }
        
        # In real application, save to database
        logger.info(f"Activity logged: {log_entry}")
        
    except Exception as e:
        logger.error(f"Failed to log activity: {e}")

async def process_uploaded_file(file_path: str, user_id: int):
    """Process uploaded file in background"""
    try:
        # Simulate file processing
        await asyncio.sleep(2)  # Simulate processing time
        
        # File processing logic here
        processed_data = {
            'file_path': file_path,
            'user_id': user_id,
            'status': 'processed',
            'processed_at': asyncio.get_event_loop().time()
        }
        
        logger.info(f"File processed: {processed_data}")
        
        # Notify user that processing is complete
        notification_data = EmailData(
            recipient=f"user{user_id}@example.com",
            subject="File Processing Complete",
            body=f"Your file {file_path} has been processed successfully."
        )
        await send_email(notification_data)
        
    except Exception as e:
        logger.error(f"Failed to process file {file_path}: {e}")

def cleanup_expired_sessions():
    """Clean up expired user sessions"""
    try:
        # Simulate database cleanup
        current_time = asyncio.get_event_loop().time()
        expired_count = 0
        
        # In real application, delete from database
        # expired_sessions = db.query(Session).filter(Session.expires_at < current_time).all()
        # for session in expired_sessions:
        #     db.delete(session)
        # expired_count = len(expired_sessions)
        # db.commit()
        
        logger.info(f"Cleaned up {expired_count} expired sessions")
        
    except Exception as e:
        logger.error(f"Failed to cleanup sessions: {e}")

# Endpoints using background tasks
@app.post("/register/")
async def register_user(user: UserRegistration, background_tasks: BackgroundTasks):
    """Register user and send welcome email in background"""
    
    # Create user in database (simulate)
    user_id = 123  # Simulated user ID
    
    # Add background tasks
    welcome_email = EmailData(
        recipient=user.email,
        subject="Welcome to Our Platform!",
        body=f"Hello {user.username}, welcome to our platform!"
    )
    background_tasks.add_task(send_email, welcome_email)
    
    # Log registration activity
    background_tasks.add_task(
        log_user_activity,
        user_id,
        "user_registered",
        {"username": user.username, "email": user.email}
    )
    
    # Return immediate response
    return {
        "message": "User registered successfully",
        "user_id": user_id,
        "username": user.username
    }

@app.post("/upload-file/")
async def upload_file(
    file_name: str,
    user_id: int,
    background_tasks: BackgroundTasks
):
    """Upload file and process in background"""
    
    # Simulate file upload
    file_path = f"/uploads/{file_name}"
    
    # Add background file processing task
    background_tasks.add_task(process_uploaded_file, file_path, user_id)
    
    # Log upload activity
    background_tasks.add_task(
        log_user_activity,
        user_id,
        "file_uploaded",
        {"file_name": file_name, "file_path": file_path}
    )
    
    return {
        "message": "File uploaded successfully",
        "file_path": file_path,
        "status": "processing"
    }

@app.post("/admin/cleanup/")
async def trigger_cleanup(background_tasks: BackgroundTasks):
    """Trigger system cleanup tasks"""
    
    # Add cleanup tasks
    background_tasks.add_task(cleanup_expired_sessions)
    
    return {"message": "Cleanup tasks scheduled"}

# Multiple background tasks example
@app.post("/send-newsletter/")
async def send_newsletter(
    subject: str,
    content: str,
    recipient_ids: List[int],
    background_tasks: BackgroundTasks
):
    """Send newsletter to multiple recipients"""
    
    # Get recipients from database (simulate)
    recipients = [f"user{uid}@example.com" for uid in recipient_ids]
    
    # Add email task for each recipient
    for recipient in recipients:
        email_data = EmailData(
            recipient=recipient,
            subject=subject,
            body=content
        )
        background_tasks.add_task(send_email, email_data)
    
    # Log newsletter activity
    background_tasks.add_task(
        log_user_activity,
        0,  # System user
        "newsletter_sent",
        {
            "subject": subject,
            "recipient_count": len(recipients)
        }
    )
    
    return {
        "message": f"Newsletter scheduled for {len(recipients)} recipients",
        "subject": subject
    }

## Question 16: Demonstrate how to create background tasks using FastAPI

```python
from fastapi import FastAPI, BackgroundTasks, HTTPException, Depends
from pydantic import BaseModel, EmailStr
import asyncio
import json
import time
from typing import Dict, List, Optional
import uuid
from datetime import datetime, timedelta

app = FastAPI()

# Task status tracking
task_status: Dict[str, Dict] = {}

class TaskResult(BaseModel):
    task_id: str
    status: str  # pending, running, completed, failed
    result: Optional[Dict] = None
    error: Optional[str] = None
    created_at: datetime
    completed_at: Optional[datetime] = None

class EmailTask(BaseModel):
    recipient: EmailStr
    subject: str
    body: str
    template: Optional[str] = None

class DataProcessingTask(BaseModel):
    data: List[Dict]
    operation: str  # sum, average, filter, etc.
    parameters: Dict = {}

# Background task implementations
async def send_email_task(task_id: str, email_data: EmailTask):
    """Send email with task tracking"""
    try:
        # Update status to running
        task_status[task_id].update({
            'status': 'running',
            'started_at': datetime.now()
        })
        
        # Simulate email sending
        await asyncio.sleep(2)  # Simulate network delay
        
        # Email sending logic would go here
        result = {
            'recipient': email_data.recipient,
            'subject': email_data.subject,
            'sent_at': datetime.now().isoformat(),
            'message_id': str(uuid.uuid4())
        }
        
        # Update status to completed
        task_status[task_id].update({
            'status': 'completed',
            'result': result,
            'completed_at': datetime.now()
        })
        
    except Exception as e:
        # Update status to failed
        task_status[task_id].update({
            'status': 'failed',
            'error': str(e),
            'completed_at': datetime.now()
        })

async def process_data_task(task_id: str, processing_data: DataProcessingTask):
    """Process data with task tracking"""
    try:
        task_status[task_id].update({
            'status': 'running',
            'started_at': datetime.now()
        })
        
        # Simulate data processing
        await asyncio.sleep(3)
        
        data = processing_data.data
        operation = processing_data.operation
        parameters = processing_data.parameters
        
        result = {}
        
        if operation == 'sum':
            field = parameters.get('field', 'value')
            total = sum(item.get(field, 0) for item in data)
            result = {'operation': 'sum', 'field': field, 'result': total}
            
        elif operation == 'average':
            field = parameters.get('field', 'value')
            values = [item.get(field, 0) for item in data if field in item]
            avg = sum(values) / len(values) if values else 0
            result = {'operation': 'average', 'field': field, 'result':
    

# FastAPI Comprehensive Guide - Advanced Topics

## 16. What are CORS, and how do you handle them in FastAPI?

**CORS (Cross-Origin Resource Sharing)** is a security feature implemented by web browsers that restricts web pages from making requests to a different domain, protocol, or port than the one serving the web page.

### Handling CORS in FastAPI:

```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "https://mydomain.com"],  # Specific origins
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

# For development (allow all origins)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/data")
async def get_data():
    return {"message": "Hello from FastAPI"}
```

### CORS Configuration Options:

- **allow_origins**: List of allowed origins
- **allow_credentials**: Whether to allow cookies/credentials
- **allow_methods**: Allowed HTTP methods
- **allow_headers**: Allowed headers
- **expose_headers**: Headers exposed to the client

## 17. How do you upload files in FastAPI?

FastAPI provides excellent support for file uploads using `UploadFile` and `File`.

### Basic File Upload:

```python
from fastapi import FastAPI, File, UploadFile, HTTPException
from typing import List
import shutil
import os

app = FastAPI()

@app.post("/upload-file/")
async def upload_file(file: UploadFile = File(...)):
    # Validate file type
    if not file.content_type.startswith('image/'):
        raise HTTPException(status_code=400, detail="Only image files allowed")
    
    # Save file
    file_location = f"uploads/{file.filename}"
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "size": file.size
    }

@app.post("/upload-multiple/")
async def upload_multiple_files(files: List[UploadFile] = File(...)):
    file_info = []
    for file in files:
        file_location = f"uploads/{file.filename}"
        with open(file_location, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        file_info.append({
            "filename": file.filename,
            "size": file.size
        })
    
    return {"uploaded_files": file_info}

# File upload with additional form data
from fastapi import Form

@app.post("/upload-with-metadata/")
async def upload_with_metadata(
    file: UploadFile = File(...),
    description: str = Form(...),
    category: str = Form(...)
):
    return {
        "filename": file.filename,
        "description": description,
        "category": category
    }
```

### Advanced File Handling:

```python
import aiofiles
from pathlib import Path

@app.post("/upload-async/")
async def upload_file_async(file: UploadFile = File(...)):
    upload_dir = Path("uploads")
    upload_dir.mkdir(exist_ok=True)
    
    file_path = upload_dir / file.filename
    
    async with aiofiles.open(file_path, 'wb') as f:
        content = await file.read()
        await f.write(content)
    
    return {"filename": file.filename, "saved_at": str(file_path)}
```

## 18. How do you implement pagination in FastAPI?

Pagination is essential for handling large datasets efficiently.

### Basic Pagination:

```python
from fastapi import FastAPI, Query, Depends
from sqlalchemy.orm import Session
from typing import List, Optional

app = FastAPI()

class PaginationParams:
    def __init__(
        self,
        page: int = Query(1, ge=1, description="Page number"),
        size: int = Query(20, ge=1, le=100, description="Page size")
    ):
        self.page = page
        self.size = size
        self.offset = (page - 1) * size

@app.get("/items/")
async def get_items(
    pagination: PaginationParams = Depends(),
    db: Session = Depends(get_db)
):
    # Get total count
    total = db.query(Item).count()
    
    # Get paginated items
    items = db.query(Item)\
        .offset(pagination.offset)\
        .limit(pagination.size)\
        .all()
    
    return {
        "items": items,
        "pagination": {
            "page": pagination.page,
            "size": pagination.size,
            "total": total,
            "pages": (total + pagination.size - 1) // pagination.size
        }
    }
```

### Advanced Pagination with Filtering:

```python
from pydantic import BaseModel

class ItemFilter(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    min_price: Optional[float] = None
    max_price: Optional[float] = None

@app.get("/items/advanced/")
async def get_items_advanced(
    pagination: PaginationParams = Depends(),
    filters: ItemFilter = Depends(),
    db: Session = Depends(get_db)
):
    query = db.query(Item)
    
    # Apply filters
    if filters.name:
        query = query.filter(Item.name.ilike(f"%{filters.name}%"))
    if filters.category:
        query = query.filter(Item.category == filters.category)
    if filters.min_price:
        query = query.filter(Item.price >= filters.min_price)
    if filters.max_price:
        query = query.filter(Item.price <= filters.max_price)
    
    total = query.count()
    items = query.offset(pagination.offset).limit(pagination.size).all()
    
    return {
        "items": items,
        "pagination": {
            "page": pagination.page,
            "size": pagination.size,
            "total": total,
            "pages": (total + pagination.size - 1) // pagination.size,
            "has_next": pagination.page * pagination.size < total,
            "has_prev": pagination.page > 1
        }
    }
```

## 19. What is the difference between @app.get() and @app.post() in FastAPI?

The main differences lie in HTTP methods, intended use, and how data is handled.

### @app.get() - HTTP GET Method:

```python
@app.get("/users/{user_id}")
async def get_user(user_id: int):
    """
    GET requests are used for:
    - Retrieving data
    - Should be idempotent (multiple calls don't change state)
    - Parameters typically in URL path or query parameters
    - No request body
    """
    return {"user_id": user_id, "name": "John Doe"}

@app.get("/search")
async def search_items(q: str, limit: int = 10):
    """Query parameters for GET requests"""
    return {"query": q, "limit": limit, "results": []}
```

### @app.post() - HTTP POST Method:

```python
from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    email: str
    age: int

@app.post("/users/")
async def create_user(user: UserCreate):
    """
    POST requests are used for:
    - Creating new resources
    - Submitting data to be processed
    - Can change server state
    - Data typically in request body
    """
    return {"message": "User created", "user": user}

@app.post("/login/")
async def login(credentials: dict):
    """POST for sensitive data like passwords"""
    return {"access_token": "token123"}
```

### Comparison Table:

| Aspect | @app.get() | @app.post() |
|--------|------------|-------------|
| Purpose | Retrieve data | Create/Submit data |
| Idempotent | Yes | No |
| Request Body | No | Yes |
| Caching | Cacheable | Not cacheable |
| URL Length Limit | Yes | No (data in body) |
| Security | Less secure for sensitive data | More secure |

## 20. How can you customize exception handling in FastAPI?

FastAPI provides multiple ways to handle exceptions globally and specifically.

### Custom Exception Classes:

```python
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

app = FastAPI()

# Custom exception class
class CustomException(Exception):
    def __init__(self, name: str):
        self.name = name

# Global exception handler for custom exceptions
@app.exception_handler(CustomException)
async def custom_exception_handler(request: Request, exc: CustomException):
    return JSONResponse(
        status_code=418,
        content={"message": f"Custom error occurred: {exc.name}"}
    )

# Override default HTTP exception handler
@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": "HTTP Exception",
            "detail": exc.detail,
            "status_code": exc.status_code
        }
    )

# Handle validation errors
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content={
            "error": "Validation Error",
            "details": exc.errors(),
            "body": exc.body
        }
    )

@app.get("/items/{item_id}")
async def get_item(item_id: int):
    if item_id == 0:
        raise CustomException(name="Invalid item ID")
    return {"item_id": item_id}
```

### Advanced Exception Handling:

```python
import logging
from datetime import datetime

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DatabaseException(Exception):
    def __init__(self, message: str, error_code: str = None):
        self.message = message
        self.error_code = error_code
        super().__init__(self.message)

@app.exception_handler(DatabaseException)
async def database_exception_handler(request: Request, exc: DatabaseException):
    logger.error(f"Database error: {exc.message}")
    
    return JSONResponse(
        status_code=500,
        content={
            "error": "Database Error",
            "message": exc.message,
            "error_code": exc.error_code,
            "timestamp": datetime.now().isoformat()
        }
    )

# Generic exception handler for unexpected errors
@app.exception_handler(Exception)
async def generic_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unexpected error: {str(exc)}")
    
    return JSONResponse(
        status_code=500,
        content={
            "error": "Internal Server Error",
            "message": "An unexpected error occurred"
        }
    )
```

## 21. How do you handle form data in FastAPI?

FastAPI can handle various types of form data including URL-encoded and multipart forms.

### URL-Encoded Form Data:

```python
from fastapi import FastAPI, Form
from pydantic import BaseModel

app = FastAPI()

@app.post("/login/")
async def login(username: str = Form(...), password: str = Form(...)):
    return {"username": username}

# Multiple form fields
@app.post("/submit-form/")
async def submit_form(
    name: str = Form(...),
    email: str = Form(...),
    age: int = Form(...),
    subscribe: bool = Form(False)
):
    return {
        "name": name,
        "email": email,
        "age": age,
        "subscribe": subscribe
    }
```

### Form Data with File Uploads:

```python
@app.post("/profile/")
async def create_profile(
    username: str = Form(...),
    bio: str = Form(...),
    avatar: UploadFile = File(None)
):
    profile_data = {"username": username, "bio": bio}
    
    if avatar:
        profile_data["avatar"] = {
            "filename": avatar.filename,
            "content_type": avatar.content_type
        }
    
    return profile_data
```

### Form Models with Pydantic:

```python
from typing import Optional

class UserForm(BaseModel):
    username: str
    email: str
    full_name: Optional[str] = None

@app.post("/users/form/")
async def create_user_form(
    username: str = Form(...),
    email: str = Form(...),
    full_name: Optional[str] = Form(None)
):
    # Create Pydantic model from form data
    user_data = UserForm(
        username=username,
        email=email,
        full_name=full_name
    )
    return user_data
```

## 22. How do you handle multiple query parameters in FastAPI?

FastAPI provides several ways to handle multiple query parameters effectively.

### Basic Query Parameters:

```python
from typing import Optional, List
from fastapi import Query

@app.get("/search/")
async def search_items(
    q: Optional[str] = None,
    skip: int = 0,
    limit: int = Query(default=10, le=100),
    sort_by: Optional[str] = Query(None, regex="^(name|date|price)$")
):
    return {
        "query": q,
        "skip": skip,
        "limit": limit,
        "sort_by": sort_by
    }
```

### Query Parameter Lists:

```python
@app.get("/items/")
async def get_items(
    categories: List[str] = Query(None),
    tags: List[str] = Query([]),
    ids: List[int] = Query(None)
):
    return {
        "categories": categories,
        "tags": tags,
        "ids": ids
    }
# URL: /items/?categories=electronics&categories=books&tags=new&ids=1&ids=2
```

### Query Parameters with Dependencies:

```python
class CommonQueryParams:
    def __init__(
        self,
        skip: int = 0,
        limit: int = Query(default=10, le=100),
        sort: str = Query("created_at", regex="^(created_at|updated_at|name)$"),
        order: str = Query("desc", regex="^(asc|desc)$")
    ):
        self.skip = skip
        self.limit = limit
        self.sort = sort
        self.order = order

@app.get("/products/")
async def get_products(commons: CommonQueryParams = Depends()):
    return {
        "skip": commons.skip,
        "limit": commons.limit,
        "sort": commons.sort,
        "order": commons.order
    }
```

### Advanced Query Parameter Handling:

```python
from enum import Enum

class SortOrder(str, Enum):
    asc = "asc"
    desc = "desc"

class Category(str, Enum):
    electronics = "electronics"
    books = "books"
    clothing = "clothing"

@app.get("/advanced-search/")
async def advanced_search(
    q: Optional[str] = Query(None, min_length=3, max_length=50),
    category: Optional[Category] = None,
    min_price: Optional[float] = Query(None, ge=0),
    max_price: Optional[float] = Query(None, ge=0),
    in_stock: bool = Query(True),
    sort_order: SortOrder = SortOrder.desc,
    page: int = Query(1, ge=1),
    per_page: int = Query(20, ge=1, le=100)
):
    return {
        "query": q,
        "filters": {
            "category": category,
            "min_price": min_price,
            "max_price": max_price,
            "in_stock": in_stock
        },
        "sorting": {
            "order": sort_order
        },
        "pagination": {
            "page": page,
            "per_page": per_page
        }
    }
```

## 23. What are request and response objects in FastAPI?

Request and response objects provide access to raw HTTP data and allow customization of responses.

### Request Object:

```python
from fastapi import FastAPI, Request
from starlette.responses import JSONResponse

app = FastAPI()

@app.get("/request-info/")
async def get_request_info(request: Request):
    return {
        "method": request.method,
        "url": str(request.url),
        "headers": dict(request.headers),
        "query_params": dict(request.query_params),
        "path_params": dict(request.path_params),
        "client": request.client.host if request.client else None,
        "cookies": dict(request.cookies)
    }

@app.post("/inspect-request/")
async def inspect_request(request: Request):
    body = await request.body()
    json_data = await request.json() if request.headers.get("content-type") == "application/json" else None
    
    return {
        "body_size": len(body),
        "content_type": request.headers.get("content-type"),
        "json_data": json_data
    }
```

### Custom Response Objects:

```python
from fastapi.responses import JSONResponse, HTMLResponse, PlainTextResponse, RedirectResponse
from starlette.responses import Response

app = FastAPI()

@app.get("/custom-json/")
async def custom_json():
    content = {"message": "Custom JSON response"}
    return JSONResponse(content=content, status_code=201, headers={"X-Custom": "header"})

@app.get("/html-response/")
async def html_response():
    html_content = """
    <html>
        <head><title>Custom HTML</title></head>
        <body><h1>Hello HTML!</h1></body>
    </html>
    """
    return HTMLResponse(content=html_content)

@app.get("/text-response/")
async def text_response():
    return PlainTextResponse("Hello, plain text!")

@app.get("/redirect/")
async def redirect():
    return RedirectResponse(url="/new-location", status_code=302)

@app.get("/custom-headers/")
async def custom_headers():
    response = JSONResponse({"message": "Success"})
    response.headers["X-Custom-Header"] = "Custom Value"
    response.set_cookie(key="session_id", value="abc123", httponly=True)
    return response
```

### Response Models and Serialization:

```python
from pydantic import BaseModel
from typing import List

class User(BaseModel):
    id: int
    name: str
    email: str

class UserResponse(BaseModel):
    user: User
    message: str

@app.get("/user/{user_id}", response_model=UserResponse)
async def get_user(user_id: int):
    user = User(id=user_id, name="John Doe", email="john@example.com")
    return UserResponse(user=user, message="User retrieved successfully")

# Custom response class
class CustomResponse(Response):
    media_type = "application/custom"
    
    def render(self, content) -> bytes:
        return f"Custom: {content}".encode("utf-8")

@app.get("/custom-response/")
async def custom_response():
    return CustomResponse("Hello Custom Response!")
```

## 24. How can you validate a specific field in a Pydantic model?

Pydantic offers multiple ways to validate individual fields in models.

### Field Validators:

```python
from pydantic import BaseModel, Field, validator, root_validator
from typing import Optional
import re
from datetime import datetime

class User(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    email: str
    age: int = Field(..., ge=0, le=120)
    password: str
    confirm_password: str
    phone: Optional[str] = None
    
    @validator('email')
    def validate_email(cls, v):
        if '@' not in v:
            raise ValueError('Invalid email format')
        return v.lower()
    
    @validator('password')
    def validate_password(cls, v):
        if len(v) < 8:
            raise ValueError('Password must be at least 8 characters')
        if not re.search(r'[A-Z]', v):
            raise ValueError('Password must contain uppercase letter')
        if not re.search(r'[a-z]', v):
            raise ValueError('Password must contain lowercase letter')
        if not re.search(r'\d', v):
            raise ValueError('Password must contain digit')
        return v
    
    @validator('phone')
    def validate_phone(cls, v):
        if v is not None:
            pattern = r'^\+?1?\d{9,15}$'
            if not re.match(pattern, v):
                raise ValueError('Invalid phone number format')
        return v
    
    @root_validator
    def validate_passwords_match(cls, values):
        pw1 = values.get('password')
        pw2 = values.get('confirm_password')
        if pw1 is not None and pw2 is not None and pw1 != pw2:
            raise ValueError('Passwords do not match')
        return values
```

### Custom Field Types:

```python
from pydantic import BaseModel, validator, Field
from typing import Union

class ProductModel(BaseModel):
    name: str
    price: float = Field(..., gt=0)
    category: str
    sku: str
    
    @validator('sku')
    def validate_sku(cls, v):
        if not re.match(r'^[A-Z]{2}\d{4}$', v):
            raise ValueError('SKU must be 2 uppercase letters followed by 4 digits')
        return v
    
    @validator('category')
    def validate_category(cls, v):
        allowed_categories = ['electronics', 'books', 'clothing', 'home']
        if v.lower() not in allowed_categories:
            raise ValueError(f'Category must be one of: {allowed_categories}')
        return v.lower()
    
    @validator('price')
    def validate_price(cls, v):
        # Round to 2 decimal places
        return round(v, 2)

# Usage in FastAPI
@app.post("/products/")
async def create_product(product: ProductModel):
    return {"message": "Product created", "product": product}
```

### Advanced Validation with Context:

```python
from pydantic import BaseModel, validator, ValidationError

class OrderModel(BaseModel):
    product_id: int
    quantity: int = Field(..., gt=0)
    discount_code: Optional[str] = None
    total_amount: float
    
    @validator('discount_code')
    def validate_discount_code(cls, v, values):
        if v is not None:
            # Example: Validate discount code format
            if not re.match(r'^[A-Z]{4}\d{2}$', v):
                raise ValueError('Invalid discount code format')
            
            # You could also check against database here
            valid_codes = ['SAVE10', 'DISC20', 'OFFER30']
            if v not in valid_codes:
                raise ValueError('Invalid discount code')
        return v
    
    @validator('total_amount')
    def validate_total_amount(cls, v, values):
        quantity = values.get('quantity', 0)
        if quantity > 0:
            # Basic validation - could be more complex with product prices
            if v <= 0:
                raise ValueError('Total amount must be positive')
        return v

    class Config:
        # Custom error messages
        error_msg_templates = {
            'value_error.missing': 'This field is required',
            'value_error.number.not_gt': 'Value must be greater than {limit_value}',
        }
```

## 25. What is the purpose of Depends() in FastAPI?

`Depends()` is FastAPI's dependency injection system that allows you to declare dependencies that will be resolved automatically.

### Basic Dependencies:

```python
from fastapi import FastAPI, Depends, HTTPException

app = FastAPI()

# Simple dependency function
def get_current_user_id() -> int:
    # In real app, this would extract from JWT token
    return 123

def get_db():
    # Database connection logic
    db = "database_connection"
    try:
        yield db
    finally:
        # Close database connection
        pass

@app.get("/profile/")
async def get_profile(user_id: int = Depends(get_current_user_id)):
    return {"user_id": user_id, "profile": "user profile data"}

@app.get("/items/")
async def get_items(db = Depends(get_db)):
    # Use database connection
    return {"items": ["item1", "item2"]}
```

### Class-Based Dependencies:

```python
class AuthService:
    def __init__(self, api_key: str = "default-key"):
        self.api_key = api_key
    
    def verify_token(self, token: str) -> bool:
        return token == "valid-token"

class DatabaseService:
    def __init__(self):
        self.connection = "db_connection"
    
    def get_user(self, user_id: int):
        return {"id": user_id, "name": "John Doe"}

def get_auth_service():
    return AuthService(api_key="secret-key")

def get_db_service():
    return DatabaseService()

@app.get("/secure-data/")
async def get_secure_data(
    token: str,
    auth: AuthService = Depends(get_auth_service),
    db: DatabaseService = Depends(get_db_service)
):
    if not auth.verify_token(token):
        raise HTTPException(status_code=401, detail="Invalid token")
    
    user = db.get_user(123)
    return {"user": user, "secure_data": "sensitive information"}
```

### Sub-Dependencies:

```python
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

security = HTTPBearer()

def get_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    return credentials.credentials

def get_current_user(token: str = Depends(get_token)):
    # Validate token and return user
    if token != "valid-token":
        raise HTTPException(status_code=401, detail="Invalid token")
    return {"id": 1, "username": "john_doe"}

def get_admin_user(current_user: dict = Depends(get_current_user)):
    if not current_user.get("is_admin"):
        raise HTTPException(status_code=403, detail="Admin access required")
    return current_user

@app.get("/admin/users/")
async def get_all_users(admin_user: dict = Depends(get_admin_user)):
    return {"message": "Admin access granted", "admin": admin_user}
```

### Dependencies with Parameters:

```python
from functools import partial

def create_rate_limiter(max_requests: int, window_seconds: int):
    def rate_limiter(request: Request):
        # Rate limiting logic here
        client_ip = request.client.host
        # Check if client_ip has exceeded max_requests in window_seconds
        return True  # or raise HTTPException if rate limited
    return rate_limiter

# Create specific rate limiters
strict_rate_limiter = create_rate_limiter(max_requests=10, window_seconds=60)
loose_rate_limiter = create_rate_limiter(max_requests=100, window_seconds=60)

@app.get("/api/strict/")
async def strict_endpoint(request: Request, _: bool = Depends(strict_rate_limiter)):
    return {"message": "Strict rate limiting applied"}

@app.get("/api/loose/")
async def loose_endpoint(request: Request, _: bool = Depends(loose_rate_limiter)):
    return {"message": "Loose rate limiting applied"}
```

## 26. How do you handle global dependencies in FastAPI?

Global dependencies can be applied to entire applications, routers, or groups of endpoints.

### Application-Level Dependencies:

```python
from fastapi import FastAPI, Depends, HTTPException, Request
import time

# Global dependency functions
def log_requests(request: Request):
    start_time = time.time()
    print(f"Request: {request.method} {request.url}")
    return start_time

def verify_api_key(api_key: str = Header(None)):
    if api_key != "secret-api-key":
        raise HTTPException(status_code=401, detail="Invalid API key")
    return api_key

# Apply global dependencies to the entire app
app = FastAPI(dependencies=[Depends(log_requests), Depends(verify_api_key)])

@app.get("/items/")
async def get_items():
    return {"items": ["item1", "item2"]}

@app.get("/users/")
async def get_users():
    return {"users": ["user1", "user2"]}
```

### Router-Level Dependencies:

```python
from fastapi import APIRouter

# Create router with dependencies
admin_router = APIRouter(
    prefix="/admin",
    dependencies=[Depends(get_admin_user), Depends(log_admin_access)]
)

def log_admin_access(current_user: dict = Depends(get_current_user)):
    print(f"Admin access by user: {current_user['username']}")
    return True

@admin_router.get("/dashboard/")
async def admin_dashboard():
    return {"message": "Admin dashboard"}

@admin_router.get("/settings/")
async def admin_settings():
    return {"message": "Admin settings"}

app.include_router(admin_router)
```

### Conditional Global Dependencies:

```python
from contextlib import asynccontextmanager

class GlobalDependencyManager:
    def __init__(self):
        self.maintenance_mode = False
        self.rate_limit_enabled = True
    
    def check_maintenance_mode(self):
        if self.maintenance_mode:
            raise HTTPException(
                status_code=503, 
                detail="Service under maintenance"
            )
        return True
    
    def apply_rate_limiting(self, request: Request):
        if self.rate_limit_enabled:
            # Apply rate limiting logic
            pass
        return True

dependency_manager = GlobalDependencyManager()

@app.middleware("http")
async def global_dependency_middleware(request: Request, call_next):
    # Apply global checks
    try:
        dependency_manager.check_maintenance_mode()
        dependency_manager.apply_rate_limiting(request)
        response = await call_next(request)
        return response
    except HTTPException as e:
        return JSONResponse(
            status_code=e.status_code,
            content={"detail": e.detail}
        )
```

### Scoped Dependencies:

```python
from typing import Generator

class DatabaseConnection:
    def __init__(self):
        self.connection = "active_db_connection"
    
    def close(self):
        print("Database connection closed")

def get_db_connection() -> Generator[DatabaseConnection, None, None]:
    db = DatabaseConnection()
    try:
        yield db
    finally:
        db.close()

# Scoped dependency for specific endpoints
protected_router = APIRouter(
    prefix="/protected",
    dependencies=[Depends(get_current_user)]
)

@protected_router.get("/data/")
async def get_protected_data(db: DatabaseConnection = Depends(get_db_connection)):
    return {"data": "protected data", "db_status": db.connection}

app.include_router(protected_router)
```

## 27. What are asynchronous dependencies, and how can you define them in FastAPI?

Asynchronous dependencies allow for non-blocking I/O operations within the dependency injection system.

### Basic Async Dependencies:

```python
import asyncio
from fastapi import FastAPI, Depends
import httpx

app = FastAPI()

# Async dependency function
async def get_external_data():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://api.example.com/data")
        return response.json()

async def verify_async_token(token: str = Header(None)):
    # Simulate async token verification (e.g., checking with external service)
    await asyncio.sleep(0.1)  # Simulate network delay
    
    if token != "valid-async-token":
        raise HTTPException(status_code=401, detail="Invalid token")
    return {"token": token, "valid": True}

@app.get("/async-data/")
async def get_data_with_async_deps(
    external_data: dict = Depends(get_external_data),
    token_info: dict = Depends(verify_async_token)
):
    return {
        "external_data": external_data,
        "token_info": token_info
    }
```

### Async Database Dependencies:

```python
import asyncpg
from typing import AsyncGenerator

class AsyncDatabase:
    def __init__(self):
        self.pool = None
    
    async def connect(self):
        self.pool = await asyncpg.create_pool(
            "postgresql://user:password@localhost/dbname"
        )
    
    async def disconnect(self):
        if self.pool:
            await self.pool.close()
    
    async def fetch_user(self, user_id: int):
        async with self.pool.acquire() as connection:
            result = await connection.fetchrow(
                "SELECT * FROM users WHERE id = $1", user_id
            )
            return dict(result) if result else None

# Global database instance
database = AsyncDatabase()

async def get_async_db() -> AsyncGenerator[AsyncDatabase, None]:
    if not database.pool:
        await database.connect()
    
    try:
        yield database
    except Exception as e:
        # Handle database errors
        print(f"Database error: {e}")
        raise HTTPException(status_code=500, detail="Database error")

@app.get("/users/{user_id}")
async def get_user(
    user_id: int,
    db: AsyncDatabase = Depends(get_async_db)
):
    user = await db.fetch_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
```

### Async Dependencies with Caching:

```python
import aioredis
from datetime import datetime, timedelta
import json

class AsyncCacheService:
    def __init__(self):
        self.redis = None
    
    async def connect(self):
        self.redis = await aioredis.from_url("redis://localhost")
    
    async def get(self, key: str):
        if not self.redis:
            await self.connect()
        
        value = await self.redis.get(key)
        return json.loads(value) if value else None
    
    async def set(self, key: str, value: dict, expire: int = 300):
        if not self.redis:
            await self.connect()
        
        await self.redis.setex(key, expire, json.dumps(value))

cache_service = AsyncCacheService()

async def get_cached_user_data(user_id: int = Path(...)):
    cache_key = f"user:{user_id}"
    
    # Try to get from cache first
    cached_data = await cache_service.get(cache_key)
    if cached_data:
        return cached_data
    
    # If not in cache, fetch from database (simulated)
    await asyncio.sleep(0.5)  # Simulate database query
    user_data = {
        "id": user_id,
        "name": f"User {user_id}",
        "fetched_at": datetime.now().isoformat()
    }
    
    # Cache the result
    await cache_service.set(cache_key, user_data)
    return user_data

@app.get("/cached-users/{user_id}")
async def get_cached_user(user_data: dict = Depends(get_cached_user_data)):
    return user_data
```

### Async Dependencies with Background Tasks:

```python
from fastapi import BackgroundTasks
import asyncio

async def log_user_activity(user_id: int, action: str):
    # Simulate async logging
    await asyncio.sleep(0.1)
    print(f"User {user_id} performed action: {action}")

async def send_notification(user_id: int, message: str):
    # Simulate async notification sending
    await asyncio.sleep(0.2)
    print(f"Notification sent to user {user_id}: {message}")

async def get_user_with_logging(
    user_id: int = Path(...),
    background_tasks: BackgroundTasks = BackgroundTasks(),
    current_user: dict = Depends(get_current_user)
):
    # Add background tasks
    background_tasks.add_task(log_user_activity, current_user["id"], "viewed_profile")
    background_tasks.add_task(send_notification, user_id, "Profile was viewed")
    
    return {"user_id": user_id, "viewer": current_user["id"]}

@app.get("/users/{user_id}/profile")
async def get_user_profile(user_data: dict = Depends(get_user_with_logging)):
    return user_data
```

## 28. How can you handle rate limiting in FastAPI?

Rate limiting helps protect your API from abuse and ensures fair usage among clients.

### Basic Rate Limiting with Redis:

```python
import aioredis
import time
from fastapi import FastAPI, Request, HTTPException, Depends
from typing import Optional

app = FastAPI()

class RateLimiter:
    def __init__(self, redis_url: str = "redis://localhost"):
        self.redis_url = redis_url
        self.redis = None
    
    async def init_redis(self):
        if not self.redis:
            self.redis = await aioredis.from_url(self.redis_url)
    
    async def is_allowed(
        self, 
        key: str, 
        limit: int, 
        window: int
    ) -> tuple[bool, dict]:
        await self.init_redis()
        
        current_time = int(time.time())
        window_start = current_time - window
        
        # Use Redis sorted set to track requests
        pipe = self.redis.pipeline()
        
        # Remove old entries
        pipe.zremrangebyscore(key, 0, window_start)
        
        # Count current requests
        pipe.zcard(key)
        
        # Add current request
        pipe.zadd(key, {str(current_time): current_time})
        
        # Set expiry
        pipe.expire(key, window)
        
        results = await pipe.execute()
        current_requests = results[1]
        
        remaining = max(0, limit - current_requests)
        reset_time = current_time + window
        
        return current_requests < limit, {
            "limit": limit,
            "remaining": remaining,
            "reset": reset_time,
            "current": current_requests
        }

rate_limiter = RateLimiter()

async def apply_rate_limit(
    request: Request,
    limit: int = 100,
    window: int = 3600  # 1 hour
):
    client_ip = request.client.host
    key = f"rate_limit:{client_ip}"
    
    allowed, info = await rate_limiter.is_allowed(key, limit, window)
    
    if not allowed:
        raise HTTPException(
            status_code=429,
            detail="Rate limit exceeded",
            headers={
                "X-RateLimit-Limit": str(info["limit"]),
                "X-RateLimit-Remaining": str(info["remaining"]),
                "X-RateLimit-Reset": str(info["reset"])
            }
        )
    
    return info

@app.get("/api/data")
async def get_data(
    request: Request,
    rate_info: dict = Depends(lambda r: apply_rate_limit(r, limit=10, window=60))
):
    return {
        "data": "some data",
        "rate_limit_info": rate_info
    }
```

### Advanced Rate Limiting with Different Tiers:

```python
from enum import Enum
from functools import wraps

class UserTier(str, Enum):
    FREE = "free"
    PREMIUM = "premium"
    ENTERPRISE = "enterprise"

class TieredRateLimiter:
    TIER_LIMITS = {
        UserTier.FREE: {"requests": 100, "window": 3600},
        UserTier.PREMIUM: {"requests": 1000, "window": 3600},
        UserTier.ENTERPRISE: {"requests": 10000, "window": 3600}
    }
    
    def __init__(self):
        self.rate_limiter = RateLimiter()
    
    async def check_user_limit(
        self, 
        user_id: str, 
        tier: UserTier
    ) -> tuple[bool, dict]:
        limits = self.TIER_LIMITS[tier]
        key = f"user_rate_limit:{user_id}"
        
        return await self.rate_limiter.is_allowed(
            key, 
            limits["requests"], 
            limits["window"]
        )

tiered_limiter = TieredRateLimiter()

async def get_user_tier(user_id: int = Depends(get_current_user_id)) -> UserTier:
    # In real app, fetch from database
    user_tiers = {
        1: UserTier.FREE,
        2: UserTier.PREMIUM,
        3: UserTier.ENTERPRISE
    }
    return user_tiers.get(user_id, UserTier.FREE)

async def apply_tiered_rate_limit(
    user_id: int = Depends(get_current_user_id),
    user_tier: UserTier = Depends(get_user_tier)
):
    allowed, info = await tiered_limiter.check_user_limit(str(user_id), user_tier)
    
    if not allowed:
        raise HTTPException(
            status_code=429,
            detail=f"Rate limit exceeded for {user_tier} tier",
            headers={
                "X-RateLimit-Limit": str(info["limit"]),
                "X-RateLimit-Remaining": str(info["remaining"]),
                "X-RateLimit-Reset": str(info["reset"]),
                "X-RateLimit-Tier": user_tier
            }
        )
    
    return info

@app.get("/api/premium-data")
async def get_premium_data(
    rate_info: dict = Depends(apply_tiered_rate_limit)
):
    return {
        "premium_data": "exclusive content",
        "rate_limit_info": rate_info
    }
```

### Rate Limiting Middleware:

```python
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse

class RateLimitMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, rate_limiter: RateLimiter):
        super().__init__(app)
        self.rate_limiter = rate_limiter
    
    async def dispatch(self, request, call_next):
        # Skip rate limiting for certain paths
        if request.url.path in ["/health", "/docs", "/openapi.json"]:
            return await call_next(request)
        
        client_ip = request.client.host
        key = f"global_rate_limit:{client_ip}"
        
        allowed, info = await self.rate_limiter.is_allowed(key, 1000, 3600)
        
        if not allowed:
            return JSONResponse(
                status_code=429,
                content={"detail": "Global rate limit exceeded"},
                headers={
                    "X-RateLimit-Limit": str(info["limit"]),
                    "X-RateLimit-Remaining": str(info["remaining"]),
                    "X-RateLimit-Reset": str(info["reset"])
                }
            )
        
        response = await call_next(request)
        
        # Add rate limit headers to response
        response.headers["X-RateLimit-Limit"] = str(info["limit"])
        response.headers["X-RateLimit-Remaining"] = str(info["remaining"])
        response.headers["X-RateLimit-Reset"] = str(info["reset"])
        
        return response

# Add middleware to app
app.add_middleware(RateLimitMiddleware, rate_limiter=rate_limiter)
```

## 29. How do you manage database connections in FastAPI?

Proper database connection management is crucial for performance and reliability.

### SQLAlchemy with Dependency Injection:

```python
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from fastapi import Depends

# Database setup
DATABASE_URL = "postgresql://user:password@localhost/dbname"

engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Database models
class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)

# Dependency to get database session
def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Usage in endpoints
@app.get("/users/{user_id}")
async def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
```

### Async Database with AsyncPG:

```python
import asyncpg
from contextlib import asynccontextmanager
from typing import AsyncGenerator

class AsyncDatabaseManager:
    def __init__(self, database_url: str):
        self.database_url = database_url
        self.pool: Optional[asyncpg.Pool] = None
    
    async def create_pool(self):
        self.pool = await asyncpg.create_pool(
            self.database_url,
            min_size=10,
            max_size=20,
            command_timeout=60,
            server_settings={
                'jit': 'off'
            }
        )
    
    async def close_pool(self):
        if self.pool:
            await self.pool.close()
    
    @asynccontextmanager
    async def get_connection(self):
        if not self.pool:
            await self.create_pool()
        
        async with self.pool.acquire() as connection:
            try:
                yield connection
            except Exception as e:
                # Log error and re-raise
                print(f"Database error: {e}")
                raise

# Global database manager
db_manager = AsyncDatabaseManager("postgresql://user:password@localhost/dbname")

# Dependency for database connection
async def get_async_db() -> AsyncGenerator[asyncpg.Connection, None]:
    async with db_manager.get_connection() as connection:
        yield connection

@app.get("/async-users/{user_id}")
async def get_async_user(
    user_id: int, 
    db: asyncpg.Connection = Depends(get_async_db)
):
    query = "SELECT id, name, email FROM users WHERE id = $1"
    user = await db.fetchrow(query, user_id)
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return dict(user)
```

### Database Connection with Health Checks:

```python
from sqlalchemy import text
import logging

logger = logging.getLogger(__name__)

class DatabaseHealthCheck:
    def __init__(self, db_session: Session):
        self.db_session = db_session
    
    async def check_connection(self) -> bool:
        try:
            # Simple query to test connection
            result = self.db_session.execute(text("SELECT 1"))
            return result.scalar() == 1
        except Exception as e:
            logger.error(f"Database health check failed: {e}")
            return False

def get_db_with_health_check() -> Session:
    db = SessionLocal()
    try:
        # Test connection before yielding
        health_check = DatabaseHealthCheck(db)
        if not health_check.check_connection():
            raise HTTPException(
                status_code=503, 
                detail="Database unavailable"
            )
        yield db
    except Exception as e:
        db.rollback()
        raise
    finally:
        db.close()

@app.get("/health/database")
async def database_health(db: Session = Depends(get_db_with_health_check)):
    return {"status": "healthy", "database": "connected"}
```

### Database Transaction Management:

```python
from contextlib import contextmanager
from sqlalchemy.orm import Session

@contextmanager
def db_transaction(db: Session):
    try:
        yield db
        db.commit()
    except Exception as e:
        db.rollback()
        logger.error(f"Database transaction failed: {e}")
        raise
    finally:
        db.close()

async def create_user_with_transaction(
    user_data: dict,
    db: Session = Depends(get_db)
):
    with db_transaction(db) as transaction_db:
        # Multiple database operations in a transaction
        user = User(**user_data)
        transaction_db.add(user)
        transaction_db.flush()  # Get the ID without committing
        
        # Additional operations
        user_profile = UserProfile(user_id=user.id, bio="Default bio")
        transaction_db.add(user_profile)
        
        # Transaction will be committed automatically
        return {"user_id": user.id, "message": "User created successfully"}
```

## 30. How can you implement JWT-based authentication in FastAPI?

JWT (JSON Web Tokens) provide a stateless way to handle authentication in FastAPI applications.

### Basic JWT Implementation:

```python
from datetime import datetime, timedelta
from typing import Optional
from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

# Configuration
SECRET_KEY = "your-secret-key-here"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
security = HTTPBearer()

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        
        # Check token expiration
        exp = payload.get("exp")
        if exp is None or datetime.utcnow() > datetime.fromtimestamp(exp):
            raise credentials_exception
            
    except JWTError:
        raise credentials_exception
    
    return payload

# Authentication endpoints
@app.post("/login")
async def login(username: str = Form(...), password: str = Form(...)):
    # Verify user credentials (check against database)
    user = authenticate_user(username, password)  # Your implementation
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password"
        )
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username, "user_id": user.id},
        expires_delta=access_token_expires
    )
    
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "expires_in": ACCESS_TOKEN_EXPIRE_MINUTES * 60
    }

# Protected endpoint
@app.get("/protected")
async def protected_route(token_data: dict = Depends(verify_token)):
    return {
        "message": "This is a protected route",
        "user": token_data.get("sub"),
        "user_id": token_data.get("user_id")
    }
```

### Advanced JWT with Refresh Tokens:

```python
import uuid
from enum import Enum

class TokenType(str, Enum):
    ACCESS = "access"
    REFRESH = "refresh"

# Token storage (in production, use Redis or database)
refresh_tokens = set()

def create_tokens(user_data: dict):
    # Create access token (short-lived)
    access_token_expires = timedelta(minutes=15)
    access_token = create_access_token(
        data={**user_data, "token_type": TokenType.ACCESS},
        expires_delta=access_token_expires
    )
    
    # Create refresh token (long-lived)
    refresh_token_expires = timedelta(days=7)
    refresh_token_data = {
        **user_data,
        "token_type": TokenType.REFRESH,
        "jti": str(uuid.uuid4())  # Unique token ID
    }
    refresh_token = create_access_token(
        data=refresh_token_data,
        expires_delta=refresh_token_expires
    )
    
    # Store refresh token
    refresh_tokens.add(refresh_token_data["jti"])
    
    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer",
        "expires_in": 15 * 60
    }

def verify_refresh_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        
        # Verify it's a refresh token
        if payload.get("token_type") != TokenType.REFRESH:
            raise HTTPException(status_code=401, detail="Invalid token type")
        
        # Check if token is still valid (not revoked)
        jti = payload.get("jti")
        if jti not in refresh_tokens:
            raise HTTPException(status_code=401, detail="Token revoked")
        
        return payload
        
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid refresh token")

@app.post("/login")
async def enhanced_login(username: str = Form(...), password: str = Form(...)):
    user = authenticate_user(username, password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    tokens = create_tokens({"sub": user.username, "user_id": user.id})
    return tokens

@app.post("/refresh")
async def refresh_access_token(refresh_token: str = Form(...)):
    payload = verify_refresh_token(refresh_token)
    
    # Create new access token
    new_access_token = create_access_token(
        data={
            "sub": payload.get("sub"),
            "user_id": payload.get("user_id"),
            "token_type": TokenType.ACCESS
        },
        expires_delta=timedelta(minutes=15)
    )
    
    return {
        "access_token": new_access_token,
        "token_type": "bearer",
        "expires_in": 15 * 60
    }

@app.post("/logout")
async def logout(refresh_token: str = Form(...)):
    payload = verify_refresh_token(refresh_token)
    
    # Revoke refresh token
    jti = payload.get("jti")
    refresh_tokens.discard(jti)
    
    return {"message": "Successfully logged out"}
```

### Role-Based Access Control with JWT:

```python
from functools import wraps
from typing import List

class UserRole(str, Enum):
    USER = "user"
    ADMIN = "admin"
    MODERATOR = "moderator"

def create_access_token_with_roles(user_data: dict, roles: List[UserRole]):
    token_data = {
        **user_data,
        "roles": [role.value for role in roles],
        "token_type": TokenType.ACCESS
    }
    return create_access_token(token_data, timedelta(minutes=15))

def require_roles(required_roles: List[UserRole]):
    def role_checker(token_data: dict = Depends(verify_token)):
        user_roles = token_data.get("roles", [])
        
        if not any(role.value in user_roles for role in required_roles):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Insufficient permissions"
            )
        
        return token_data
    
    return role_checker

def require_admin(token_data: dict = Depends(verify_token)):
    if UserRole.ADMIN.value not in token_data.get("roles", []):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin access required"
        )
    return token_data

# Protected endpoints with role requirements
@app.get("/admin/users")
async def get_all_users(token_data: dict = Depends(require_admin)):
    return {"users": ["user1", "user2"], "admin": token_data.get("sub")}

@app.get("/moderator/reports")
async def get_reports(
    token_data: dict = Depends(require_roles([UserRole.ADMIN, UserRole.MODERATOR]))
):
    return {"reports": ["report1", "report2"], "user": token_data.get("sub")}
```

# FastAPI Advanced Topics Guide (Questions 50-59)

## Question 50: How do you mock external dependencies in FastAPI tests using TestClient?

FastAPI provides excellent dependency injection that makes mocking external dependencies straightforward using dependency overrides.

### Basic Dependency Override Pattern

```python
# app.py
from fastapi import FastAPI, Depends
import httpx

app = FastAPI()

# External service dependency
async def get_external_api_client():
    async with httpx.AsyncClient() as client:
        yield client

@app.get("/users/{user_id}")
async def get_user(user_id: int, client: httpx.AsyncClient = Depends(get_external_api_client)):
    response = await client.get(f"https://api.example.com/users/{user_id}")
    return response.json()
```

```python
# test_app.py
import pytest
from fastapi.testclient import TestClient
from unittest.mock import AsyncMock, MagicMock
from app import app, get_external_api_client

@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture
def mock_external_client():
    mock_client = AsyncMock()
    mock_response = MagicMock()
    mock_response.json.return_value = {"id": 1, "name": "John Doe"}
    mock_client.get.return_value = mock_response
    return mock_client

def test_get_user_success(client, mock_external_client):
    # Override the dependency
    app.dependency_overrides[get_external_api_client] = lambda: mock_external_client
    
    response = client.get("/users/1")
    
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "John Doe"}
    mock_external_client.get.assert_called_once_with("https://api.example.com/users/1")
    
    # Clean up
    app.dependency_overrides.clear()
```

### Database Dependency Mocking

```python
# database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

SQLALCHEMY_DATABASE_URL = "postgresql://user:pass@localhost/dbname"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

```python
# test_database.py
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient
from app import app
from database import get_db

# Use in-memory SQLite for testing
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

@pytest.fixture
def client():
    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as c:
        yield c
    app.dependency_overrides.clear()
```

### Complex Service Mocking with Context Managers

```python
# services.py
class EmailService:
    async def send_email(self, to: str, subject: str, body: str):
        # External email service logic
        pass

class PaymentService:
    async def process_payment(self, amount: float, token: str):
        # External payment processing
        pass

async def get_email_service():
    return EmailService()

async def get_payment_service():
    return PaymentService()
```

```python
# test_services.py
from unittest.mock import AsyncMock
import pytest

@pytest.fixture
def mock_services():
    mock_email = AsyncMock(spec=EmailService)
    mock_payment = AsyncMock(spec=PaymentService)
    
    app.dependency_overrides[get_email_service] = lambda: mock_email
    app.dependency_overrides[get_payment_service] = lambda: mock_payment
    
    yield {"email": mock_email, "payment": mock_payment}
    
    app.dependency_overrides.clear()

def test_order_creation(client, mock_services):
    mock_services["payment"].process_payment.return_value = {"status": "success"}
    mock_services["email"].send_email.return_value = None
    
    response = client.post("/orders", json={"amount": 100.0, "email": "test@example.com"})
    
    assert response.status_code == 201
    mock_services["payment"].process_payment.assert_called_once()
    mock_services["email"].send_email.assert_called_once()
```

## Question 51: What deployment strategies do you recommend for production FastAPI apps?

### Uvicorn + Gunicorn + Nginx Architecture

This is the most common and recommended production setup for FastAPI applications.

#### 1. Application Structure

```python
# main.py
from fastapi import FastAPI
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    print("Starting up...")
    yield
    # Shutdown
    print("Shutting down...")

app = FastAPI(lifespan=lifespan)

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

#### 2. Gunicorn Configuration

```python
# gunicorn.conf.py
import multiprocessing

# Server socket
bind = "0.0.0.0:8000"
backlog = 2048

# Worker processes
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = "uvicorn.workers.UvicornWorker"
worker_connections = 1000
max_requests = 1000
max_requests_jitter = 50
preload_app = True

# Timeout
timeout = 30
keepalive = 2

# Logging
accesslog = "-"
errorlog = "-"
loglevel = "info"
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s" %(D)s'

# Process naming
proc_name = 'fastapi_app'

# Security
limit_request_line = 4094
limit_request_fields = 100
limit_request_field_size = 8190
```

#### 3. Nginx Configuration

```nginx
# /etc/nginx/sites-available/fastapi_app
upstream fastapi_backend {
    server 127.0.0.1:8000;
    # Add more servers for load balancing
    # server 127.0.0.1:8001;
    # server 127.0.0.1:8002;
}

server {
    listen 80;
    server_name your-domain.com;
    
    # Redirect HTTP to HTTPS
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl http2;
    server_name your-domain.com;
    
    # SSL Configuration
    ssl_certificate /path/to/ssl/cert.pem;
    ssl_certificate_key /path/to/ssl/private.key;
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers ECDHE-RSA-AES256-GCM-SHA512:DHE-RSA-AES256-GCM-SHA512;
    ssl_prefer_server_ciphers off;
    
    # Security headers
    add_header X-Content-Type-Options nosniff;
    add_header X-Frame-Options DENY;
    add_header X-XSS-Protection "1; mode=block";
    add_header Strict-Transport-Security "max-age=63072000; includeSubDomains; preload";
    
    # Gzip compression
    gzip on;
    gzip_vary on;
    gzip_min_length 1000;
    gzip_types application/json application/javascript text/css text/javascript;
    
    # Rate limiting
    limit_req_zone $binary_remote_addr zone=api:10m rate=10r/s;
    
    location / {
        limit_req zone=api burst=20 nodelay;
        
        proxy_pass http://fastapi_backend;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        
        # Timeouts
        proxy_connect_timeout 30s;
        proxy_send_timeout 30s;
        proxy_read_timeout 30s;
        
        # WebSocket support
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
    }
    
    # Static files (if any)
    location /static/ {
        alias /path/to/static/files/;
        expires 1y;
        add_header Cache-Control "public, immutable";
    }
    
    # Health check endpoint
    location /health {
        access_log off;
        proxy_pass http://fastapi_backend;
    }
}
```

#### 4. Docker Production Setup

```dockerfile
# Dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY . .

# Create non-root user
RUN useradd --create-home --shell /bin/bash app
RUN chown -R app:app /app
USER app

# Expose port
EXPOSE 8000

# Run application
CMD ["gunicorn", "-c", "gunicorn.conf.py", "main:app"]
```

```yaml
# docker-compose.prod.yml
version: '3.8'

services:
  fastapi:
    build: .
    restart: unless-stopped
    environment:
      - DATABASE_URL=postgresql://user:pass@db:5432/dbname
      - REDIS_URL=redis://redis:6379
    depends_on:
      - db
      - redis
    networks:
      - app-network

  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf
      - ./ssl:/etc/ssl
    depends_on:
      - fastapi
    restart: unless-stopped
    networks:
      - app-network

  db:
    image: postgres:15
    environment:
      - POSTGRES_DB=dbname
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=pass
    volumes:
      - postgres_data:/var/lib/postgresql/data
    restart: unless-stopped
    networks:
      - app-network

  redis:
    image: redis:alpine
    restart: unless-stopped
    networks:
      - app-network

volumes:
  postgres_data:

networks:
  app-network:
    driver: bridge
```

#### 5. Systemd Service (Alternative to Docker)

```ini
# /etc/systemd/system/fastapi.service
[Unit]
Description=FastAPI application
After=network.target

[Service]
Type=exec
User=www-data
Group=www-data
WorkingDirectory=/opt/fastapi-app
Environment=PATH=/opt/fastapi-app/venv/bin
ExecStart=/opt/fastapi-app/venv/bin/gunicorn -c gunicorn.conf.py main:app
ExecReload=/bin/kill -s HUP $MAINPID
Restart=on-failure
RestartSec=5s

[Install]
WantedBy=multi-user.target
```

## Question 52: How do you enable logging and monitor FastAPI APIs in production?

### Comprehensive Logging Setup

#### 1. Structured Logging Configuration

```python
# logging_config.py
import logging
import logging.config
import json
from datetime import datetime
from typing import Any, Dict

class JSONFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        log_entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
            "module": record.module,
            "function": record.funcName,
            "line": record.lineno,
        }
        
        if record.exc_info:
            log_entry["exception"] = self.formatException(record.exc_info)
        
        # Add extra fields
        if hasattr(record, 'request_id'):
            log_entry["request_id"] = record.request_id
        if hasattr(record, 'user_id'):
            log_entry["user_id"] = record.user_id
        if hasattr(record, 'duration'):
            log_entry["duration"] = record.duration
            
        return json.dumps(log_entry)

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "json": {
            "()": JSONFormatter,
        },
        "standard": {
            "format": "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
        },
    },
    "handlers": {
        "console": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "formatter": "json",
        },
        "file": {
            "level": "INFO",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": "app.log",
            "maxBytes": 10485760,  # 10MB
            "backupCount": 5,
            "formatter": "json",
        },
    },
    "loggers": {
        "": {  # root logger
            "handlers": ["console", "file"],
            "level": "INFO",
            "propagate": False,
        },
        "uvicorn": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": False,
        },
        "sqlalchemy.engine": {
            "handlers": ["file"],
            "level": "WARNING",
            "propagate": False,
        },
    },
}

def setup_logging():
    logging.config.dictConfig(LOGGING_CONFIG)
```

#### 2. Request/Response Logging Middleware

```python
# middleware.py
import logging
import time
import uuid
from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.types import ASGIApp

logger = logging.getLogger(__name__)

class LoggingMiddleware(BaseHTTPMiddleware):
    def __init__(self, app: ASGIApp):
        super().__init__(app)

    async def dispatch(self, request: Request, call_next):
        # Generate request ID
        request_id = str(uuid.uuid4())
        
        # Add request ID to request state
        request.state.request_id = request_id
        
        # Log request
        start_time = time.time()
        logger.info(
            "Request started",
            extra={
                "request_id": request_id,
                "method": request.method,
                "url": str(request.url),
                "user_agent": request.headers.get("user-agent"),
                "client_ip": request.client.host,
            }
        )
        
        # Process request
        try:
            response = await call_next(request)
            duration = time.time() - start_time
            
            # Log response
            logger.info(
                "Request completed",
                extra={
                    "request_id": request_id,
                    "status_code": response.status_code,
                    "duration": round(duration, 4),
                }
            )
            
            # Add request ID to response headers
            response.headers["X-Request-ID"] = request_id
            return response
            
        except Exception as e:
            duration = time.time() - start_time
            logger.error(
                "Request failed",
                extra={
                    "request_id": request_id,
                    "duration": round(duration, 4),
                    "error": str(e),
                },
                exc_info=True
            )
            raise
```

#### 3. Application with Logging

```python
# main.py
import logging
from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import JSONResponse
from logging_config import setup_logging
from middleware import LoggingMiddleware

# Setup logging
setup_logging()
logger = logging.getLogger(__name__)

app = FastAPI(title="FastAPI with Logging")

# Add logging middleware
app.add_middleware(LoggingMiddleware)

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    logger.error(
        "HTTP exception occurred",
        extra={
            "request_id": getattr(request.state, "request_id", None),
            "status_code": exc.status_code,
            "detail": exc.detail,
        }
    )
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail}
    )

@app.exception_handler(Exception)
async def general_exception_handler(request, exc):
    logger.error(
        "Unhandled exception occurred",
        extra={
            "request_id": getattr(request.state, "request_id", None),
        },
        exc_info=True
    )
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal server error"}
    )

@app.get("/")
async def root():
    logger.info("Root endpoint accessed")
    return {"message": "Hello World"}

@app.get("/error")
async def trigger_error():
    logger.warning("Error endpoint accessed")
    raise HTTPException(status_code=400, "This is a test error")
```

### Production Monitoring Setup

#### 1. Prometheus Metrics

```python
# metrics.py
from prometheus_client import Counter, Histogram, Gauge, generate_latest
from fastapi import FastAPI, Response
import time
import psutil

# Metrics
REQUEST_COUNT = Counter(
    'fastapi_requests_total',
    'Total number of requests',
    ['method', 'endpoint', 'status_code']
)

REQUEST_DURATION = Histogram(
    'fastapi_request_duration_seconds',
    'Request duration in seconds',
    ['method', 'endpoint']
)

ACTIVE_REQUESTS = Gauge(
    'fastapi_active_requests',
    'Number of active requests'
)

SYSTEM_METRICS = {
    'cpu_usage': Gauge('system_cpu_usage_percent', 'CPU usage percentage'),
    'memory_usage': Gauge('system_memory_usage_percent', 'Memory usage percentage'),
    'disk_usage': Gauge('system_disk_usage_percent', 'Disk usage percentage'),
}

class MetricsMiddleware:
    def __init__(self, app: FastAPI):
        self.app = app

    async def __call__(self, scope, receive, send):
        if scope["type"] != "http":
            await self.app(scope, receive, send)
            return

        request = scope
        method = request["method"]
        path = request["path"]
        
        ACTIVE_REQUESTS.inc()
        start_time = time.time()
        
        try:
            await self.app(scope, receive, send)
        finally:
            ACTIVE_REQUESTS.dec()
            duration = time.time() - start_time
            
            # Record metrics (you'd need to extract status code from response)
            REQUEST_DURATION.labels(method=method, endpoint=path).observe(duration)

def update_system_metrics():
    """Update system metrics"""
    SYSTEM_METRICS['cpu_usage'].set(psutil.cpu_percent())
    SYSTEM_METRICS['memory_usage'].set(psutil.virtual_memory().percent)
    SYSTEM_METRICS['disk_usage'].set(psutil.disk_usage('/').percent)

@app.get("/metrics")
async def metrics():
    update_system_metrics()
    return Response(
        content=generate_latest(),
        media_type="text/plain"
    )
```

#### 2. Health Check Endpoints

```python
# health.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
import redis
import httpx
from typing import Dict, Any

router = APIRouter()

async def check_database(db: Session = Depends(get_db)) -> Dict[str, Any]:
    try:
        db.execute("SELECT 1")
        return {"status": "healthy", "response_time": 0.001}
    except Exception as e:
        return {"status": "unhealthy", "error": str(e)}

async def check_redis() -> Dict[str, Any]:
    try:
        r = redis.Redis(host='localhost', port=6379, db=0)
        r.ping()
        return {"status": "healthy"}
    except Exception as e:
        return {"status": "unhealthy", "error": str(e)}

async def check_external_service() -> Dict[str, Any]:
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get("https://httpbin.org/status/200", timeout=5.0)
            if response.status_code == 200:
                return {"status": "healthy"}
            else:
                return {"status": "unhealthy", "status_code": response.status_code}
    except Exception as e:
        return {"status": "unhealthy", "error": str(e)}

@router.get("/health")
async def health_check():
    return {"status": "healthy", "timestamp": time.time()}

@router.get("/health/detailed")
async def detailed_health_check(db: Session = Depends(get_db)):
    checks = {
        "database": await check_database(db),
        "redis": await check_redis(),
        "external_service": await check_external_service(),
    }
    
    overall_status = "healthy" if all(
        check["status"] == "healthy" for check in checks.values()
    ) else "unhealthy"
    
    return {
        "status": overall_status,
        "timestamp": time.time(),
        "checks": checks
    }
```

#### 3. APM Integration (Example with Elastic APM)

```python
# apm_config.py
from elasticapm.contrib.starlette import make_apm_client, ElasticAPM

apm_config = {
    'SERVICE_NAME': 'fastapi-app',
    'SECRET_TOKEN': 'your-secret-token',
    'SERVER_URL': 'http://localhost:8200',
    'ENVIRONMENT': 'production',
    'DEBUG': False,
}

apm = make_apm_client(apm_config)

# Add to main.py
app.add_middleware(ElasticAPM, client=apm)
```

## Question 53: How do you manage environment-based settings using dotenv and Pydantic Settings?

### Pydantic Settings Management

#### 1. Complete Settings Configuration

```python
# settings.py
from pydantic import BaseSettings, validator, Field
from typing import Optional, List
from enum import Enum
import os

class Environment(str, Enum):
    DEVELOPMENT = "development"
    TESTING = "testing"
    STAGING = "staging"
    PRODUCTION = "production"

class DatabaseSettings(BaseSettings):
    host: str = Field(..., env="DB_HOST")
    port: int = Field(5432, env="DB_PORT")
    username: str = Field(..., env="DB_USERNAME")
    password: str = Field(..., env="DB_PASSWORD")
    database: str = Field(..., env="DB_DATABASE")
    
    @property
    def url(self) -> str:
        return f"postgresql://{self.username}:{self.password}@{self.host}:{self.port}/{self.database}"
    
    @property
    def async_url(self) -> str:
        return f"postgresql+asyncpg://{self.username}:{self.password}@{self.host}:{self.port}/{self.database}"

class RedisSettings(BaseSettings):
    host: str = Field("localhost", env="REDIS_HOST")
    port: int = Field(6379, env="REDIS_PORT")
    password: Optional[str] = Field(None, env="REDIS_PASSWORD")
    db: int = Field(0, env="REDIS_DB")
    
    @property
    def url(self) -> str:
        if self.password:
            return f"redis://:{self.password}@{self.host}:{self.port}/{self.db}"
        return f"redis://{self.host}:{self.port}/{self.db}"

class JWTSettings(BaseSettings):
    secret_key: str = Field(..., env="JWT_SECRET_KEY")
    algorithm: str = Field("HS256", env="JWT_ALGORITHM")
    access_token_expire_minutes: int = Field(30, env="JWT_ACCESS_TOKEN_EXPIRE_MINUTES")
    refresh_token_expire_days: int = Field(7, env="JWT_REFRESH_TOKEN_EXPIRE_DAYS")
    
    @validator("secret_key")
    def validate_secret_key(cls, v):
        if len(v) < 32:
            raise ValueError("JWT secret key must be at least 32 characters long")
        return v

class EmailSettings(BaseSettings):
    smtp_server: str = Field(..., env="SMTP_SERVER")
    smtp_port: int = Field(587, env="SMTP_PORT")
    smtp_username: str = Field(..., env="SMTP_USERNAME")
    smtp_password: str = Field(..., env="SMTP_PASSWORD")
    from_email: str = Field(..., env="FROM_EMAIL")
    use_tls: bool = Field(True, env="SMTP_USE_TLS")

class Settings(BaseSettings):
    # Application settings
    app_name: str = Field("FastAPI App", env="APP_NAME")
    app_version: str = Field("1.0.0", env="APP_VERSION")
    environment: Environment = Field(Environment.DEVELOPMENT, env="ENVIRONMENT")
    debug: bool = Field(False, env="DEBUG")
    
    # Server settings
    host: str = Field("127.0.0.1", env="HOST")
    port: int = Field(8000, env="PORT")
    workers: int = Field(1, env="WORKERS")
    
    # Security settings
    allowed_hosts: List[str] = Field(["*"], env="ALLOWED_HOSTS")
    cors_origins: List[str] = Field(["*"], env="CORS_ORIGINS")
    
    # Nested settings
    database: DatabaseSettings = DatabaseSettings()
    redis: RedisSettings = RedisSettings()
    jwt: JWTSettings = JWTSettings()
    email: EmailSettings = EmailSettings()
    
    # API settings
    api_v1_prefix: str = Field("/api/v1", env="API_V1_PREFIX")
    docs_url: Optional[str] = Field("/docs", env="DOCS_URL")
    redoc_url: Optional[str] = Field("/redoc", env="REDOC_URL")
    
    # External services
    external_api_url: str = Field(..., env="EXTERNAL_API_URL")
    external_api_key: str = Field(..., env="EXTERNAL_API_KEY")
    
    # File storage
    upload_dir: str = Field("uploads", env="UPLOAD_DIR")
    max_file_size: int = Field(10485760, env="MAX_FILE_SIZE")  # 10MB
    
    # Logging
    log_level: str = Field("INFO", env="LOG_LEVEL")
    log_file: Optional[str] = Field(None, env="LOG_FILE")
    
    @validator("environment", pre=True)
    def validate_environment(cls, v):
        if isinstance(v, str):
            return Environment(v.lower())
        return v
    
    @validator("allowed_hosts", "cors_origins", pre=True)
    def validate_list_fields(cls, v):
        if isinstance(v, str):
            return [item.strip() for item in v.split(",")]
        return v
    
    @validator("docs_url", "redoc_url")
    def validate_docs_urls(cls, v, values):
        environment = values.get("environment")
        if environment == Environment.PRODUCTION and v is not None:
            return None  # Disable docs in production
        return v
    
    @property
    def is_development(self) -> bool:
        return self.environment == Environment.DEVELOPMENT
    
    @property
    def is_production(self) -> bool:
        return self.environment == Environment.PRODUCTION
    
    @property
    def is_testing(self) -> bool:
        return self.environment == Environment.TESTING
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False
        # Support for nested env vars
        env_nested_delimiter = "__"

# Global settings instance
settings = Settings()
```

#### 2. Environment-Specific Configuration Files

```bash
# .env.development
ENVIRONMENT=development
DEBUG=true
DB_HOST=localhost
DB_USERNAME=dev_user
DB_PASSWORD=dev_password
DB_DATABASE=dev_db
JWT_SECRET_KEY=your-super-secret-development-key-here
DOCS_URL=/docs
REDOC_URL=/redoc
LOG_LEVEL=DEBUG
```

```bash
# .env.production
ENVIRONMENT=production
DEBUG=false
DB_HOST=prod-db-server
DB_USERNAME=prod_user
DB_PASSWORD=secure_prod_password
DB_DATABASE=prod_db
JWT_SECRET_KEY=your-super-secure-production-key-32chars
DOCS_URL=null
REDOC_URL=null
LOG_LEVEL=INFO
ALLOWED_HOSTS=yourdomain.com,api.yourdomain.com
CORS_ORIGINS=https://yourdomain.com,https://app.yourdomain.com
```

```bash
# .env.testing
ENVIRONMENT=testing
DEBUG=false
DB_HOST=localhost
DB_USERNAME=test_user
DB_PASSWORD=test_password
DB_DATABASE=test_db
JWT_SECRET_KEY=test-secret-key-for-testing-only
LOG_LEVEL=WARNING
```

#### 3. Settings Factory Pattern

```python
# config.py
from functools import lru_cache
from typing import Type
import os

@lru_cache()
def get_settings() -> Settings:
    # Determine environment
    env = os.getenv("ENVIRONMENT", "development").lower()
    
    # Load appropriate .env file
    env_file = f".env.{env}"
    if os.path.exists(env_file):
        return Settings(_env_file=env_file)
    else:
        return Settings()

# Usage in FastAPI
from fastapi import Depends

async def get_app_settings() -> Settings:
    return get_settings()
```

#### 4. Application Integration

```python
# main.py
from fastapi import FastAPI, Depends
from config import get_settings, Settings
from database import create_database_engine
from middleware import setup_middleware

def create_app() -> FastAPI:
    settings = get_settings()
    
    app = FastAPI(
        title=settings.app_name,
        version=settings.app_version,
        docs_url=settings.docs_url,
        redoc_url=settings.redoc_url,
        debug=settings.debug,
    )
    
    # Setup middleware based on settings
    setup_middleware(app, settings)
    
    # Create database engine
    create_database_engine(settings.database.url)
    
    return app

app = create_app()

@app.get("/config")
async def get_config(settings: Settings = Depends(get_app_settings)):
    # Return non-sensitive config info
    return {
        "app_name": settings.app_name,
        "version": settings.app_version,
        "environment": settings.environment,
        "debug": settings.debug,
        "api_prefix": settings.api_v1_prefix,
    }
```

#### 5. Testing with Different Settings

```python
# test_settings.py
import pytest
from config import Settings
import tempfile
import os

@pytest.fixture
def test_settings():
    # Create temporary .env file for testing
    with tempfile.NamedTemporaryFile(mode='w', suffix='.env', delete=False) as f:
        f.write("""
ENVIRONMENT=testing
DEBUG=false
DB_HOST=test-db
DB_USERNAME=test_user
DB_PASSWORD=test_pass
DB_DATABASE=test_db
JWT_SECRET_KEY=test-secret-key-for-testing-purposes
        """)
        f.flush()
        
        # Load settings from temporary file
        settings = Settings(_env_file=f.name)
        
        yield settings
        
        # Cleanup
        os.unlink(f.name)

def test_settings_loading(test_settings):
    assert test_settings.environment == "testing"
    assert test_settings.debug is False
    assert test_settings.database.host == "test-db"
    assert test_settings.is_testing is True
```

## Question 54: How do you implement refresh tokens and access token rotation with JWT in FastAPI?

### Complete JWT Authentication System with Refresh Tokens

#### 1. Token Models and Schemas

```python
# auth_models.py
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
    expires_in: int

class TokenPayload(BaseModel):
    sub: Optional[str] = None
    exp: Optional[int] = None
    iat: Optional[int] = None
    jti: Optional[str] = None  # JWT ID for refresh token
    token_type: Optional[str] = None  # "access" or "refresh"

class RefreshTokenRequest(BaseModel):
    refresh_token: str

class LoginRequest(BaseModel):
    username: str
    password: str
```

#### 2. JWT Service Implementation

```python
# jwt_service.py
import jwt
from datetime import datetime, timedelta
from typing import Optional, Dict, Any
import uuid
from passlib.context import CryptContext
from config import get_settings
import redis
import json

settings = get_settings()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Redis client for storing refresh tokens
redis_client = redis.Redis(
    host=settings.redis.host,
    port=settings.redis.port,
    password=settings.redis.password,
    db=settings.redis.db,
    decode_responses=True
)

class JWTService:
    def __init__(self):
        self.secret_key = settings.jwt.secret_key
        self.algorithm = settings.jwt.algorithm
        self.access_token_expire_minutes = settings.jwt.access_token_expire_minutes
        self.refresh_token_expire_days = settings.jwt.refresh_token_expire_days

    def create_access_token(self, data: Dict[str, Any]) -> str:
        to_encode = data.copy()
        expire = datetime.utcnow() + timedelta(minutes=self.access_token_expire_minutes)
        
        to_encode.update({
            "exp": expire,
            "iat": datetime.utcnow(),
            "token_type": "access"
        })
        
        return jwt.encode(to_encode, self.secret_key, algorithm=self.algorithm)

    def create_refresh_token(self, data: Dict[str, Any]) -> str:
        to_encode = data.copy()
        expire = datetime.utcnow() + timedelta(days=self.refresh_token_expire_days)
        jti = str(uuid.uuid4())  # Unique token ID
        
        to_encode.update({
            "exp": expire,
            "iat": datetime.utcnow(),
            "jti": jti,
            "token_type": "refresh"
        })
        
        refresh_token = jwt.encode(to_encode, self.secret_key, algorithm=self.algorithm)
        
        # Store refresh token in Redis with expiration
        token_data = {
            "user_id": data.get("sub"),
            "jti": jti,
            "created_at": datetime.utcnow().isoformat(),
            "is_active": True
        }
        
        redis_key = f"refresh_token:{jti}"
        redis_client.setex(
            redis_key,
            timedelta(days=self.refresh_token_expire_days),
            json.dumps(token_data)
        )
        
        return refresh_token

    def verify_token(self, token: str, token_type: str = "access") -> Optional[TokenPayload]:
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
            
            # Verify token type
            if payload.get("token_type") != token_type:
                return None
            
            # For refresh tokens, verify it exists in Redis and is active
            if token_type == "refresh":
                jti = payload.get("jti")
                if not jti:
                    return None
                
                redis_key = f"refresh_token:{jti}"
                token_data = redis_client.get(redis_key)
                
                if not token_data:
                    return None
                
                token_info = json.loads(token_data)
                if not token_info.get("is_active", False):
                    return None
            
            return TokenPayload(**payload)
            
        except jwt.ExpiredSignatureError:
            return None
        except jwt.JWTError:
            return None

    def revoke_refresh_token(self, jti: str) -> bool:
        """Revoke a refresh token by marking it as inactive"""
        redis_key = f"refresh_token:{jti}"
        token_data = redis_client.get(redis_key)
        
        if token_data:
            token_info = json.loads(token_data)
            token_info["is_active"] = False
            redis_client.setex(
                redis_key,
                timedelta(days=self.refresh_token_expire_days),
                json.dumps(token_info)
            )
            return True
        return False

    def revoke_all_user_tokens(self, user_id: str) -> int:
        """Revoke all refresh tokens for a user"""
        pattern = "refresh_token:*"
        revoked_count = 0
        
        for key in redis_client.scan_iter(match=pattern):
            token_data = redis_client.get(key)
            if token_data:
                token_info = json.loads(token_data)
                if token_info.get("user_id") == user_id and token_info.get("is_active"):
                    token_info["is_active"] = False
                    redis_client.setex(
                        key,
                        timedelta(days=self.refresh_token_expire_days),
                        json.dumps(token_info)
                    )
                    revoked_count += 1
        
        return revoked_count

    def get_user_active_tokens(self, user_id: str) -> list:
        """Get all active refresh tokens for a user"""
        pattern = "refresh_token:*"
        tokens = []
        
        for key in redis_client.scan_iter(match=pattern):
            token_data = redis_client.get(key)
            if token_data:
                token_info = json.loads(token_data)
                if (token_info.get("user_id") == user_id and 
                    token_info.get("is_active")):
                    tokens.append(token_info)
        
        return tokens

jwt_service = JWTService()
```

#### 3. Authentication Dependencies

```python
# auth_dependencies.py
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jwt_service import jwt_service, TokenPayload
from database import get_db
from models import User
from sqlalchemy.orm import Session

security = HTTPBearer()

async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    token_payload = jwt_service.verify_token(credentials.credentials, "access")
    if token_payload is None or token_payload.sub is None:
        raise credentials_exception
    
    user = db.query(User).filter(User.id == token_payload.sub).first()
    if user is None:
        raise credentials_exception
    
    return user

async def get_current_active_user(
    current_user: User = Depends(get_current_user)
) -> User:
    if not current_user.is_active:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Inactive user"
        )
    return current_user
```

#### 4. Authentication Routes

```python
# auth_routes.py
from fastapi import APIRouter, Depends, HTTPException, status, Response
from fastapi.security import HTTPBearer
from sqlalchemy.orm import Session
from database import get_db
from models import User
from auth_models import Token, LoginRequest, RefreshTokenRequest
from jwt_service import jwt_service
from auth_dependencies import get_current_active_user
from passlib.context import CryptContext
import logging

router = APIRouter(prefix="/auth", tags=["authentication"])
security = HTTPBearer()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
logger = logging.getLogger(__name__)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def authenticate_user(db: Session, username: str, password: str) -> User:
    user = db.query(User).filter(User.username == username).first()
    if not user or not verify_password(password, user.hashed_password):
        return None
    return user

@router.post("/login", response_model=Token)
async def login(
    login_data: LoginRequest,
    response: Response,
    db: Session = Depends(get_db)
):
    user = authenticate_user(db, login_data.username, login_data.password)
    if not user:
        logger.warning(f"Failed login attempt for username: {login_data.username}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Inactive user"
        )
    
    # Create tokens
    token_data = {"sub": str(user.id), "username": user.username}
    access_token = jwt_service.create_access_token(token_data)
    refresh_token = jwt_service.create_refresh_token(token_data)
    
    # Set refresh token as HTTP-only cookie
    response.set_cookie(
        key="refresh_token",
        value=refresh_token,
        httponly=True,
        secure=True,  # Set to False for development
        samesite="strict",
        max_age=jwt_service.refresh_token_expire_days * 24 * 60 * 60
    )
    
    logger.info(f"User {user.username} logged in successfully")
    
    return Token(
        access_token=access_token,
        refresh_token=refresh_token,
        expires_in=jwt_service.access_token_expire_minutes * 60
    )

@router.post("/refresh", response_model=Token)
async def refresh_token(
    refresh_data: RefreshTokenRequest,
    response: Response,
    db: Session = Depends(get_db)
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate refresh token",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    # Verify refresh token
    token_payload = jwt_service.verify_token(refresh_data.refresh_token, "refresh")
    if token_payload is None or token_payload.sub is None:
        raise credentials_exception
    
    # Get user
    user = db.query(User).filter(User.id == token_payload.sub).first()
    if user is None or not user.is_active:
        raise credentials_exception
    
    # Revoke old refresh token
    if token_payload.jti:
        jwt_service.revoke_refresh_token(token_payload.jti)
    
    # Create new tokens (token rotation)
    token_data = {"sub": str(user.id), "username": user.username}
    new_access_token = jwt_service.create_access_token(token_data)
    new_refresh_token = jwt_service.create_refresh_token(token_data)
    
    # Update refresh token cookie
    response.set_cookie(
        key="refresh_token",
        value=new_refresh_token,
        httponly=True,
        secure=True,
        samesite="strict",
        max_age=jwt_service.refresh_token_expire_days * 24 * 60 * 60
    )
    
    logger.info(f"Tokens refreshed for user {user.username}")
    
    return Token(
        access_token=new_access_token,
        refresh_token=new_refresh_token,
        expires_in=jwt_service.access_token_expire_minutes * 60
    )

@router.post("/logout")
async def logout(
    response: Response,
    refresh_data: RefreshTokenRequest,
    current_user: User = Depends(get_current_active_user)
):
    # Verify and revoke refresh token
    token_payload = jwt_service.verify_token(refresh_data.refresh_token, "refresh")
    if token_payload and token_payload.jti:
        jwt_service.revoke_refresh_token(token_payload.jti)
    
    # Clear refresh token cookie
    response.delete_cookie(key="refresh_token")
    
    logger.info(f"User {current_user.username} logged out")
    return {"message": "Successfully logged out"}

@router.post("/logout-all")
async def logout_all_devices(
    response: Response,
    current_user: User = Depends(get_current_active_user)
):
    # Revoke all refresh tokens for the user
    revoked_count = jwt_service.revoke_all_user_tokens(str(current_user.id))
    
    # Clear refresh token cookie
    response.delete_cookie(key="refresh_token")
    
    logger.info(f"All tokens revoked for user {current_user.username}, count: {revoked_count}")
    return {"message": f"Logged out from {revoked_count} devices"}

@router.get("/me")
async def get_current_user_info(
    current_user: User = Depends(get_current_active_user)
):
    return {
        "id": current_user.id,
        "username": current_user.username,
        "email": current_user.email,
        "is_active": current_user.is_active,
    }

@router.get("/sessions")
async def get_active_sessions(
    current_user: User = Depends(get_current_active_user)
):
    """Get all active sessions (refresh tokens) for the current user"""
    active_tokens = jwt_service.get_user_active_tokens(str(current_user.id))
    return {
        "active_sessions": len(active_tokens),
        "sessions": [
            {
                "jti": token["jti"],
                "created_at": token["created_at"],
            }
            for token in active_tokens
        ]
    }
```

#### 5. Frontend Integration Example

```javascript
// auth.js - Frontend token management
class AuthService {
    constructor() {
        this.baseURL = 'http://localhost:8000/auth';
        this.accessToken = localStorage.getItem('access_token');
    }

    async login(username, password) {
        const response = await fetch(`${this.baseURL}/login`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ username, password }),
            credentials: 'include', // Include cookies
        });

        if (!response.ok) {
            throw new Error('Login failed');
        }

        const data = await response.json();
        this.accessToken = data.access_token;
        localStorage.setItem('access_token', data.access_token);
        
        return data;
    }

    async refreshToken() {
        const response = await fetch(`${this.baseURL}/refresh`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                refresh_token: this.getRefreshTokenFromCookie()
            }),
            credentials: 'include',
        });

        if (!response.ok) {
            this.logout();
            throw new Error('Token refresh failed');
        }

        const data = await response.json();
        this.accessToken = data.access_token;
        localStorage.setItem('access_token', data.access_token);
        
        return data;
    }

    async apiCall(url, options = {}) {
        // Add authorization header
        const headers = {
            'Authorization': `Bearer ${this.accessToken}`,
            'Content-Type': 'application/json',
            ...options.headers,
        };

        let response = await fetch(url, {
            ...options,
            headers,
            credentials: 'include',
        });

        // If token expired, try to refresh
        if (response.status === 401) {
            try {
                await this.refreshToken();
                // Retry with new token
                headers['Authorization'] = `Bearer ${this.accessToken}`;
                response = await fetch(url, {
                    ...options,
                    headers,
                    credentials: 'include',
                });
            } catch (error) {
                this.logout();
                throw error;
            }
        }

        return response;
    }

    logout() {
        this.accessToken = null;
        localStorage.removeItem('access_token');
        // Redirect to login page
        window.location.href = '/login';
    }

    getRefreshTokenFromCookie() {
        const cookies = document.cookie.split(';');
        for (let cookie of cookies) {
            const [name, value] = cookie.trim().split('=');
            if (name === 'refresh_token') {
                return value;
            }
        }
        return null;
    }
}

const authService = new AuthService();
```

## Question 55: How do you secure WebSockets or background tasks in FastAPI with user identity?

### WebSocket Authentication and Authorization

#### 1. WebSocket Authentication Setup

```python
# websocket_auth.py
from fastapi import WebSocket, WebSocketDisconnect, HTTPException, Query
from jwt_service import jwt_service
from typing import Optional, Dict, List
import json
import logging
from models import User
from database import SessionLocal

logger = logging.getLogger(__name__)

class ConnectionManager:
    def __init__(self):
        # Store active connections with user information
        self.active_connections: Dict[str, Dict] = {}
        # Store connections by user ID for easy lookup
        self.user_connections: Dict[str, List[str]] = {}

    async def connect(self, websocket: WebSocket, connection_id: str, user: User):
        await websocket.accept()
        
        # Store connection info
        self.active_connections[connection_id] = {
            "websocket": websocket,
            "user": user,
            "user_id": str(user.id),
            "username": user.username,
        }
        
        # Track user connections
        user_id = str(user.id)
        if user_id not in self.user_connections:
            self.user_connections[user_id] = []
        self.user_connections[user_id].append(connection_id)
        
        logger.info(f"WebSocket connected: {user.username} ({connection_id})")

    def disconnect(self, connection_id: str):
        if connection_id in self.active_connections:
            connection_info = self.active_connections[connection_id]
            user_id = connection_info["user_id"]
            username = connection_info["username"]
            
            # Remove from active connections
            del self.active_connections[connection_id]
            
            # Remove from user connections
            if user_id in self.user_connections:
                self.user_connections[user_id].remove(connection_id)
                if not self.user_connections[user_id]:
                    del self.user_connections[user_id]
            
            logger.info(f"WebSocket disconnected: {username} ({connection_id})")

    async def send_personal_message(self, message: str, connection_id: str):
        if connection_id in self.active_connections:
            websocket = self.active_connections[connection_id]["websocket"]
            await websocket.send_text(message)

    async def send_to_user(self, message: str, user_id: str):
        """Send message to all connections of a specific user"""
        if user_id in self.user_connections:
            for connection_id in self.user_connections[user_id]:
                await self.send_personal_message(message, connection_id)

    async def broadcast(self, message: str, exclude_user_id: Optional[str] = None):
        """Broadcast message to all connected users except excluded user"""
        for connection_id, connection_info in self.active_connections.items():
            if exclude_user_id and connection_info["user_id"] == exclude_user_id:
                continue
            await self.send_personal_message(message, connection_id)

    async def send_to_users(self, message: str, user_ids: List[str]):
        """Send message to specific users"""
        for user_id in user_ids:
            await self.send_to_user(message, user_id)

    def get_user_info(self, connection_id: str) -> Optional[User]:
        if connection_id in self.active_connections:
            return self.active_connections[connection_id]["user"]
        return None

    def get_connected_users(self) -> List[Dict]:
        """Get list of all connected users"""
        users = []
        for connection_info in self.active_connections.values():
            user_info = {
                "user_id": connection_info["user_id"],
                "username": connection_info["username"],
            }
            if user_info not in users:
                users.append(user_info)
        return users

manager = ConnectionManager()

async def authenticate_websocket_user(token: str) -> Optional[User]:
    """Authenticate user from WebSocket token"""
    try:
        # Verify JWT token
        token_payload = jwt_service.verify_token(token, "access")
        if not token_payload or not token_payload.sub:
            return None
        
        # Get user from database
        db = SessionLocal()
        try:
            user = db.query(User).filter(User.id == token_payload.sub).first()
            if user and user.is_active:
                return user
        finally:
            db.close()
        
        return None
    except Exception as e:
        logger.error(f"WebSocket authentication error: {str(e)}")
        return None
```

#### 2. WebSocket Routes with Authentication

```python
# websocket_routes.py
from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Depends, Query
from websocket_auth import manager, authenticate_websocket_user
from typing import Optional
import json
import uuid
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

@router.websocket("/ws/{token}")
async def websocket_endpoint(websocket: WebSocket, token: str):
    # Authenticate user
    user = await authenticate_websocket_user(token)
    if not user:
        await websocket.close(code=4001, reason="Authentication failed")
        return
    
    connection_id = str(uuid.uuid4())
    
    try:
        await manager.connect(websocket, connection_id, user)
        
        # Send welcome message
        await manager.send_personal_message(
            json.dumps({
                "type": "welcome",
                "message": f"Welcome {user.username}!",
                "user_id": str(user.id)
            }),
            connection_id
        )
        
        # Notify other users about new connection
        await manager.broadcast(
            json.dumps({
                "type": "user_joined",
                "username": user.username,
                "user_id": str(user.id)
            }),
            exclude_user_id=str(user.id)
        )
        
        while True:
            # Receive message from client
            data = await websocket.receive_text()
            
            try:
                message_data = json.loads(data)
                await handle_websocket_message(message_data, connection_id)
            except json.JSONDecodeError:
                await manager.send_personal_message(
                    json.dumps({
                        "type": "error",
                        "message": "Invalid JSON format"
                    }),
                    connection_id
                )
                
    except WebSocketDisconnect:
        manager.disconnect(connection_id)
        
        # Notify other users about disconnection
        await manager.broadcast(
            json.dumps({
                "type": "user_left",
                "username": user.username,
                "user_id": str(user.id)
            }),
            exclude_user_id=str(user.id)
        )

async def handle_websocket_message(message_data: dict, connection_id: str):
    """Handle different types of WebSocket messages"""
    user = manager.get_user_info(connection_id)
    if not user:
        return
    
    message_type = message_data.get("type")
    
    if message_type == "chat":
        # Handle chat message
        await handle_chat_message(message_data, connection_id, user)
    elif message_type == "private_message":
        # Handle private message
        await handle_private_message(message_data, connection_id, user)
    elif message_type == "typing":
        # Handle typing indicator
        await handle_typing_indicator(message_data, connection_id, user)
    else:
        await manager.send_personal_message(
            json.dumps({
                "type": "error",
                "message": f"Unknown message type: {message_type}"
            }),
            connection_id
        )

async def handle_chat_message(message_data: dict, connection_id: str, user):
    """Handle public chat messages"""
    message = message_data.get("message", "")
    if not message.strip():
        return
    
    # Broadcast message to all users
    await manager.broadcast(
        json.dumps({
            "type": "chat",
            "message": message,
            "username": user.username,
            "user_id": str(user.id),
            "timestamp": datetime.utcnow().isoformat()
        })
    )
    
    logger.info(f"Chat message from {user.username}: {message}")

async def handle_private_message(message_data: dict, connection_id: str, user):
    """Handle private messages between users"""
    target_user_id = message_data.get("target_user_id")
    message = message_data.get("message", "")
    
    if not target_user_id or not message.strip():
        await manager.send_personal_message(
            json.dumps({
                "type": "error",
                "message": "Target user ID and message are required"
            }),
            connection_id
        )
        return
    
    # Send to target user
    await manager.send_to_user(
        json.dumps({
            "type": "private_message",
            "message": message,
            "from_username": user.username,
            "from_user_id": str(user.id),
            "timestamp": datetime.utcnow().isoformat()
        }),
        target_user_id
    )
    
    # Send confirmation to sender
    await manager.send_personal_message(
        json.dumps({
            "type": "private_message_sent",
            "message": message,
            "to_user_id": target_user_id,
            "timestamp": datetime.utcnow().isoformat()
        }),
        connection_id
    )

async def handle_typing_indicator(message_data: dict, connection_id: str, user):
    """Handle typing indicators"""
    is_typing = message_data.get("is_typing", False)
    
    await manager.broadcast(
        json.dumps({
            "type": "typing",
            "username": user.username,
            "user_id": str(user.id),
            "is_typing": is_typing
        }),
        exclude_user_id=str(user.id)
    )

@router.get("/ws/users")
async def get_connected_users():
    """Get list of currently connected users"""
    return {"connected_users": manager.get_connected_users()}
```

### Background Task Security

#### 3. Secure Background Task System

```python
# background_tasks.py
from celery import Celery
from sqlalchemy.orm import Session
from database import SessionLocal
from models import User, Task
from typing import Optional, Dict, Any
import logging
from datetime import datetime
from jwt_service import jwt_service

logger = logging.getLogger(__name__)

# Celery setup
celery_app = Celery(
    "fastapi_tasks",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)

class SecureTaskManager:
    """Manager for secure background tasks with user context"""
    
    @staticmethod
    def create_task_with_user(
        task_func,
        user_id: str,
        task_data: Dict[str, Any],
        task_type: str = "general"
    ):
        """Create a background task with user context"""
        # Store task in database with user association
        db = SessionLocal()
        try:
            task = Task(
                user_id=user_id,
                task_type=task_type,
                status="pending",
                created_at=datetime.utcnow(),
                task_data=task_data
            )
            db.add(task)
            db.commit()
            db.refresh(task)
            
            # Execute Celery task with task ID and user ID
            result = task_func.delay(str(task.id), user_id, task_data)
            
            # Update task with Celery task ID
            task.celery_task_id = result.id
            db.commit()
            
            logger.info(f"Created task {task.id} for user {user_id}")
            return task.id
            
        finally:
            db.close()

    @staticmethod
    def get_user_tasks(user_id: str, status: Optional[str] = None) -> list:
        """Get tasks for a specific user"""
        db = SessionLocal()
        try:
            query = db.query(Task).filter(Task.user_id == user_id)
            if status:
                query = query.filter(Task.status == status)
            return query.all()
        finally:
            db.close()

    @staticmethod
    def update_task_status(task_id: str, status: str, result: Optional[Dict] = None):
        """Update task status and result"""
        db = SessionLocal()
        try:
            task = db.query(Task).filter(Task.id == task_id).first()
            if task:
                task.status = status
                task.updated_at = datetime.utcnow()
                if result:
                    task.result = result
                db.commit()
                logger.info(f"Updated task {task_id} status to {status}")
        finally:
            db.close()

# Secure task decorators
def secure_task(task_type: str = "general"):
    """Decorator for creating secure Celery tasks"""
    def decorator(func):
        @celery_app.task(bind=True)
        def wrapper(self, task_id: str, user_id: str, task_data: Dict[str, Any]):
            try:
                # Verify user exists and is active
                db = SessionLocal()
                try:
                    user = db.query(User).filter(User.id == user_id).first()
                    if not user or not user.is_active:
                        raise ValueError(f"Invalid or inactive user: {user_id}")
                finally:
                    db.close()
                
                # Update task status to running
                SecureTaskManager.update_task_status(task_id, "running")
                
                # Execute the actual task function
                result = func(task_id, user_id, task_data)
                
                # Update task status to completed
                SecureTaskManager.update_task_status(task_id, "completed", result)
                
                return result
                
            except Exception as e:
                logger.error(f"Task {task_id} failed: {str(e)}")
                SecureTaskManager.update_task_status(
                    task_id, 
                    "failed", 
                    {"error": str(e)}
                )
                raise
        
        wrapper.original_func = func
        wrapper.task_type = task_type
        return wrapper
    return decorator

# Example secure background tasks
@secure_task("email")
def send_email_task(task_id: str, user_id: str, task_data: Dict[str, Any]):
    """Send email background task with user context"""
    recipient = task_data.get("recipient")
    subject = task_data.get("subject")
    body = task_data.get("body")
    
    # Verify user has permission to send email
    db = SessionLocal()
    try:
        user = db.query(User).filter(User.id == user_id).first()
        if not user.can_send_emails:
            raise PermissionError("User does not have email sending permissions")
    finally:
        db.close()
    
    # Simulate email sending
    import time
    time.sleep(2)
    
    logger.info(f"Email sent to {recipient} by user {user_id}")
    return {"status": "sent", "recipient": recipient}

@secure_task("report")
def generate_report_task(task_id: str, user_id: str, task_data: Dict[str, Any]):
    """Generate report background task with user context"""
    report_type = task_data.get("report_type")
    filters = task_data.get("filters", {})
    
    # Verify user has access to requested data
    db = SessionLocal()
    try:
        user = db.query(User).filter(User.id == user_id).first()
        if not user.has_role("analyst") and report_type == "sensitive":
            raise PermissionError("User does not have access to sensitive reports")
    finally:
        db.close()
    
    # Generate report
    report_data = {
        "report_type": report_type,
        "generated_by": user_id,
        "data": "Report content here...",
        "generated_at": datetime.utcnow().isoformat()
    }
    
    logger.info(f"Report generated for user {user_id}")
    return report_data

@secure_task("file_processing")
def process_file_task(task_id: str, user_id: str, task_data: Dict[str, Any]):
    """Process uploaded file with user context"""
    file_path = task_data.get("file_path")
    processing_type = task_data.get("processing_type")
    
    # Verify user owns the file
    db = SessionLocal()
    try:
        from models import UserFile
        file_record = db.query(UserFile).filter(
            UserFile.file_path == file_path,
            UserFile.user_id == user_id
        ).first()
        
        if not file_record:
            raise PermissionError("User does not have access to this file")
    finally:
        db.close()
    
    # Process file
    import time
    time.sleep(5)  # Simulate processing
    
    processed_data = {
        "file_path": file_path,
        "processing_type": processing_type,
        "processed_at": datetime.utcnow().isoformat(),
        "result": "File processed successfully"
    }
    
    logger.info(f"File processed for user {user_id}")
    return processed_data

# Task management API routes
@router.post("/tasks/email")
async def create_email_task(
    email_data: dict,
    current_user: User = Depends(get_current_active_user)
):
    """Create an email sending task"""
    task_id = SecureTaskManager.create_task_with_user(
        send_email_task,
        str(current_user.id),
        email_data,
        "email"
    )
    
    return {"task_id": task_id, "status": "created"}

@router.post("/tasks/report")
async def create_report_task(
    report_data: dict,
    current_user: User = Depends(get_current_active_user)
):
    """Create a report generation task"""
    task_id = SecureTaskManager.create_task_with_user(
        generate_report_task,
        str(current_user.id),
        report_data,
        "report"
    )
    
    return {"task_id": task_id, "status": "created"}

@router.get("/tasks")
async def get_user_tasks(
    status: Optional[str] = None,
    current_user: User = Depends(get_current_active_user)
):
    """Get all tasks for the current user"""
    tasks = SecureTaskManager.get_user_tasks(str(current_user.id), status)
    
    return {
        "tasks": [
            {
                "id": task.id,
                "task_type": task.task_type,
                "status": task.status,
                "created_at": task.created_at.isoformat(),
                "updated_at": task.updated_at.isoformat() if task.updated_at else None,
                "result": task.result
            }
            for task in tasks
        ]
    }

@router.get("/tasks/{task_id}")
async def get_task_status(
    task_id: str,
    current_user: User = Depends(get_current_active_user)
):
    """Get status of a specific task"""
    db = SessionLocal()
    try:
        task = db.query(Task).filter(
            Task.id == task_id,
            Task.user_id == str(current_user.id)
        ).first()
        
        if not task:
            raise HTTPException(status_code=404, detail="Task not found")
        
        return {
            "id": task.id,
            "task_type": task.task_type,
            "status": task.status,
            "created_at": task.created_at.isoformat(),
            "updated_at": task.updated_at.isoformat() if task.updated_at else None,
            "result": task.result
        }
    finally:
        db.close()
```

#### 4. WebSocket Authentication with Frontend

```javascript
// websocket_client.js
class SecureWebSocket {
    constructor(baseURL) {
        this.baseURL = baseURL;
        this.websocket = null;
        this.reconnectAttempts = 0;
        this.maxReconnectAttempts = 5;
        this.reconnectDelay = 1000;
        this.messageHandlers = new Map();
    }

    async connect() {
        const token = localStorage.getItem('access_token');
        if (!token) {
            throw new Error('No access token available');
        }

        const wsURL = `${this.baseURL}/ws/${token}`;
        
        try {
            this.websocket = new WebSocket(wsURL);
            this.setupEventHandlers();
            
            return new Promise((resolve, reject) => {
                this.websocket.onopen = () => {
                    console.log('WebSocket connected');
                    this.reconnectAttempts = 0;
                    resolve();
                };
                
                this.websocket.onerror = (error) => {
                    console.error('WebSocket connection error:', error);
                    reject(error);
                };
            });
        } catch (error) {
            console.error('Failed to create WebSocket connection:', error);
            throw error;
        }
    }

    setupEventHandlers() {
        this.websocket.onmessage = (event) => {
            try {
                const data = JSON.parse(event.data);
                this.handleMessage(data);
            } catch (error) {
                console.error('Error parsing WebSocket message:', error);
            }
        };

        this.websocket.onclose = (event) => {
            console.log('WebSocket connection closed:', event.code, event.reason);
            
            if (event.code === 4001) {
                // Authentication failed
                console.error('WebSocket authentication failed');
                // Redirect to login or refresh token
                this.handleAuthenticationError();
            } else {
                // Try to reconnect
                this.handleReconnect();
            }
        };

        this.websocket.onerror = (error) => {
            console.error('WebSocket error:', error);
        };
    }

    handleMessage(data) {
        const messageType = data.type;
        
        if (this.messageHandlers.has(messageType)) {
            this.messageHandlers.get(messageType)(data);
        } else {
            console.log('Unhandled message type:', messageType, data);
        }
    }

    onMessage(messageType, handler) {
        this.messageHandlers.set(messageType, handler);
    }

    sendMessage(messageType, data) {
        if (this.websocket && this.websocket.readyState === WebSocket.OPEN) {
            const message = {
                type: messageType,
                ...data
            };
            this.websocket.send(JSON.stringify(message));
        } else {
            console.error('WebSocket is not connected');
        }
    }

    sendChatMessage(message) {
        this.sendMessage('chat', { message });
    }

    sendPrivateMessage(targetUserId, message) {
        this.sendMessage('private_message', {
            target_user_id: targetUserId,
            message
        });
    }

    sendTypingIndicator(isTyping) {
        this.sendMessage('typing', { is_typing: isTyping });
    }

    async handleAuthenticationError() {
        // Try to refresh token
        try {
            const authService = new AuthService();
            await authService.refreshToken();
            // Reconnect with new token
            await this.connect();
        } catch (error) {
            // Redirect to login
            window.location.href = '/login';
        }
    }

    handleReconnect() {
        if (this.reconnectAttempts < this.maxReconnectAttempts) {
            this.reconnectAttempts++;
            const delay = this.reconnectDelay * this.reconnectAttempts;
            
            console.log(`Attempting to reconnect in ${delay}ms... (${this.reconnectAttempts}/${this.maxReconnectAttempts})`);
            
            setTimeout(async () => {
                try {
                    await this.connect();
                } catch (error) {
                    console.error('Reconnection failed:', error);
                }
            }, delay);
        } else {
            console.error('Max reconnection attempts reached');
        }
    }

    disconnect() {
        if (this.websocket) {
            this.websocket.close();
            this.websocket = null;
        }
    }
}

// Usage example
const ws = new SecureWebSocket('ws://localhost:8000');

// Set up message handlers
ws.onMessage('welcome', (data) => {
    console.log('Welcome message:', data.message);
});

ws.onMessage('chat', (data) => {
    displayChatMessage(data.username, data.message, data.timestamp);
});

ws.onMessage('private_message', (data) => {
    displayPrivateMessage(data.from_username, data.message, data.timestamp);
});

ws.onMessage('typing', (data) => {
    showTypingIndicator(data.username, data.is_typing);
});

// Connect to WebSocket
ws.connect().catch(console.error);
```

## Question 56: What are scopes in OAuth2, and how can FastAPI enforce them per route?

### OAuth2 Scopes Implementation

#### 1. Scope Definition and Management

```python
# oauth2_scopes.py
from enum import Enum
from typing import List, Dict, Set
from dataclasses import dataclass

class OAuth2Scope(str, Enum):
    # User scopes
    USER_READ = "user:read"
    USER_WRITE = "user:write"
    USER_DELETE = "user:delete"
    
    # Profile scopes
    PROFILE_READ = "profile:read"
    PROFILE_WRITE = "profile:write"
    
    # Admin scopes
    ADMIN_READ = "admin:read"
    ADMIN_WRITE = "admin:write"
    ADMIN_DELETE = "admin:delete"
    
    # Resource scopes
    POSTS_READ = "posts:read"
    POSTS_WRITE = "posts:write"
    POSTS_DELETE = "posts:delete"
    
    # File scopes
    FILES_READ = "files:read"
    FILES_WRITE = "files:write"
    FILES_DELETE = "files:delete"
    
    # Analytics scopes
    ANALYTICS_READ = "analytics:read"
    ANALYTICS_WRITE = "analytics:write"
    
    # System scopes
    SYSTEM_READ = "system:read"
    SYSTEM_WRITE = "system:write"

@dataclass
class ScopeInfo:
    name: str
    description: str
    category: str
    is_sensitive: bool = False

# Scope definitions with descriptions
SCOPE_DEFINITIONS: Dict[OAuth2Scope, ScopeInfo] = {
    OAuth2Scope.USER_READ: ScopeInfo(
        "Read User Data",
        "Read basic user information",
        "user"
    ),
    OAuth2Scope.USER_WRITE: ScopeInfo(
        "Write User Data",
        "Create and update user information",
        "user"
    ),
    OAuth2Scope.USER_DELETE: ScopeInfo(
        "Delete Users",
        "Delete user accounts",
        "user",
        is_sensitive=True
    ),
    OAuth2Scope.PROFILE_READ: ScopeInfo(
        "Read Profile",
        "Read user profile information",
        "profile"
    ),
    OAuth2Scope.PROFILE_WRITE: ScopeInfo(
        "Write Profile",
        "Update user profile information",
        "profile"
    ),
    OAuth2Scope.ADMIN_READ: ScopeInfo(
        "Admin Read",
        "Read administrative data",
        "admin",
        is_sensitive=True
    ),
    OAuth2Scope.ADMIN_WRITE: ScopeInfo(
        "Admin Write",
        "Perform administrative operations",
        "admin",
        is_sensitive=True
    ),
    OAuth2Scope.ADMIN_DELETE: ScopeInfo(
        "Admin Delete",
        "Delete administrative data",
        "admin",
        is_sensitive=True
    ),
    # ... add more scope definitions
}

# Role-based scope mappings
ROLE_SCOPES: Dict[str, Set[OAuth2Scope]] = {
    "user": {
        OAuth2Scope.USER_READ,
        OAuth2Scope.PROFILE_READ,
        OAuth2Scope.PROFILE_WRITE,
        OAuth2Scope.POSTS_READ,
        OAuth2Scope.FILES_READ,
    },
    "moderator": {
        OAuth2Scope.USER_READ,
        OAuth2Scope.PROFILE_READ,
        OAuth2Scope.PROFILE_WRITE,
        OAuth2Scope.POSTS_READ,
        OAuth2Scope.POSTS_WRITE,
        OAuth2Scope.POSTS_DELETE,
        OAuth2Scope.FILES_READ,
        OAuth2Scope.FILES_WRITE,
    },
    "admin": {
        OAuth2Scope.USER_READ,
        OAuth2Scope.USER_WRITE,
        OAuth2Scope.USER_DELETE,
        OAuth2Scope.PROFILE_READ,
        OAuth2Scope.PROFILE_WRITE,
        OAuth2Scope.ADMIN_READ,
        OAuth2Scope.ADMIN_WRITE,
        OAuth2Scope.ADMIN_DELETE,
        OAuth2Scope.POSTS_READ,
        OAuth2Scope.POSTS_WRITE,
        OAuth2Scope.POSTS_DELETE,
        OAuth2Scope.FILES_READ,
        OAuth2Scope.FILES_WRITE,
        OAuth2Scope.FILES_DELETE,
        OAuth2Scope.ANALYTICS_READ,
        OAuth2Scope.ANALYTICS_WRITE,
        OAuth2Scope.SYSTEM_READ,
        OAuth2Scope.SYSTEM_WRITE,
    },
    "system": {
        # All scopes for system access
        *OAuth2Scope.__members__.values()
    }
}

class ScopeManager:
    @staticmethod
    def get_scopes_for_role(role: str) -> Set[OAuth2Scope]:
        """Get all scopes for a given role"""
        return ROLE_SCOPES.get(role, set())
    
    @staticmethod
    def get_scopes_for_roles(roles: List[str]) -> Set[OAuth2Scope]:
        """Get combined scopes for multiple roles"""
        combined_scopes = set()
        for role in roles:
            combined_scopes.update(ROLE_SCOPES.get(role, set()))
        return combined_scopes
    
    @staticmethod
    def validate_scopes(requested_scopes: List[str]) -> List[OAuth2Scope]:
        """Validate and convert string scopes to OAuth2Scope enum"""
        valid_scopes = []
        for scope_str in requested_scopes:
            try:
                scope = OAuth2Scope(scope_str)
                valid_scopes.append(scope)
            except ValueError:
                pass  # Invalid scope, skip it
        return valid_scopes
    
    @staticmethod
    def check_scope_permission(user_scopes: Set[OAuth2Scope], required_scopes: List[OAuth2Scope]) -> bool:
        """Check if user has all required scopes"""
        return set(required_scopes).issubset(user_scopes)
```

#### 2. OAuth2 Security with Scopes

```python
# oauth2_security.py
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jwt_service import jwt_service
from oauth2_scopes import OAuth2Scope, ScopeManager
from models import User, UserRole
from database import get_db
from sqlalchemy.orm import Session
from typing import List, Set, Optional
import logging

logger = logging.getLogger(__name__)
security = HTTPBearer()

class OAuth2SecurityManager:
    def __init__(self):
        self.scope_manager = ScopeManager()
    
    async def get_current_user_with_scopes(
        self,
        credentials: HTTPAuthorizationCredentials = Depends(security),
        db: Session = Depends(get_db)
    ) -> tuple[User, Set[OAuth2Scope]]:
        """Get current user and their scopes"""
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        
        # Verify JWT token
        token_payload = jwt_service.verify_token(credentials.credentials, "access")
        if not token_payload or not token_payload.sub:
            raise credentials_exception
        
        # Get user from database
        user = db.query(User).filter(User.id == token_payload.sub).first()
        if not user or not user.is_active:
            raise credentials_exception
        
        # Get user roles and calculate scopes
        user_roles = [role.name for role in user.roles]
        user_scopes = self.scope_manager.get_scopes_for_roles(user_roles)
        
        # Add any additional scopes from token (if present)
        token_scopes = getattr(token_payload, 'scopes', [])
        if token_scopes:
            additional_scopes = self.scope_manager.validate_scopes(token_scopes)
            user_scopes.update(additional_scopes)
        
        return user, user_scopes
    
    def require_scopes(self, *required_scopes: OAuth2Scope):
        """Dependency factory for requiring specific scopes"""
        async def check_scopes(
            user_and_scopes: tuple[User, Set[OAuth2Scope]] = Depends(self.get_current_user_with_scopes)
        ) -> User:
            user, user_scopes = user_and_scopes
            
            if not self.scope_manager.check_scope_permission(user_scopes, list(required_scopes)):
                missing_scopes = set(required_scopes) - user_scopes
                logger.warning(
                    f"User {user.username} missing scopes: {[s.value for s in missing_scopes]}"
                )
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail=f"Insufficient permissions. Missing scopes: {[s.value for s in missing_scopes]}"
                )
            
            return user
        
        return check_scopes
    
    def require_any_scope(self, *required_scopes: OAuth2Scope):
        """Dependency factory for requiring any of the specified scopes"""
        async def check_any_scope(
            user_and_scopes: tuple[User, Set[OAuth2Scope]] = Depends(self.get_current_user_with_scopes)
        ) -> User:
            user, user_scopes = user_and_scopes
            
            if not any(scope in user_scopes for scope in required_scopes):
                logger.warning(
                    f"User {user.username} missing any of required scopes: {[s.value for s in required_scopes]}"
                )
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail=f"Insufficient permissions. Need one of: {[s.value for s in required_scopes]}"
                )
            
            return user
        
        return check_any_scope

oauth2_security = OAuth2SecurityManager()
```

#### 3. Enhanced JWT Service with Scopes

```python
# enhanced_jwt_service.py (additions to existing jwt_service.py)
from oauth2_scopes import OAuth2Scope, ScopeManager
from typing import List

class EnhancedJWTService(JWTService):
    def __init__(self):
        super().__init__()
        self.scope_manager = ScopeManager()
    
    def create_access_token_with_scopes(
        self, 
        data: Dict[str, Any], 
        scopes: List[OAuth2Scope]
    ) -> str:
        """Create access token with specific scopes"""
        to_encode = data.copy()
        expire = datetime.utcnow() + timedelta(minutes=self.access_token_expire_minutes)
        
        to_encode.update({
            "exp": expire,
            "iat": datetime.utcnow(),
            "token_type": "access",
            "scopes": [scope.value for scope in scopes]
        })
        
        return jwt.encode(to_encode, self.secret_key, algorithm=self.algorithm)
    
    def create_tokens_for_user(
        self, 
        user: User, 
        requested_scopes: Optional[List[str]] = None
    ) -> Dict[str, str]:
        """Create tokens for user with appropriate scopes"""
        # Get user roles and calculate available scopes
        user_roles = [role.name for role in user.roles]
        available_scopes = self.scope_manager.get_scopes_for_roles(user_roles)
        
        # Filter requested scopes to only include available ones
        if requested_scopes:
            valid_requested_scopes = self.scope_manager.validate_scopes(requested_scopes)
            granted_scopes = [
                scope for scope in valid_requested_scopes 
                if scope in available_scopes
            ]
        else:
            granted_scopes = list(available_scopes)
        
        token_data = {
            "sub": str(user.id),
            "username": user.username,
            "roles": user_roles
        }
        
        access_token = self.create_access_token_with_scopes(token_data, granted_scopes)
        refresh_token = self.create_refresh_token(token_data)
        
        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "granted_scopes": [scope.value for scope in granted_scopes]
        }

enhanced_jwt_service = EnhancedJWTService()
```

#### 4. Route Implementation with Scopes

```python
# scoped_routes.py
from fastapi import APIRouter, Depends, HTTPException, Query
from oauth2_security import oauth2_security
from oauth2_scopes import OAuth2Scope
from models import User, Post
from typing import List, Optional

router = APIRouter()

# User management routes
@router.get("/users", dependencies=[Depends(oauth2_security.require_scopes(OAuth2Scope.USER_READ))])
async def get_users(
    limit: int = Query(10, le=100),
    offset: int = Query(0, ge=0)
):
    """Get users - requires user:read scope"""
    # Implementation
    return {"users": [], "total": 0}

@router.post("/users", dependencies=[Depends(oauth2_security.require_scopes(OAuth2Scope.USER_WRITE))])
async def create_user(user_data: dict):
    """Create user - requires user:write scope"""
    # Implementation
    return {"message": "User created"}

@router.delete("/users/{user_id}")
async def delete_user(
    user_id: str,
    current_user: User = Depends(oauth2_security.require_scopes(OAuth2Scope.USER_DELETE))
):
    """Delete user - requires user:delete scope"""
    # Implementation
    return {"message": f"User {user_id} deleted"}

# Profile routes
@router.get("/profile")
async def get_profile(
    current_user: User = Depends(oauth2_security.require_scopes(OAuth2Scope.PROFILE_READ))
):
    """Get user profile - requires profile:read scope"""
    return {
        "id": current_user.id,
        "username": current_user.username,
        "email": current_user.email
    }

@router.put("/profile")
async def update_profile(
    profile_data: dict,
    current_user: User = Depends(oauth2_security.require_scopes(OAuth2Scope.PROFILE_WRITE))
):
    """Update user profile - requires profile:write scope"""
    # Implementation
    return {"message": "Profile updated"}

# Admin routes
@router.get("/admin/users")
async def admin_get_users(
    current_user: User = Depends(oauth2_security.require_scopes(OAuth2Scope.ADMIN_READ))
):
    """Admin user management - requires admin:read scope"""
    # Implementation
    return {"admin_users": []}

@router.post("/admin/system/maintenance")
async def system_maintenance(
    current_user: User = Depends(oauth2_security.require_scopes(
        OAuth2Scope.ADMIN_WRITE, 
        OAuth2Scope.SYSTEM_WRITE
    ))
):
    """System maintenance - requires both admin:write and system:write scopes"""
    # Implementation
    return {"message": "Maintenance mode enabled"}

# Posts with flexible scope requirements
@router.get("/posts")
async def get_posts(
    current_user: User = Depends(oauth2_security.require_any_scope(
        OAuth2Scope.POSTS_READ,
        OAuth2Scope.ADMIN_READ
    ))
):
    """Get posts - requires posts:read OR admin:read scope"""
    # Implementation
    return {"posts": []}

@router.delete("/posts/{post_id}")
async def delete_post(
    post_id: str,
    current_user: User = Depends(oauth2_security.require_any_scope(
        OAuth2Scope.POSTS_DELETE,
        OAuth2Scope.ADMIN_DELETE
    ))
):
    """Delete post - requires posts:delete OR admin:delete scope"""
    # Implementation
    return {"message": f"Post {post_id} deleted"}

# Conditional scope-based access
@router.get("/analytics")
async def get_analytics(
    user_and_scopes = Depends(oauth2_security.get_current_user_with_scopes)
):
    """Get analytics with different data based on scopes"""
    user, user_scopes = user_and_scopes
    
    analytics_data = {"basic_stats": {"users": 100, "posts": 500}}
    
    # Add detailed analytics if user has analytics:read scope
    if OAuth2Scope.ANALYTICS_READ in user_scopes:
        analytics_data["detailed_stats"] = {
            "revenue": 10000,
            "conversion_rate": 0.05,
            "user_growth": 0.15
        }
    
    # Add sensitive analytics if user has admin scope
    if OAuth2Scope.ADMIN_READ in user_scopes:
        analytics_data["sensitive_stats"] = {
            "server_costs": 5000,
            "profit_margin": 0.3,
            "churn_rate": 0.02
        }
    
    return analytics_data

# Scope information endpoint
@router.get("/oauth2/scopes")
async def get_available_scopes():
    """Get information about available OAuth2 scopes"""
    from oauth2_scopes import SCOPE_DEFINITIONS
    
    scopes_info = {}
    for scope, info in SCOPE_DEFINITIONS.items():
        scopes_info[scope.value] = {
            "name": info.name,
            "description": info.description,
            "category": info.category,
            "is_sensitive": info.is_sensitive
        }
    
    return {"scopes": scopes_info}

@router.get("/oauth2/my-scopes")
async def get_my_scopes(
    user_and_scopes = Depends(oauth2_security.get_current_user_with_scopes)
):
    """Get current user's granted scopes"""
    user, user_scopes = user_and_scopes
    
    return {
        "user_id": str(user.id),
        "username": user.username,
        "scopes": [scope.value for scope in user_scopes],
        "roles": [role.name for role in user.roles]
    }
```

#### 5. OAuth2 Authorization Flow with Scopes

```python
# oauth2_auth_flow.py
from fastapi import APIRouter, Depends, HTTPException, Form, Query, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlalchemy.orm import Session
from database import get_db
from models import User, OAuth2Client, OAuth2AuthorizationCode
from oauth2_scopes import OAuth2Scope, ScopeManager, SCOPE_DEFINITIONS
from enhanced_jwt_service import enhanced_jwt_service
from typing import List, Optional
import secrets
import urllib.parse
from datetime import datetime, timedelta

router = APIRouter(prefix="/oauth2", tags=["OAuth2"])

class OAuth2AuthorizationServer:
    def __init__(self):
        self.scope_manager = ScopeManager()
    
    async def validate_client(self, client_id: str, db: Session) -> Optional[OAuth2Client]:
        """Validate OAuth2 client"""
        return db.query(OAuth2Client).filter(
            OAuth2Client.client_id == client_id,
            OAuth2Client.is_active == True
        ).first()
    
    async def validate_redirect_uri(self, client: OAuth2Client, redirect_uri: str) -> bool:
        """Validate redirect URI against registered URIs"""
        return redirect_uri in client.redirect_uris
    
    def validate_scopes(self, requested_scopes: List[str], client: OAuth2Client) -> List[OAuth2Scope]:
        """Validate requested scopes against client allowed scopes"""
        valid_scopes = self.scope_manager.validate_scopes(requested_scopes)
        client_allowed_scopes = self.scope_manager.validate_scopes(client.allowed_scopes)
        
        # Only return scopes that are both valid and allowed for this client
        return [scope for scope in valid_scopes if scope in client_allowed_scopes]

oauth2_server = OAuth2AuthorizationServer()

@router.get("/authorize")
async def authorization_endpoint(
    request: Request,
    response_type: str = Query(...),
    client_id: str = Query(...),
    redirect_uri: str = Query(...),
    scope: str = Query(""),
    state: Optional[str] = Query(None),
    db: Session = Depends(get_db)
):
    """OAuth2 authorization endpoint"""
    
    # Validate response_type
    if response_type != "code":
        raise HTTPException(status_code=400, detail="Unsupported response_type")
    
    # Validate client
    client = await oauth2_server.validate_client(client_id, db)
    if not client:
        raise HTTPException(status_code=400, detail="Invalid client_id")
    
    # Validate redirect_uri
    if not await oauth2_server.validate_redirect_uri(client, redirect_uri):
        raise HTTPException(status_code=400, detail="Invalid redirect_uri")
    
    # Parse and validate scopes
    requested_scopes = scope.split() if scope else []
    valid_scopes = oauth2_server.validate_scopes(requested_scopes, client)
    
    # Store authorization request in session or database
    auth_request = {
        "client_id": client_id,
        "redirect_uri": redirect_uri,
        "scopes": [s.value for s in valid_scopes],
        "state": state
    }
    
    # Check if user is already authenticated
    # (In real implementation, check session/JWT token)
    user_authenticated = False  # Placeholder
    
    if not user_authenticated:
        # Redirect to login with authorization parameters
        login_url = f"/login?{urllib.parse.urlencode(auth_request)}"
        return RedirectResponse(url=login_url)
    
    # Show consent screen
    return await show_consent_screen(auth_request, valid_scopes, client, db)

async def show_consent_screen(auth_request: dict, scopes: List[OAuth2Scope], client: OAuth2Client, db: Session):
    """Show OAuth2 consent screen"""
    scope_details = []
    for scope in scopes:
        if scope in SCOPE_DEFINITIONS:
            scope_info = SCOPE_DEFINITIONS[scope]
            scope_details.append({
                "scope": scope.value,
                "name": scope_info.name,
                "description": scope_info.description,
                "is_sensitive": scope_info.is_sensitive
            })
    
    consent_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Authorize {client.name}</title>
        <style>
            body {{ font-family: Arial, sans-serif; max-width: 600px; margin: 50px auto; padding: 20px; }}
            .app-info {{ background: #f5f5f5; padding: 20px; border-radius: 5px; margin-bottom: 20px; }}
            .scope {{ padding: 10px; border-bottom: 1px solid #eee; }}
            .scope.sensitive {{ background: #fff3cd; }}
            .buttons {{ margin-top: 20px; }}
            button {{ padding: 10px 20px; margin: 5px; border: none; border-radius: 3px; cursor: pointer; }}
            .approve {{ background: #28a745; color: white; }}
            .deny {{ background: #dc3545; color: white; }}
        </style>
    </head>
    <body>
        <div class="app-info">
            <h2>{client.name}</h2>
            <p>{client.description}</p>
            <p>wants to access your account with the following permissions:</p>
        </div>
        
        <div class="scopes">
            {chr(10).join([
                f'<div class="scope{"  sensitive" if s["is_sensitive"] else ""}">'
                f'<strong>{s["name"]}</strong><br>'
                f'<small>{s["description"]}</small>'
                f'</div>'
                for s in scope_details
            ])}
        </div>
        
        <form method="post" action="/oauth2/consent">
            <input type="hidden" name="client_id" value="{auth_request['client_id']}">
            <input type="hidden" name="redirect_uri" value="{auth_request['redirect_uri']}">
            <input type="hidden" name="scopes" value="{' '.join(auth_request['scopes'])}">
            <input type="hidden" name="state" value="{auth_request.get('state', '')}">
            
            <div class="buttons">
                <button type="submit" name="action" value="approve" class="approve">Authorize</button>
                <button type="submit" name="action" value="deny" class="deny">Deny</button>
            </div>
        </form>
    </body>
    </html>
    """
    
    return HTMLResponse(content=consent_html)

@router.post("/consent")
async def consent_endpoint(
    action: str = Form(...),
    client_id: str = Form(...),
    redirect_uri: str = Form(...),
    scopes: str = Form(""),
    state: Optional[str] = Form(None),
    db: Session = Depends(get_db),
    # current_user: User = Depends(get_current_user)  # Assume user is authenticated
):
    """Handle user consent"""
    current_user = None  # Placeholder - get from authentication
    
    if action != "approve":
        # User denied authorization
        error_params = {"error": "access_denied"}
        if state:
            error_params["state"] = state
        error_url = f"{redirect_uri}?{urllib.parse.urlencode(error_params)}"
        return RedirectResponse(url=error_url)
    
    # Generate authorization code
    auth_code = secrets.token_urlsafe(32)
    expires_at = datetime.utcnow() + timedelta(minutes=10)  # 10 minute expiry
    
    # Store authorization code
    db_auth_code = OAuth2AuthorizationCode(
        code=auth_code,
        client_id=client_id,
        user_id=str(current_user.id),
        redirect_uri=redirect_uri,
        scopes=scopes.split(),
        expires_at=expires_at
    )
    db.add(db_auth_code)
    db.commit()
    
    # Redirect back to client with authorization code
    callback_params = {"code": auth_code}
    if state:
        callback_params["state"] = state
    
    callback_url = f"{redirect_uri}?{urllib.parse.urlencode(callback_params)}"
    return RedirectResponse(url=callback_url)

@router.post("/token")
async def token_endpoint(
    grant_type: str = Form(...),
    code: Optional[str] = Form(None),
    redirect_uri: Optional[str] = Form(None),
    client_id: str = Form(...),
    client_secret: str = Form(...),
    scope: Optional[str] = Form(None),
    db: Session = Depends(get_db)
):
    """OAuth2 token endpoint"""
    
    # Validate client credentials
    client = db.query(OAuth2Client).filter(
        OAuth2Client.client_id == client_id,
        OAuth2Client.client_secret == client_secret,
        OAuth2Client.is_active == True
    ).first()
    
    if not client:
        raise HTTPException(status_code=401, detail="Invalid client credentials")
    
    if grant_type == "authorization_code":
        # Authorization code flow
        if not code or not redirect_uri:
            raise HTTPException(status_code=400, detail="Missing code or redirect_uri")
        
        # Validate authorization code
        auth_code_record = db.query(OAuth2AuthorizationCode).filter(
            OAuth2AuthorizationCode.code == code,
            OAuth2AuthorizationCode.client_id == client_id,
            OAuth2AuthorizationCode.redirect_uri == redirect_uri,
            OAuth2AuthorizationCode.is_used == False,
            OAuth2AuthorizationCode.expires_at > datetime.utcnow()
        ).first()
        
        if not auth_code_record:
            raise HTTPException(status_code=400, detail="Invalid or expired authorization code")
        
        # Mark code as used
        auth_code_record.is_used = True
        db.commit()
        
        # Get user
        user = db.query(User).filter(User.id == auth_code_record.user_id).first()
        if not user or not user.is_active:
            raise HTTPException(status_code=400, detail="Invalid user")
        
        # Create tokens with granted scopes
        token_data = enhanced_jwt_service.create_tokens_for_user(
            user, 
            auth_code_record.scopes
        )
        
        return {
            "access_token": token_data["access_token"],
            "refresh_token": token_data["refresh_token"],
            "token_type": "bearer",
            "expires_in": enhanced_jwt_service.access_token_expire_minutes * 60,
            "scope": " ".join(token_data["granted_scopes"])
        }
    
    elif grant_type == "client_credentials":
        # Client credentials flow (for machine-to-machine)
        requested_scopes = scope.split() if scope else []
        valid_scopes = oauth2_server.validate_scopes(requested_scopes, client)
        
        # Create token for client (no user context)
        token_data = {
            "sub": client.client_id,
            "client_id": client.client_id,
            "token_type": "client_credentials"
        }
        
        access_token = enhanced_jwt_service.create_access_token_with_scopes(
            token_data, 
            valid_scopes
        )
        
        return {
            "access_token": access_token,
            "token_type": "bearer",
            "expires_in": enhanced_jwt_service.access_token_expire_minutes * 60,
            "scope": " ".join([s.value for s in valid_scopes])
        }
    
    else:
        raise HTTPException(status_code=400, detail="Unsupported grant_type")
```

## Question 57: How do you customize the OpenAPI schema or documentation UI in FastAPI?

### Complete OpenAPI Customization

#### 1. Basic OpenAPI Schema Customization

```python
# openapi_customization.py
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from fastapi.openapi.docs import get_swagger_ui_html, get_redoc_html
from fastapi.staticfiles import StaticFiles
from typing import Dict, Any, Optional
import json

def create_custom_openapi_schema(app: FastAPI) -> Dict[str, Any]:
    """Create customized OpenAPI schema"""
    if app.openapi_schema:
        return app.openapi_schema
    
    openapi_schema = get_openapi(
        title="Advanced FastAPI Application",
        version="2.0.0",
        description="""
        ## Advanced FastAPI Application with OAuth2 and Scopes
        
        This API demonstrates advanced FastAPI features including:
        
        * **OAuth2 Authentication** with scopes
        * **JWT Token Management** with refresh tokens
        * **WebSocket Support** with authentication
        * **Background Tasks** with user context
        * **Multi-tenancy** support
        * **Rate Limiting** and security
        
        ### Authentication
        
        This API uses OAuth2 with JWT tokens. To authenticate:
        
        1. Obtain an access token from `/auth/login`
        2. Include the token in the Authorization header: `Bearer <token>`
        3. Tokens include scopes that determine available operations
        
        ### Rate Limits
        
        * **Standard users**: 1000 requests/hour
        * **Premium users**: 10000 requests/hour
        * **Admin users**: Unlimited
        
        ### Support
        
        For support, contact: support@example.com
        """,
        routes=app.routes,
        contact={
            "name": "API Support Team",
            "url": "https://example.com/contact",
            "email": "support@example.com"
        },
        license_info={
            "name": "MIT License",
            "url": "https://opensource.org/licenses/MIT"
        },
        servers=[
            {
                "url": "https://api.example.com",
                "description": "Production server"
            },
            {
                "url": "https://staging-api.example.com", 
                "description": "Staging server"
            },
            {
                "url": "http://localhost:8000",
                "description": "Development server"
            }
        ]
    )
    
    # Add custom security schemes
    openapi_schema["components"]["securitySchemes"] = {
        "OAuth2": {
            "type": "oauth2",
            "flows": {
                "authorizationCode": {
                    "authorizationUrl": "/oauth2/authorize",
                    "tokenUrl": "/oauth2/token",
                    "scopes": {
                        "user:read": "Read user information",
                        "user:write": "Write user information", 
                        "user:delete": "Delete users",
                        "profile:read": "Read user profile",
                        "profile:write": "Write user profile",
                        "admin:read": "Read admin data",
                        "admin:write": "Write admin data",
                        "admin:delete": "Delete admin data",
                        "posts:read": "Read posts",
                        "posts:write": "Write posts",
                        "posts:delete": "Delete posts",
                        "files:read": "Read files",
                        "files:write": "Write files",
                        "files:delete": "Delete files",
                        "analytics:read": "Read analytics",
                        "analytics:write": "Write analytics",
                        "system:read": "Read system data",
                        "system:write": "Write system data"
                    }
                },
                "clientCredentials": {
                    "tokenUrl": "/oauth2/token",
                    "scopes": {
                        "api:read": "Read API data",
                        "api:write": "Write API data"
                    }
                }
            }
        },
        "BearerAuth": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT"
        },
        "ApiKeyAuth": {
            "type": "apiKey",
            "in": "header",
            "name": "X-API-Key"
        }
    }
    
    # Add custom tags with descriptions
    openapi_schema["tags"] = [
        {
            "name": "authentication",
            "description": "Authentication and authorization operations",
            "externalDocs": {
                "description": "Auth documentation",
                "url": "https://docs.example.com/auth"
            }
        },
        {
            "name": "users",
            "description": "User management operations"
        },
        {
            "name": "posts", 
            "description": "Blog post operations"
        },
        {
            "name": "admin",
            "description": "Administrative operations",
            "externalDocs": {
                "description": "Admin guide",
                "url": "https://docs.example.com/admin"
            }
        },
        {
            "name": "websockets",
            "description": "Real-time WebSocket connections"
        },
        {
            "name": "files",
            "description": "File upload and management"
        }
    ]
    
    # Add custom extensions
    openapi_schema["x-logo"] = {
        "url": "https://example.com/logo.png",
        "altText": "API Logo"
    }
    
    # Add API versioning info
    openapi_schema["x-api-id"] = "advanced-fastapi-api"
    openapi_schema["x-audience"] = "external"
    
    app.openapi_schema = openapi_schema
    return app.openapi_schema

def customize_openapi_operation(
    operation_id: str,
    summary: str,
    description: str,
    tags: list,
    responses: Optional[Dict] = None,
    security: Optional[list] = None,
    deprecated: bool = False
):
    """Decorator to customize OpenAPI operation details"""
    def decorator(func):
        # Store metadata on function
        func.__openapi_operation__ = {
            "operation_id": operation_id,
            "summary": summary, 
            "description": description,
            "tags": tags,
            "responses": responses or {},
            "security": security,
            "deprecated": deprecated
        }
        return func
    return decorator
```

#### 2. Custom Documentation UI

```python
# custom_docs.py
from fastapi import FastAPI, Request
from fastapi.openapi.docs import get_swagger_ui_html, get_redoc_html
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import json

def setup_custom_docs(app: FastAPI):
    """Setup custom documentation endpoints"""
    
    # Mount static files for custom assets
    app.mount("/static", StaticFiles(directory="static"), name="static")
    
    # Custom Swagger UI
    @app.get("/docs", include_in_schema=False)
    async def custom_swagger_ui_html():
        return get_swagger_ui_html(
            openapi_url="/openapi.json",
            title=f"{app.title} - Interactive API Documentation",
            swagger_js_url="https://unpkg.com/swagger-ui-dist@5.9.0/swagger-ui-bundle.js",
            swagger_css_url="https://unpkg.com/swagger-ui-dist@5.9.0/swagger-ui.css",
            swagger_ui_parameters={
                "deepLinking": True,
                "displayRequestDuration": True,
                "docExpansion": "none",
                "operationsSorter": "method",
                "tagsSorter": "alpha",
                "filter": True,
                "tryItOutEnabled": True,
                "persistAuthorization": True,
                "displayOperationId": True,
                "showExtensions": True,
                "showCommonExtensions": True,
                "defaultModelsExpandDepth": 2,
                "defaultModelExpandDepth": 2,
                "requestInterceptor": """
                (request) => {
                    // Add custom headers or modify requests
                    request.headers['X-Custom-Header'] = 'SwaggerUI';
                    return request;
                }
                """,
                "responseInterceptor": """
                (response) => {
                    // Log responses or modify them
                    console.log('API Response:', response);
                    return response;
                }
                """
            }
        )
    
    # Custom ReDoc
    @app.get("/redoc", include_in_schema=False)
    async def custom_redoc_html():
        return get_redoc_html(
            openapi_url="/openapi.json",
            title=f"{app.title} - API Reference",
            redoc_js_url="https://unpkg.com/redoc@next/bundles/redoc.standalone.js",
            with_google_fonts=True,
            redoc_options={
                "nativeScrollbars": True,
                "theme": {
                    "colors": {
                        "primary": {
                            "main": "#1976d2"
                        }
                    },
                    "typography": {
                        "fontSize": "14px",
                        "fontFamily": "Arial, sans-serif",
                        "headings": {
                            "fontFamily": "Arial, sans-serif",
                            "fontWeight": "600"
                        },
                        "code": {
                            "fontSize": "13px",
                            "fontFamily": "'Courier New', monospace"
                        }
                    },
                    "sidebar": {
                        "width": "300px"
                    }
                },
                "hideDownloadButton": False,
                "disableSearch": False,
                "expandResponses": "200,201",
                "requiredPropsFirst": True,
                "sortPropsAlphabetically": True,
                "showExtensions": True,
                "hideHostname": False,
                "expandSingleSchemaField": True,
                "menuToggle": True,
                "scrollYOffset": 0,
                "hideLoading": False
            }
        )
    
    # Custom API explorer with additional features
    @app.get("/api-explorer", include_in_schema=False)
    async def api_explorer():
        html_content = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>API Explorer - Advanced FastAPI</title>
            <link rel="stylesheet" href="https://unpkg.com/swagger-ui-dist@5.9.0/swagger-ui.css" />
            <style>
                body { font-family: Arial, sans-serif; margin: 0; }
                .header { background: #1976d2; color: white; padding: 20px; text-align: center; }
                .nav { background: #f5f5f5; padding: 10px; text-align: center; }
                .nav a { margin: 0 15px; text-decoration: none; color: #1976d2; font-weight: bold; }
                .nav a:hover { text-decoration: underline; }
                .content { padding: 20px; }
                .feature-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; margin: 20px 0; }
                .feature-card { border: 1px solid #ddd; border-radius: 8px; padding: 20px; }
                .feature-card h3 { color: #1976d2; }
                #swagger-ui { margin-top: 20px; }
            </style>
        </head>
        <body>
            <div class="header">
                <h1>Advanced FastAPI - API Explorer</h1>
                <p>Comprehensive API documentation and testing interface</p>
            </div>
            
            <div class="nav">
                <a href="#overview">Overview</a>
                <a href="#authentication">Authentication</a>
                <a href="#endpoints">Endpoints</a>
                <a href="#websockets">WebSockets</a>
                <a href="#examples">Examples</a>
            </div>
            
            <div class="content">
                <div id="overview">
                    <h2>API Overview</h2>
                    <div class="feature-grid">
                        <div class="feature-card">
                            <h3>🔐 OAuth2 Authentication</h3>
                            <p>Secure authentication with JWT tokens and fine-grained scopes</p>
                        </div>
                        <div class="feature-card">
                            <h3>🔄 Real-time WebSockets</h3>
                            <p>Bi-directional communication with authentication support</p>
                        </div>
                        <div class="feature-card">
                            <h3>⚡ Background Tasks</h3>
                            <p>Asynchronous task processing with user context</p>
                        </div>
                        <div class="feature-card">
                            <h3>🏢 Multi-tenancy</h3>
                            <p>Support for multiple tenants with data isolation</p>
                        </div>
                    </div>
                </div>
                
                <div id="swagger-ui"></div>
            </div>
            
            <script src="https://unpkg.com/swagger-ui-dist@5.9.0/swagger-ui-bundle.js"></script>
            <script>
                const ui = SwaggerUIBundle({
                    url: '/openapi.json',
                    dom_id: '#swagger-ui',
                    deepLinking: true,
                    presets: [
                        SwaggerUIBundle.presets.apis,
                        SwaggerUIBundle.presets.standalone
                    ],
                    plugins: [
                        SwaggerUIBundle.plugins.DownloadUrl
                    ],
                    layout: "StandaloneLayout",
                    displayRequestDuration: true,
                    docExpansion: "list",
                    filter: true,
                    showExtensions: true,
                    showCommonExtensions: true,
                    tryItOutEnabled: true,
                    persistAuthorization: true,
                    onComplete: function() {
                        console.log('Swagger UI loaded');
                        // Add custom JavaScript functionality
                        addCustomFeatures();
                    }
                });
                
                function addCustomFeatures() {
                    // Add custom buttons or functionality
                    const toolbar = document.querySelector('.topbar');
                    if (toolbar) {
                        const customButton = document.createElement('button');
                        customButton.textContent = 'Generate SDK';
                        customButton.style.cssText = 'margin-left: 10px; padding: 8px 16px; background: #1976d2; color: white; border: none; border-radius: 4px; cursor: pointer;';
                        customButton.onclick = function() {
                            alert('SDK generation would be implemented here');
                        };
                        toolbar.appendChild(customButton);
                    }
                }
                
                // Add keyboard shortcuts
                document.addEventListener('keydown', function(e) {
                    // Ctrl+K to focus search
                    if (e.ctrlKey && e.key === 'k') {
                        e.preventDefault();
                        const searchInput = document.querySelector('.filter input');
                        if (searchInput) searchInput.focus();
                    }
                });
            </script>
        </body>
        </html>
        """
        return HTMLResponse(content=html_content)
    
    # OpenAPI JSON with custom processing
    @app.get("/openapi.json", include_in_schema=False)
    async def get_openapi_json():
        return app.openapi()
    
    # Alternative format exports
    @app.get("/openapi.yaml", include_in_schema=False)
    async def get_openapi_yaml():
        import yaml
        openapi_dict = app.openapi()
        yaml_content = yaml.dump(openapi_dict, default_flow_style=False)
        return Response(content=yaml_content, media_type="text/yaml")
    
    @app.get("/postman-collection", include_in_schema=False)
    async def get_postman_collection():
        """Generate Postman collection from OpenAPI spec"""
        openapi_dict = app.openapi()
        
        # Convert OpenAPI to Postman collection format
        postman_collection = {
            "info": {
                "name": openapi_dict["info"]["title"],
                "description": openapi_dict["info"]["description"],
                "version": openapi_dict["info"]["version"],
                "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
            },
            "item": [],
            "auth": {
                "type": "oauth2",
                "oauth2": [
                    {"key": "authUrl", "value": "/oauth2/authorize", "type": "string"},
                    {"key": "accessTokenUrl", "value": "/oauth2/token", "type": "string"},
                    {"key": "scope", "value": "user:read profile:read", "type": "string"}
                ]
            }
        }


# Advanced FastAPI: Multi-tenancy, API Versioning & GraphQL Integration

## 58. How would you implement multi-tenancy in FastAPI (e.g., subdomain-based or DB-schema based)?

Multi-tenancy allows a single application instance to serve multiple tenants while keeping their data isolated. Here are several approaches:

### Subdomain-based Multi-tenancy

```python
from fastapi import FastAPI, Request, HTTPException, Depends
from fastapi.middleware.base import BaseHTTPMiddleware
import re

app = FastAPI()

class TenantMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        host = request.headers.get("host", "")
        
        # Extract subdomain
        subdomain_match = re.match(r"^([^.]+)\.example\.com", host)
        if subdomain_match:
            tenant_id = subdomain_match.group(1)
            request.state.tenant_id = tenant_id
        else:
            request.state.tenant_id = "default"
        
        response = await call_next(request)
        return response

app.add_middleware(TenantMiddleware)

def get_tenant_id(request: Request) -> str:
    return getattr(request.state, "tenant_id", "default")

@app.get("/users")
async def get_users(tenant_id: str = Depends(get_tenant_id)):
    # Query users for specific tenant
    return {"tenant": tenant_id, "users": []}
```

### Database Schema-based Multi-tenancy

```python
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, Session
from fastapi import Depends, HTTPException
import asyncpg

class TenantDatabaseManager:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.engines = {}
    
    def get_tenant_engine(self, tenant_id: str):
        if tenant_id not in self.engines:
            # Create separate database per tenant
            db_url = f"{self.base_url}/tenant_{tenant_id}"
            self.engines[tenant_id] = create_engine(db_url)
        return self.engines[tenant_id]
    
    def get_tenant_session(self, tenant_id: str) -> Session:
        engine = self.get_tenant_engine(tenant_id)
        SessionLocal = sessionmaker(bind=engine)
        return SessionLocal()

# Schema-based approach (single database, multiple schemas)
class SchemaBasedTenancy:
    def __init__(self, database_url: str):
        self.engine = create_engine(database_url)
        self.SessionLocal = sessionmaker(bind=self.engine)
    
    def get_tenant_session(self, tenant_id: str) -> Session:
        session = self.SessionLocal()
        # Set schema for this session
        session.execute(text(f"SET search_path TO tenant_{tenant_id}"))
        return session

# Usage in FastAPI
tenant_manager = SchemaBasedTenancy("postgresql://user:pass@localhost/mydb")

async def get_db_session(tenant_id: str = Depends(get_tenant_id)):
    session = tenant_manager.get_tenant_session(tenant_id)
    try:
        yield session
    finally:
        session.close()

@app.get("/tenant-data")
async def get_tenant_data(
    tenant_id: str = Depends(get_tenant_id),
    db: Session = Depends(get_db_session)
):
    # Data is automatically isolated by schema
    result = db.execute(text("SELECT * FROM users"))
    return {"tenant": tenant_id, "data": result.fetchall()}
```

### Header-based Multi-tenancy

```python
from fastapi import Header, HTTPException

async def get_tenant_from_header(x_tenant_id: str = Header(...)):
    if not x_tenant_id:
        raise HTTPException(status_code=400, detail="Tenant ID required")
    return x_tenant_id

@app.get("/api/data")
async def get_data(tenant_id: str = Depends(get_tenant_from_header)):
    return {"tenant": tenant_id, "message": "Tenant isolated data"}
```

### Row-level Multi-tenancy

```python
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, ForeignKey

Base = declarative_base()

class Tenant(Base):
    __tablename__ = "tenants"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    tenant_id = Column(Integer, ForeignKey("tenants.id"))
    tenant = relationship("Tenant")

# Repository with tenant filtering
class UserRepository:
    def __init__(self, db: Session, tenant_id: str):
        self.db = db
        self.tenant_id = tenant_id
    
    def get_users(self):
        return self.db.query(User).filter(User.tenant_id == self.tenant_id).all()
    
    def create_user(self, user_data: dict):
        user_data["tenant_id"] = self.tenant_id
        user = User(**user_data)
        self.db.add(user)
        self.db.commit()
        return user

@app.get("/users")
async def list_users(
    tenant_id: str = Depends(get_tenant_id),
    db: Session = Depends(get_db_session)
):
    repo = UserRepository(db, tenant_id)
    users = repo.get_users()
    return {"users": users}
```

## 59. How do you version your OpenAPI documentation and avoid breaking client contracts?

API versioning is crucial for maintaining backward compatibility. Here are several strategies:

### URL Path Versioning

```python
from fastapi import FastAPI
from fastapi.routing import APIRouter

app = FastAPI()

# Version 1 API
v1_router = APIRouter(prefix="/api/v1", tags=["v1"])

@v1_router.get("/users")
async def get_users_v1():
    return {"users": [], "version": "1.0"}

# Version 2 API with breaking changes
v2_router = APIRouter(prefix="/api/v2", tags=["v2"])

@v2_router.get("/users")
async def get_users_v2():
    return {
        "data": {"users": []},
        "meta": {"version": "2.0", "total": 0}
    }

app.include_router(v1_router)
app.include_router(v2_router)
```

### Header-based Versioning

```python
from fastapi import Header, HTTPException
from typing import Optional

async def get_api_version(accept_version: Optional[str] = Header(None, alias="Accept-Version")):
    if accept_version is None:
        return "1.0"  # Default version
    
    if accept_version not in ["1.0", "2.0"]:
        raise HTTPException(status_code=400, detail="Unsupported API version")
    
    return accept_version

@app.get("/users")
async def get_users(version: str = Depends(get_api_version)):
    if version == "1.0":
        return {"users": []}
    elif version == "2.0":
        return {"data": {"users": []}, "meta": {"version": "2.0"}}
```

### Content Negotiation Versioning

```python
from fastapi import Request
import json

def parse_accept_header(accept_header: str) -> str:
    # Parse application/vnd.myapi.v2+json
    if "vnd.myapi.v2" in accept_header:
        return "2.0"
    elif "vnd.myapi.v1" in accept_header:
        return "1.0"
    return "1.0"  # Default

@app.get("/users")
async def get_users(request: Request):
    accept_header = request.headers.get("accept", "")
    version = parse_accept_header(accept_header)
    
    if version == "2.0":
        return {"data": {"users": []}}
    return {"users": []}
```

### Separate OpenAPI Documentation per Version

```python
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

def create_versioned_app(version: str) -> FastAPI:
    app = FastAPI(
        title=f"My API v{version}",
        version=version,
        docs_url=f"/docs/v{version}",
        redoc_url=f"/redoc/v{version}",
        openapi_url=f"/openapi/v{version}.json"
    )
    
    def custom_openapi():
        if app.openapi_schema:
            return app.openapi_schema
        
        openapi_schema = get_openapi(
            title=f"My API v{version}",
            version=version,
            description=f"API version {version} documentation",
            routes=app.routes,
        )
        
        # Add version-specific information
        openapi_schema["info"]["x-api-version"] = version
        app.openapi_schema = openapi_schema
        return app.openapi_schema
    
    app.openapi = custom_openapi
    return app

# Create separate apps for each version
v1_app = create_versioned_app("1.0")
v2_app = create_versioned_app("2.0")

main_app = FastAPI()
main_app.mount("/v1", v1_app)
main_app.mount("/v2", v2_app)
```

### Backward Compatibility Strategies

```python
from pydantic import BaseModel, Field
from typing import Optional, Union

# Flexible response models
class UserV1(BaseModel):
    id: int
    name: str

class UserV2(BaseModel):
    id: int
    full_name: str = Field(alias="name")  # Backward compatible
    email: Optional[str] = None

class VersionedResponse(BaseModel):
    data: Union[UserV1, UserV2]
    version: str

@app.get("/users/{user_id}")
async def get_user(
    user_id: int,
    version: str = Depends(get_api_version)
) -> VersionedResponse:
    # Fetch user data
    user_data = {"id": user_id, "name": "John Doe", "email": "john@example.com"}
    
    if version == "1.0":
        user = UserV1(**user_data)
    else:
        user = UserV2(**user_data)
    
    return VersionedResponse(data=user, version=version)
```

### Deprecation Warnings

```python
from fastapi import FastAPI, Response
import warnings

@app.get("/legacy-endpoint")
async def legacy_endpoint(response: Response):
    # Add deprecation headers
    response.headers["Warning"] = '299 - "Deprecated API"'
    response.headers["Sunset"] = "2024-12-31"
    response.headers["Link"] = '</api/v2/new-endpoint>; rel="successor-version"'
    
    warnings.warn("This endpoint is deprecated", DeprecationWarning)
    return {"message": "This endpoint is deprecated"}
```

## 60. Can FastAPI be used with GraphQL? How?

Yes, FastAPI can be integrated with GraphQL using libraries like Strawberry, Graphene, or Ariadne. Here are different approaches:

### Using Strawberry GraphQL

```python
from fastapi import FastAPI
import strawberry
from strawberry.fastapi import GraphQLRouter
from typing import List, Optional

# Define GraphQL types
@strawberry.type
class User:
    id: int
    name: str
    email: str

@strawberry.type
class Post:
    id: int
    title: str
    content: str
    author_id: int

# Sample data
users_db = [
    User(id=1, name="John Doe", email="john@example.com"),
    User(id=2, name="Jane Smith", email="jane@example.com")
]

posts_db = [
    Post(id=1, title="Hello World", content="First post", author_id=1),
    Post(id=2, title="GraphQL with FastAPI", content="Second post", author_id=1)
]

# Define queries
@strawberry.type
class Query:
    @strawberry.field
    def users(self) -> List[User]:
        return users_db
    
    @strawberry.field
    def user(self, id: int) -> Optional[User]:
        return next((user for user in users_db if user.id == id), None)
    
    @strawberry.field
    def posts(self) -> List[Post]:
        return posts_db
    
    @strawberry.field
    def posts_by_user(self, author_id: int) -> List[Post]:
        return [post for post in posts_db if post.author_id == author_id]

# Define mutations
@strawberry.input
class CreateUserInput:
    name: str
    email: str

@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_user(self, input: CreateUserInput) -> User:
        new_id = max(user.id for user in users_db) + 1
        new_user = User(id=new_id, name=input.name, email=input.email)
        users_db.append(new_user)
        return new_user

# Create schema
schema = strawberry.Schema(query=Query, mutation=Mutation)

# FastAPI app
app = FastAPI()

# Add GraphQL endpoint
graphql_app = GraphQLRouter(schema)
app.include_router(graphql_app, prefix="/graphql")

# Optional: Add REST endpoints alongside GraphQL
@app.get("/health")
async def health_check():
    return {"status": "healthy"}
```

### Using Graphene with FastAPI

```python
from fastapi import FastAPI
import graphene
from starlette.graphql import GraphQLApp

class User(graphene.ObjectType):
    id = graphene.Int()
    name = graphene.String()
    email = graphene.String()

class Query(graphene.ObjectType):
    users = graphene.List(User)
    user = graphene.Field(User, id=graphene.Int(required=True))
    
    def resolve_users(self, info):
        return [
            {"id": 1, "name": "John Doe", "email": "john@example.com"},
            {"id": 2, "name": "Jane Smith", "email": "jane@example.com"}
        ]
    
    def resolve_user(self, info, id):
        users = self.resolve_users(info)
        return next((user for user in users if user["id"] == id), None)

class CreateUser(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        email = graphene.String(required=True)
    
    user = graphene.Field(User)
    
    def mutate(self, info, name, email):
        # Create user logic here
        new_user = {"id": 3, "name": name, "email": email}
        return CreateUser(user=new_user)

class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)

app = FastAPI()
app.add_route("/graphql", GraphQLApp(schema=schema))
```

### Advanced GraphQL Integration with Database

```python
import strawberry
from sqlalchemy.orm import Session
from fastapi import Depends
from typing import List, Optional
import asyncio

# Database models (using SQLAlchemy)
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class UserModel(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    posts = relationship("PostModel", back_populates="author")

class PostModel(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(String)
    author_id = Column(Integer, ForeignKey("users.id"))
    author = relationship("UserModel", back_populates="posts")

# GraphQL types
@strawberry.type
class User:
    id: int
    name: str
    email: str
    
    @strawberry.field
    async def posts(self, info) -> List['Post']:
        # Access database session from context
        db: Session = info.context["db"]
        posts = db.query(PostModel).filter(PostModel.author_id == self.id).all()
        return [Post(id=p.id, title=p.title, content=p.content, author_id=p.author_id) for p in posts]

@strawberry.type
class Post:
    id: int
    title: str
    content: str
    author_id: int
    
    @strawberry.field
    async def author(self, info) -> Optional[User]:
        db: Session = info.context["db"]
        user = db.query(UserModel).filter(UserModel.id == self.author_id).first()
        if user:
            return User(id=user.id, name=user.name, email=user.email)
        return None

# Context provider
async def get_context(db: Session = Depends(get_db)):
    return {"db": db}

# Queries with database integration
@strawberry.type
class Query:
    @strawberry.field
    async def users(self, info) -> List[User]:
        db: Session = info.context["db"]
        users = db.query(UserModel).all()
        return [User(id=u.id, name=u.name, email=u.email) for u in users]
    
    @strawberry.field
    async def user(self, info, id: int) -> Optional[User]:
        db: Session = info.context["db"]
        user = db.query(UserModel).filter(UserModel.id == id).first()
        if user:
            return User(id=user.id, name=user.name, email=user.email)
        return None

# Schema with context
schema = strawberry.Schema(query=Query)

# GraphQL app with dependency injection
from strawberry.fastapi import GraphQLRouter

graphql_app = GraphQLRouter(
    schema,
    context_getter=get_context
)
app.include_router(graphql_app, prefix="/graphql")
```

### Subscription Support with WebSockets

```python
import strawberry
from strawberry.types import Info
from typing import AsyncGenerator
import asyncio

@strawberry.type
class Subscription:
    @strawberry.subscription
    async def user_updates(self, info: Info) -> AsyncGenerator[User, None]:
        # Simulate real-time updates
        while True:
            await asyncio.sleep(1)
            # Yield updated user data
            yield User(id=1, name="Updated User", email="updated@example.com")
    
    @strawberry.subscription
    async def post_created(self, info: Info) -> AsyncGenerator[Post, None]:
        # Listen for new posts
        while True:
            await asyncio.sleep(5)
            yield Post(id=999, title="New Post", content="Real-time post", author_id=1)

# Add subscription to schema
schema = strawberry.Schema(
    query=Query,
    mutation=Mutation,
    subscription=Subscription
)

# WebSocket support
from strawberry.fastapi import GraphQLRouter

graphql_app = GraphQLRouter(schema)
app.include_router(graphql_app, prefix="/graphql")
```

### Hybrid REST + GraphQL API

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Hybrid REST + GraphQL API")

# REST endpoints
class UserCreate(BaseModel):
    name: str
    email: str

@app.post("/api/users", response_model=User)
async def create_user_rest(user: UserCreate):
    # REST endpoint for user creation
    return {"id": 1, "name": user.name, "email": user.email}

@app.get("/api/users/{user_id}")
async def get_user_rest(user_id: int):
    # REST endpoint for single user
    return {"id": user_id, "name": "John Doe", "email": "john@example.com"}

# GraphQL endpoint
app.include_router(graphql_app, prefix="/graphql")

# Documentation endpoints
@app.get("/")
async def root():
    return {
        "message": "Hybrid API with REST and GraphQL",
        "rest_docs": "/docs",
        "graphql_playground": "/graphql"
    }
```

This comprehensive guide covers multi-tenancy implementation strategies, API versioning best practices, and GraphQL integration with FastAPI. Each approach has its trade-offs, and the choice depends on your specific requirements for scalability, maintainability, and client needs.