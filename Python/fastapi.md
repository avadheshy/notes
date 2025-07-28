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