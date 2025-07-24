# 1. How does FastAPI compare to Flask or Django REST Framework (DRF) in terms of performance and architecture?

| Feature           | FastAPI                    | Flask                  | Django REST Framework       |
| ----------------- | -------------------------- | ---------------------- | --------------------------- |
| **Performance**   | Very high (async/await)    | Lower (sync)           | Lower (sync, ORM overhead)  |
| **Type Hints**    | First-class support        | Optional               | Limited                     |
| **Validation**    | Pydantic-based             | Manual or Marshmallow  | DRF serializers             |
| **Async Support** | Native (Starlette)         | Third-party extensions | Some async support          |
| **Architecture**  | Lightweight, modular       | Lightweight, minimal   | Heavy, batteries included   |
| **Docs**          | Auto-generated via OpenAPI | Manual with plugins    | Automatic via Browsable API |


# 2. What are startup and shutdown events in FastAPI?
FastAPI provides hooks to run logic when the app starts or stops:

```
from fastapi import FastAPI

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    # e.g., connect to DB, load models
    pass

@app.on_event("shutdown")
async def shutdown_event():
    # e.g., close DB connection
    pass
```
# 3. How do you implement dependency overrides in FastAPI (e.g., during testing)?
Use app.dependency_overrides to replace dependencies in tests:

```
def override_get_db():
    return TestingSessionLocal()

app.dependency_overrides[get_db] = override_get_db
```
# 4. What is response_model_exclude_unset, and when should it be used?
Usage: Return only the fields that were explicitly set.

Example:

```
@app.get("/user", response_model=User, response_model_exclude_unset=True)
def get_user():
    return user_instance  # Fields not set by user will be excluded
```
Useful for PATCH or sparse updates.

# 5. How do you implement custom request and response classes?
Streaming Response:

```
from fastapi.responses import StreamingResponse

def iter_file():
    yield from open("large_file.txt", mode="rb")

@app.get("/download")
def download():
    return StreamingResponse(iter_file(), media_type="application/octet-stream")
```
Custom JSON Response:

```
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

@app.get("/custom")
def custom():
    data = {"value": "x"}
    return JSONResponse(content=jsonable_encoder(data), status_code=200)
```
# 6. How does FastAPI handle type hinting for path/query/body/header/cookie parameters?
FastAPI introspects type hints using Python’s typing and FastAPI’s dependency injection system.

Examples:
```
@app.get("/items/{id}")
def read_item(id: int, q: Optional[str] = None, user_agent: str = Header(...)):
    pass
```
Internally:

Uses inspect and typing.get_type_hints

Constructs dependencies dynamically using Depends

# 7. How can you share global variables or singletons (e.g., DB connections) in FastAPI apps safely?
Use a dependency that returns a singleton or store them during startup.

Option A – Singleton Pattern:

```
@app.on_event("startup")
def startup():
    app.state.db = create_db()

@app.get("/")
def read(db=Depends(lambda: app.state.db)):
    ...
```
Option B – Lifespan Event:

```
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.db = create_db()
    yield
    app.state.db.close()

app = FastAPI(lifespan=lifespan)
```
# 1. How would you enforce API versioning in FastAPI?
Option A: URL Path Versioning

```
@app.get("/v1/items/")
def get_v1():
    ...

@app.get("/v2/items/")
def get_v2():
    ...
```
Option B: Header Versioning

```
@app.get("/items/")
def get_items(x_api_version: str = Header(...)):
    if x_api_version == "1":
        ...
    elif x_api_version == "2":
        ...
```
# 1. How can you handle schema evolution or breaking changes in Pydantic models over time?
Best Practices:

Use versioned models: UserV1, UserV2

Deprecate fields using deprecated metadata (in OpenAPI)

Use Union for backward compatibility

```
class UserV1(BaseModel):
    name: str

class UserV2(BaseModel):
    name: str
    age: int

@app.post("/user")
def create_user(user: Union[UserV1, UserV2]):
    ...
```
# 10. How do you handle partial updates (PATCH method) in FastAPI and validate only the updated fields?
Use optional fields in a separate schema:

```
class UserUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None

@app.patch("/user/{user_id}")
def update_user(user_id: int, update: UserUpdate):
    user = get_user_from_db(user_id)
    update_data = update.dict(exclude_unset=True)
    for k, v in update_data.items():
        setattr(user, k, v)
    save(user)
    return user

```

# 1. How do you mock external dependencies in FastAPI tests using TestClient?
You can override dependencies using app.dependency_overrides.

Example:

```
from fastapi.testclient import TestClient
from main import app, get_db

def override_get_db():
    yield {"mocked": "db"}

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
```
#  2. How do you use httpx and pytest-asyncio for testing async FastAPI endpoints?
httpx.AsyncClient with pytest-asyncio allows async testing.

Example:

```
import pytest
from httpx import AsyncClient
from main import app

@pytest.mark.asyncio
async def test_read_root():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/")
    assert response.status_code == 200
```
# 3. How would you set up a CI/CD pipeline for a FastAPI project (e.g., with GitHub Actions)?
GitHub Actions Workflow: .github/workflows/ci.yml

```
name: FastAPI CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    services:
      postgres:
        image: postgres:13
        env:
          POSTGRES_USER: testuser
          POSTGRES_PASSWORD: testpass
          POSTGRES_DB: testdb
        ports: ["5432:5432"]
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5

    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: "3.10"

    - name: Install dependencies
      run: |
        pip install -r requirements.txt
        pip install pytest httpx pytest-asyncio

    - name: Run Tests
      run: pytest
```
# 4. What deployment strategies do you recommend for production FastAPI apps?
Recommended Stack:

Uvicorn (ASGI server) behind

Gunicorn (process manager) behind

Nginx (reverse proxy)

Run with Gunicorn + Uvicorn workers:

```
gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker
```
Nginx reverse proxy sample:

nginx
```
server {
    listen 80;
    server_name yourdomain.com;

    location / {
        proxy_pass http://localhost:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```
📊 5. How do you enable logging and monitor FastAPI APIs in production?
Logging setup in main.py:

```
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)
```
Monitoring tools:

Prometheus + Grafana (metrics)

Sentry (exception tracking)

NewRelic / Datadog / Elastic APM (performance monitoring)

Health Checks via FastAPI route:

```
@app.get("/health")
def health_check():
    return {"status": "ok"}
```

# 1. How do you manage environment-based settings (e.g., dotenv, Pydantic Settings Management)?
FastAPI leverages Pydantic to manage environment-based configuration elegantly.

Using pydantic.BaseSettings:
```
# config.py
from pydantic import BaseSettings

class Settings(BaseSettings):
    database_url: str
    secret_key: str
    debug: bool = False

    class Config:
        env_file = ".env"

settings = Settings()
```
Using .env:
ini
```
# .env
DATABASE_URL=sqlite:///./test.db
SECRET_KEY=mysecretkey
DEBUG=True
```
Usage in FastAPI app:
```
from fastapi import FastAPI
from config import settings

app = FastAPI()

@app.get("/info")
def get_info():
    return {
        "debug": settings.debug,
        "db": settings.database_url
    }
```
# Benefits:

Type-safe environment configuration.

Easily switch between .env files in different environments (dev, staging, prod).

Supports dotenv, system env vars, and more.

# 2. How do you implement refresh tokens and access token rotation with JWT in FastAPI?
Concept:
Access Token: Short-lived token used to access protected routes.

Refresh Token: Long-lived token used to get a new access token when it expires.

Typical Workflow:
Login → Issue access token (e.g., 15 mins) and refresh token (e.g., 7 days).

Store refresh token securely (e.g., HTTP-only cookie).

On access token expiration, client calls refresh endpoint.

Server verifies refresh token and issues new access token (and optionally a new refresh token).

Implementation Sample:
```
from datetime import datetime, timedelta
from jose import jwt, JWTError

SECRET_KEY = "supersecret"
ALGORITHM = "HS256"
ACCESS_EXPIRE_MINUTES = 15
REFRESH_EXPIRE_DAYS = 7

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def create_refresh_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(days=REFRESH_EXPIRE_DAYS)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
Refresh endpoint:

@app.post("/token/refresh")
def refresh_token(refresh_token: str = Form(...)):
    try:
        payload = jwt.decode(refresh_token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("sub")
        new_access_token = create_access_token({"sub": user_id})
        return {"access_token": new_access_token}
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid refresh token")
```
# Best practices:

Rotate refresh tokens: issue a new one every time it's used.

Invalidate old tokens on server if you store them (e.g., Redis).

Secure refresh token via HTTP-only cookies.

# 3. What are scopes in OAuth2, and how can FastAPI enforce them per route?
Concept:
Scopes define levels of access.

Example: ["read", "write", "admin"]

Declare Scopes:
```
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token", scopes={
    "read": "Read access",
    "write": "Write access",
    "admin": "Admin access"
})
```
Token with scopes:
```
def create_access_token(data: dict, scopes: list):
    data.update({"scopes": scopes})
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
```
Dependency to validate scopes:
```
from fastapi import Security, Depends, HTTPException
from fastapi.security import SecurityScopes

async def get_current_user(
    security_scopes: SecurityScopes,
    token: str = Depends(oauth2_scheme)
):
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    token_scopes = payload.get("scopes", [])

    for scope in security_scopes.scopes:
        if scope not in token_scopes:
            raise HTTPException(status_code=403, detail="Not enough permissions")
    return payload
```
Secure routes with scopes:
```
@app.get("/users/me", dependencies=[Security(get_current_user, scopes=["read"])])
async def read_me():
    return {"msg": "You're allowed to read!"}
```
# Best practices:

Keep scopes granular (read:products, write:orders, etc.).

Enforce them with SecurityScopes and Security() dependency.

Combine with role-based access control if needed.



# 1. How do you customize the OpenAPI schema or documentation UI in FastAPI?
✅ FastAPI uses Swagger UI and ReDoc by default.
You can customize both the OpenAPI schema and the docs UI in several ways:

A. Customizing metadata:
```
from fastapi import FastAPI

app = FastAPI(
    title="My API",
    description="Custom API with Swagger UI",
    version="2.0.0",
    contact={
        "name": "Avadhesh Yadav",
        "email": "avadhesh@example.com"
    },
    docs_url="/documentation",  # Custom URL
    redoc_url=None  # Disable ReDoc
)
```
B. Adding custom tags for grouping endpoints:
```
@app.get("/items/", tags=["Items"])
def read_items():
    return {"msg": "Items"}
```
C. Custom OpenAPI schema:
```
from fastapi.openapi.utils import get_openapi

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Custom Title",
        version="1.0.0",
        description="Custom description",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi
```
1. How would you implement multi-tenancy in FastAPI?
There are two main strategies:

✅ A. Subdomain-based tenancy (e.g., tenant1.example.com)
Use middleware to parse subdomain and determine tenant:

```
from starlette.middleware.base import BaseHTTPMiddleware

class TenantMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        host = request.headers.get("host")
        tenant = host.split(".")[0]  # Extract tenant
        request.state.tenant = tenant
        response = await call_next(request)
        return response

app.add_middleware(TenantMiddleware)
```
Then in views:

```
@app.get("/data/")
def get_data(request: Request):
    return {"tenant": request.state.tenant}
```
✅ B. Schema-based or DB-per-tenant strategy
Use SQLAlchemy session factories per tenant (schema or DB).

Choose the right DB connection based on user/tenant.

Example:

```
def get_db(request: Request):
    tenant = request.state.tenant
    session = SessionLocal(tenant=tenant)
    try:
        yield session
    finally:
        session.close()
```
1. How do you version your OpenAPI documentation and avoid breaking client contracts?

 A. Route prefixing
```
v1 = FastAPI(openapi_prefix="/v1")
v2 = FastAPI(openapi_prefix="/v2")

@v1.get("/users")
def get_users_v1():
    return [{"id": 1}]

@v2.get("/users")
def get_users_v2():
    return [{"id": 1, "name": "John"}]

app.mount("/v1", v1)
app.mount("/v2", v2)
```
 B. Manual OpenAPI separation
You can provide multiple OpenAPI JSON endpoints for different versions using the FastAPI(openapi_url=...) option.

# Best Practices:
Don’t remove fields (deprecate first).

Add deprecated=True in path operations:

```
@app.get("/old-endpoint", deprecated=True)
```
Use clear versioning in API URLs and schemas.

# 1. Can FastAPI be used with GraphQL? How?
Yes, via the graphene or strawberry libraries.

A. Using graphene
```
pip install graphene
```
```
import graphene
from starlette.graphql import GraphQLApp
from fastapi import FastAPI

class Query(graphene.ObjectType):
    hello = graphene.String()

    def resolve_hello(self, info):
        return "Hello from GraphQL!"

app = FastAPI()
app.add_route("/graphql", GraphQLApp(schema=graphene.Schema(query=Query)))
```
Note: starlette.graphql is deprecated. Use strawberry for modern GraphQL in FastAPI.

B. Using strawberry (Recommended)
```
pip install strawberry-graphql

import strawberry
from strawberry.fastapi import GraphQLRouter
from fastapi import FastAPI

@strawberry.type
class Query:
    @strawberry.field
    def hello(self) -> str:
        return "Hello World"

schema = strawberry.Schema(query=Query)
graphql_app = GraphQLRouter(schema)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")
```