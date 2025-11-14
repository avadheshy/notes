#  FastAPI Path Operations and Data Validation

FastAPI is a modern, high-performance Python web framework for building APIs. It uses **path operations** to define how the application should respond to various HTTP requests.

---

##  What are Path Operations?

**Path operations** in FastAPI define how your API responds to HTTP methods like `GET`, `POST`, `PUT`, `DELETE`, etc., on specific **URLs (paths)**.

Each path operation is a **route handler** that corresponds to a combination of:

- **Path** (e.g., `/users`)
- **HTTP Method** (e.g., `GET`, `POST`)

---

##  Types of Path Operations (HTTP Methods)

| Method | Purpose                            | Example Usage                 |
|--------|------------------------------------|-------------------------------|
| `GET`  | Retrieve data                      | Get a list of users           |
| `POST` | Create new data                    | Create a new user             |
| `PUT`  | Update/replace existing data       | Replace user info             |
| `PATCH`| Partially update existing data     | Update a user's email         |
| `DELETE`| Remove data                       | Delete a user                 |

---

##  Example: Creating Path Operations

```
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# Pydantic model
class User(BaseModel):
    name: str
    email: str
    age: Optional[int] = None

# In-memory "database"
db = []

@app.get("/users")
def get_users():
    return db

@app.post("/users")
def create_user(user: User): # path operation function
    db.append(user)
    return {"message": "User created", "user": user}

@app.put("/users/{user_id}")
def update_user(user_id: int, user: User):
    db[user_id] = user
    return {"message": "User updated", "user": user}

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    deleted_user = db.pop(user_id)
    return {"message": "User deleted", "user": deleted_user}

```
# Importance of Data Validation in APIs
Data validation ensures:

API receives correct and expected data

Prevents invalid inputs from causing crashes or inconsistencies

Enhances security, reliability, and maintainability

# How FastAPI Uses Pydantic for Data Validation
FastAPI uses Pydantic models to:

Validate request bodies

Define response schemas

Automatically generate OpenAPI docs (Swagger UI)

Provide helpful error messages when data is invalid

Request Validation Example
```
@app.post("/register")
def register_user(user: User):
    return {"message": "User registered", "user": user}
```
FastAPI automatically parses the JSON body

Validates it against the User schema

Returns 422 Unprocessable Entity on validation errors

 Response Validation Example
```
from fastapi import Response
from fastapi.responses import JSONResponse
from typing import List

@app.get("/users", response_model=List[User])
def list_users():
    return db  # FastAPI ensures every item matches User schema
```
Ensures API response structure is guaranteed and documented

Prevents accidentally leaking sensitive fields

# Optional: Field-Level Validation
```
from pydantic import BaseModel, EmailStr, Field

class User(BaseModel):
    name: str = Field(..., min_length=3)
    email: EmailStr
    age: int = Field(..., ge=18, le=99)
```
min_length=3 → Name must be at least 3 characters

EmailStr → Must be a valid email

ge=18, le=99 → Age must be between 18 and 99

| Syntax                               | Meaning                                        |
| ------------------------------------ | ---------------------------------------------- |
| `Union[int, None] = None`            | Optional; valid if `int` or `None`             |
| `Optional[int] = None`               | Shorthand for `Union[int, None]`               |
| `Optional[int] = Field(None, ge=18)` | Optional with constraints                      |
| `Union[int, str, None] = None`       | Can be `int`, `str`, or `None` (very flexible) |


# Summary
| Feature                 | Benefit                                                |
| ----------------------- | ------------------------------------------------------ |
| Path operations         | Define how to handle different HTTP methods and routes |
| GET/POST/PUT/DELETE     | Clean separation of functionality                      |
| Pydantic integration    | Automatic validation for request/response data         |
| Field-level constraints | More precise control of input validation               |
| Response models         | Ensure APIs return clean, expected data                |
| Auto-generated docs     | Comes for free via OpenAPI/Swagger UI                  |


# How do you handle request validation errors in FastAPI?

FastAPI automatically handles request validation using Pydantic models and returns a clear JSON response if the validation fails.

Example:
```
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()

class User(BaseModel):
    name: str
    email: EmailStr

@app.post("/users/")
def create_user(user: User):
    return {"message": "User created", "user": user}

```

 Invalid request:
```
{
  "name": "John",
  "email": "not-an-email"
}
```
 Response:
```
{
  "detail": [
    {
      "loc": ["body", "user", "email"],
      "msg": "value is not a valid email address",
      "type": "value_error.email"
    }
  ]
}
```
 Custom error handling (optional):
```
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi import Request
from fastapi.exception_handlers import request_validation_exception_handler

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content={"custom_error": exc.errors()}
    )
```
How can you validate a specific field in a Pydantic model?
You can use Pydantic's @validator decorator to apply custom logic to a specific field.

Example:
```
from pydantic import BaseModel, validator

class Product(BaseModel):
    name: str
    price: float

    @validator('price')
    def check_price_positive(cls, value):
        if value <= 0:
            raise ValueError("Price must be greater than zero")
        return value
```
How do you handle partial updates (PATCH method) in FastAPI and validate only the updated fields?
For partial updates, you define a separate Pydantic model where all fields are optional.

Example:
```
from typing import Optional
from fastapi import FastAPI, HTTPException

app = FastAPI()

class User(BaseModel):
    name: str
    email: EmailStr
    age: int

class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    age: Optional[int] = None

fake_db = {
    1: {"name": "Alice", "email": "alice@example.com", "age": 25}
}

@app.patch("/users/{user_id}")
def update_user(user_id: int, update: UserUpdate):
    if user_id not in fake_db:
        raise HTTPException(status_code=404, detail="User not found")
    
    stored_user = fake_db[user_id]
    update_data = update.dict(exclude_unset=True)

    stored_user.update(update_data)
    return {"message": "User updated", "user": stored_user}
```
# Key Points:
exclude_unset=True: ensures only provided fields are used for update.

This approach avoids overwriting fields with None.


# 1. How do you implement pagination in FastAPI?
FastAPI supports pagination using query parameters like limit and offset or page and size.

🔹 Example (limit-offset style):
```
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
def get_items(limit: int = Query(10, ge=1), offset: int = Query(0, ge=0)):
    items = [{"id": i} for i in range(100)]  # Fake database
    return items[offset : offset + limit]
```
You can also return metadata like total count:

```
return {
    "total": len(items),
    "limit": limit,
    "offset": offset,
    "data": items[offset : offset + limit]
}
```
# 2. How can you customize exception handling in FastAPI?
Use @app.exception_handler() to define custom handlers.

🔹 Example: Custom 404 handler
```
from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse

@app.exception_handler(HTTPException)
async def custom_http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": f"Oops! {exc.detail}"},
    )
```
🔹 Example: Handle generic exceptions
```
@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"message": "Something went wrong."},
    )
```
# 3. How do you handle form data in FastAPI?
Use Form from fastapi.

🔹 Example:
```
from fastapi import Form

@app.post("/login/")
def login(username: str = Form(...), password: str = Form(...)):
    return {"username": username}
```
Form data must be sent with Content-Type: application/x-www-form-urlencoded or multipart/form-data.

# 4. How do you handle multiple query parameters in FastAPI?
Simply declare them as function parameters:

🔹 Example:
```
@app.get("/search/")
def search(q: str = "", category: str = None, page: int = 1, size: int = 10):
    return {"query": q, "category": category, "page": page, "size": size}
```
You can also receive multiple values for the same query key using List:

```
from typing import List

@app.get("/filters/")
def filters(tags: List[str] = Query([])):
    return {"tags": tags}
```
Request: /filters/?tags=books&tags=electronics

# 5. What are request and response objects in FastAPI?
Request: Contains details about the incoming HTTP request.

Response: Used to modify response headers, cookies, status codes, etc.

🔹 Import:
```
from fastapi import Request, Response
```
🔹 Example using Request:
```
@app.get("/info/")
async def get_info(request: Request):
    client_host = request.client.host
    return {"client_host": client_host}
```
🔹 Example using Response:
```
@app.get("/set-cookie/")
def set_cookie(response: Response):
    response.set_cookie(key="mycookie", value="fastapi")
    return {"message": "Cookie set"}
```
# 6. How can you validate a specific field in a Pydantic model?
Use Pydantic's @validator.

🔹 Example:
```
from pydantic import BaseModel, validator

class User(BaseModel):
    username: str
    age: int

    @validator('username')
    def username_must_be_alphanumeric(cls, v):
        if not v.isalnum():
            raise ValueError('Username must be alphanumeric')
        return v
```
You can also use root_validator to validate multiple fields together.

ChatGPT said:
Rate Limiting in FastAPI
Rate limiting helps protect your API by restricting how many requests a user or client can make in a given period of time. It’s especially important to prevent abuse and ensure fair usage of resources.

# Ways to Implement Rate Limiting in FastAPI
# 1. Using slowapi (based on limits library)
slowapi is a popular rate limiting library compatible with FastAPI.

Install it:
```
pip install slowapi
```
Example:
```
from fastapi import FastAPI, Request
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from fastapi.responses import JSONResponse
from slowapi.errors import RateLimitExceeded

app = FastAPI()

limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

@app.get("/limited")
@limiter.limit("5/minute")  # 5 requests per minute per IP
async def limited_endpoint(request: Request):
    return {"message": "This is a rate-limited endpoint"}
```

# 2. Manual Rate Limiting (Basic In-Memory for Learning)
You can implement basic rate limiting using Python dictionaries and timestamps.

```
from fastapi import FastAPI, Request, HTTPException
from datetime import datetime, timedelta

app = FastAPI()
client_requests = {}

@app.middleware("http")
async def rate_limiter(request: Request, call_next):
    ip = request.client.host
    now = datetime.utcnow()

    # Allow 3 requests per 10 seconds
    limit = 3
    window = timedelta(seconds=10)

    if ip not in client_requests:
        client_requests[ip] = []

    # Filter out old timestamps
    client_requests[ip] = [t for t in client_requests[ip] if now - t < window]

    if len(client_requests[ip]) >= limit:
        raise HTTPException(status_code=429, detail="Too many requests")

    client_requests[ip].append(now)
    response = await call_next(request)
    return response
```
# Best Practices for Rate Limiting
Use Redis for distributed environments (use limits with RedisStorage).

Set user-specific limits using API keys or authentication.

Whitelist internal IPs or trusted users.

Use exponential backoff for retries on the client side.

# Advanced: 
Using redis for distributed rate limiting
```
from slowapi import Limiter
from slowapi.storage import RedisStorage
import redis

storage = RedisStorage(redis.StrictRedis(host="localhost", port=6379, db=0))
limiter = Limiter(key_func=get_remote_address, storage=storage)
```
This way, rate limits are shared across multiple app instances or workers.


# Path Operation Configuration¶
- There are several parameters that you can pass to your path operation decorator to configure it
## 1. Response Status Code

You can define the (HTTP) status_code to be used in the response of your path operation.

```@app.post("/items/", response_model=Item, status_code=status.HTTP_201_CREATED)
```
## 2. Tags
You can add tags to your path operation, pass the parameter tags with a list of str (commonly just one str):
```
@app.post("/items/", response_model=Item, tags=["items"])
```
## 3. You can add a summary and description
## 4. Description from docstring
## 5. Response description
## 6. Deprecate a path operation
If you need to mark a path operation as deprecated, but without removing it, pass the parameter deprecated:







