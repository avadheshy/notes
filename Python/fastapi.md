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

