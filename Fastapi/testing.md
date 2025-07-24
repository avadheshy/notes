# Importance of Testing in FastAPI Development
Testing ensures:

Your app behaves correctly as it evolves.

Faster feedback during development.

Prevention of regressions and bugs.

Confidence during refactoring or adding new features.

FastAPI supports both sync and async testing and integrates well with pytest, httpx, and TestClient.

# Unit vs Integration Testing in FastAPI
🔹 Unit Tests
Focus on individual functions or logic.

Avoid I/O (e.g., DB or network calls).

Fast and isolated.

🔹 Integration Tests
Test full API flow (routing, DB, dependencies).

Use TestClient or httpx.AsyncClient.

Ensure components work together correctly.

🚀 Example: Simple FastAPI App
```
# main.py
from fastapi import FastAPI, Depends

app = FastAPI()

def get_greeting():
    return "Hello, Avadhesh!"

@app.get("/greet")
def greet(msg: str = Depends(get_greeting)):
    return {"message": msg}
```
# 1. Unit Testing Example
```
# test_unit.py
from main import get_greeting

def test_get_greeting():
    assert get_greeting() == "Hello, Avadhesh!"
```
# 2. Integration Testing with TestClient
```
# test_integration.py
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_greet_endpoint():
    response = client.get("/greet")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, Avadhesh!"}
```
# 3. Dependency Overrides for Testing
```
# test_override.py
from main import app
from fastapi.testclient import TestClient

def override_greeting():
    return "Hello from test!"

app.dependency_overrides[app.dependency_overrides.keys()[0]] = override_greeting

client = TestClient(app)

def test_override():
    response = client.get("/greet")
    assert response.json() == {"message": "Hello from test!"}
```
Or more generally:

```
app.dependency_overrides[get_greeting] = override_greeting
```
# 4. Mocking External Dependencies
Suppose you call an external API in a dependency:

```
# main.py
import httpx

async def fetch_data():
    async with httpx.AsyncClient() as client:
        res = await client.get("https://api.example.com/data")
        return res.json()

@app.get("/external")
async def get_external(data: dict = Depends(fetch_data)):
    return {"fetched": data}
```
Mock it in tests:

```
# test_mock.py
import pytest
from httpx import Response
from fastapi.testclient import TestClient
from main import app, fetch_data

async def mock_fetch_data():
    return {"mocked": True}

app.dependency_overrides[fetch_data] = mock_fetch_data

client = TestClient(app)

def test_external_mocked():
    res = client.get("/external")
    assert res.json() == {"fetched": {"mocked": True}}
```
5. Testing Async Endpoints with httpx + pytest-asyncio
Install first:

```
pip install httpx pytest pytest-asyncio
```
```
# test_async.py
import pytest
from httpx import AsyncClient
from main import app

@pytest.mark.asyncio
async def test_async_endpoint():
    async with AsyncClient(app=app, base_url="http://test") as client:
        res = await client.get("/greet")
        assert res.status_code == 200
        assert res.json() == {"message": "Hello, Avadhesh!"}
```
# Best Practices for Testing FastAPI
- Use TestClient for sync testing, and httpx.AsyncClient for async routes.
- Isolate logic for easier unit testing.
- Use dependency overrides to inject fake or mock implementations.
- Mock external services (e.g., DBs, APIs) using tools like unittest.mock, pytest-mock, or custom functions.
-  Use pytest fixtures to manage test setup/teardown.
- Use in-memory databases (like SQLite in-memory) for integration testing.

# Example of Fixture + Dependency Override with Database
```
# test_with_fixture.py
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main import app, get_db, Base

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
```
# Override DB
```
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

@pytest.fixture(scope="module")
def client():
    Base.metadata.create_all(bind=engine)
    with TestClient(app) as c:
        yield c
    Base.metadata.drop_all(bind=engine)
```
