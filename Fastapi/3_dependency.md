#  Dependency Injection in FastAPI

Dependency Injection (DI) is one of the **core features** of FastAPI that promotes **clean code**, **modularity**, and **easy testing**.

---

##  What is Dependency Injection?

> **Dependency Injection (DI)** is a design pattern where required resources (dependencies) are provided to a function rather than created within it.

In FastAPI, you declare dependencies using the `Depends()` function, and FastAPI takes care of **resolving** and **injecting** them automatically.

---

##  Benefits of Dependency Injection

| Benefit              | Description                                                   |
|----------------------|---------------------------------------------------------------|
|  Clean Code        | Avoids duplication, separates concerns                        |
|  Reusability       | Shared logic (e.g., DB connection, authentication) is reusable |
|  Easier Testing     | Dependencies can be easily overridden during tests            |
|  Modularity        | Keeps route functions focused on business logic               |

---

##  Example: Using Dependency Injection in FastAPI

### Step 1: Create Dependencies

####  Database Session Dependency
```
from fastapi import Depends

def get_db():
    db = DBSession()  # your database session factory
    try:
        yield db
    finally:
        db.close()
```
# Authentication Dependency
```
from fastapi import HTTPException, status

def get_current_user(token: str = Depends(oauth2_scheme)):
    user = verify_token(token)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return user

```
# Step 2: Use Dependencies in Routes
```
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

app = FastAPI()

@app.get("/users/me")
def read_users_me(
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    return {"user": current_user}
```
#  What FastAPI Does Automatically
Resolves dependencies like get_db() and get_current_user()

Injects required values into the route handler

Manages the lifecycle (e.g., closing DB sessions)

#  How It Simplifies Testing
FastAPI allows you to override dependencies for testing:

```
from fastapi.testclient import TestClient

def override_get_db():
    yield TestDBSession()

def override_get_current_user():
    return {"id": 123, "name": "Test User"}

app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user

client = TestClient(app)

def test_read_users_me():
    response = client.get("/users/me")
    assert response.json() == {"user": {"id": 123, "name": "Test User"}}
```
# Summary
| Feature               | Benefit                                      |
| --------------------- | -------------------------------------------- |
| **Reusable logic**    | Centralize shared operations like DB or auth |
| **Clean endpoints**   | Routes focus only on business logic          |
| **Test-friendly**     | Easily inject mocks/fakes during tests       |
| **Managed lifecycle** | Auto-close DB sessions, etc.                 |


# What is the Purpose of Depends()?
Depends() tells FastAPI what external logic to execute and inject the result into your endpoint or function.

It can be used for:

DB sessions

Auth checks

Configuration access

Custom logic (e.g., logging, caching)

Example: Using Dependency Injection in FastAPI
Step 1: Create Dependencies

 Database Session Dependency
```
from fastapi import Depends

def get_db():
    db = DBSession()  # Your database session factory (e.g., SQLAlchemy)
    try:
        yield db
    finally:
        db.close()
```
 Authentication Dependency
```
from fastapi import HTTPException, status

def get_current_user(token: str = Depends(oauth2_scheme)):
    user = verify_token(token)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return user
```
Step 2: Use Dependencies in Routes
```
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

app = FastAPI()

@app.get("/users/me")
def read_users_me(
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    return {"user": current_user}
```
# Global Dependencies
To apply a dependency globally (e.g., logging, auth), use the dependencies parameter when creating the FastAPI app:

```
app = FastAPI(dependencies=[Depends(some_dependency)])
```
This will apply some_dependency to all routes.

# Asynchronous Dependencies

You can use async def for async dependencies:

```
async def get_data_from_cache():
    result = await redis.get("some_key")
    return result

@app.get("/")
async def home(data=Depends(get_data_from_cache)):
    return {"data": data}
```
FastAPI supports both def and async def in dependencies.

# How Do You Manage Database Connections?
You manage DB sessions (like SQLAlchemy) with dependencies:

```
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```
FastAPI handles opening and closing DB connections cleanly per request.

In production, consider using connection pooling (e.g., SQLAlchemy engine with pool_pre_ping=True).

# How It Simplifies Testing
FastAPI allows overriding dependencies during tests:

```
from fastapi.testclient import TestClient

def override_get_db():
    yield TestDBSession()

def override_get_current_user():
    return {"id": 123, "name": "Test User"}

app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user

client = TestClient(app)

def test_read_users_me():
    response = client.get("/users/me")
    assert response.json() == {"user": {"id": 123, "name": "Test User"}}

```
# Summary
| Feature               | Benefit                                      |
| --------------------- | -------------------------------------------- |
| **Reusable logic**    | Centralize shared operations like DB/auth    |
| **Clean endpoints**   | Routes focus only on business logic          |
| **Test-friendly**     | Easily inject mocks/fakes during tests       |
| **Managed lifecycle** | Auto-close DB sessions, etc.                 |
| **Global scope**      | Apply dependencies across all routes         |
| **Async ready**       | Seamlessly supports `async def` dependencies |
