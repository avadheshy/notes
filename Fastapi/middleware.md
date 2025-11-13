# FastAPI Middleware & CORS Guide

## Table of Contents
- [What Are Middleware in FastAPI?](#what-are-middleware-in-fastapi)
- [Use Cases for Middleware](#use-cases-for-middleware)
- [How to Use Middleware](#how-to-use-middleware)
- [What is CORS?](#what-is-cors)
- [How to Handle CORS in FastAPI](#how-to-handle-cors-in-fastapi)
- [Best Practices](#best-practices)

---

## What Are Middleware in FastAPI?

Middleware in FastAPI are functions that are executed **before and/or after each request**. They sit in the middle between the client request and the endpoint handling logic, allowing you to:

- Modify the request or response
- Perform logging
- Handle errors
- Apply cross-cutting concerns like authentication, CORS, or rate limiting

FastAPI uses **Starlette** under the hood, and middleware in FastAPI is powered by Starlette's middleware system.

---

## Use Cases for Middleware

- ✅ Logging request and response details
- ✅ Measuring request execution time
- ✅ Adding or validating custom headers
- ✅ Request/response transformations
- ✅ Global error handling
- ✅ Authentication/authorization
- ✅ CORS (Cross-Origin Resource Sharing)
- ✅ Rate limiting

---

## How to Use Middleware

### Creating Custom Middleware

FastAPI provides the `@app.middleware("http")` decorator to create middleware for HTTP requests.

#### Example: Logging Middleware

```python
from fastapi import FastAPI, Request
import time

app = FastAPI()

@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()
    
    response = await call_next(request)  # Call the actual endpoint
    
    duration = time.time() - start_time
    print(f"Request to {request.url.path} took {duration:.2f} seconds")
    
    return response
```

#### Example: Adding a Custom Header

```python
@app.middleware("http")
async def add_custom_header(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Custom-Header"] = "FastAPI-Middleware"
    return response
```

### Using Third-Party Middleware

You can also add middleware using `app.add_middleware()` for external or reusable classes.

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Use a whitelist in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

---

## What is CORS?

**CORS (Cross-Origin Resource Sharing)** is a security mechanism enforced by web browsers that controls how resources on a web server can be requested from another domain (origin) outside the domain from which the resource originated.

### Example Scenario

If your FastAPI backend runs at `https://api.example.com` and your frontend at `https://frontend.example.com`, a browser will block frontend JavaScript from making requests to the backend unless the backend explicitly allows it via CORS headers.

### Why Is CORS Needed?

- 🛡️ Browsers block cross-origin AJAX requests unless the server allows them
- 🛡️ Helps prevent malicious websites from reading sensitive data from another site where the user is authenticated
- 🛡️ Protects against certain types of CSRF attacks

---

## How to Handle CORS in FastAPI

FastAPI provides built-in support for CORS using the Starlette middleware.

### Basic CORS Setup

```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Define allowed origins
origins = [
    "http://localhost",
    "http://localhost:3000",
    "https://your-frontend-domain.com"
]

# Add the CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,              # List of allowed origins
    allow_credentials=True,
    allow_methods=["*"],                # HTTP methods: GET, POST, etc.
    allow_headers=["*"],                # Allowed headers like Authorization
)
```

### CORSMiddleware Parameters

| Parameter | Description |
|-----------|-------------|
| `allow_origins` | List of allowed origins (use `["*"]` to allow all — **not recommended in production**) |
| `allow_methods` | List of HTTP methods to allow (e.g., `["GET", "POST"]`) |
| `allow_headers` | List of allowed headers (e.g., `["Authorization", "Content-Type"]`) |
| `allow_credentials` | Boolean. Allows cookies or Authorization headers in cross-origin requests |
| `expose_headers` | List of headers that browsers can access on the response |
| `max_age` | How long the results of a preflight request can be cached |

---

## Best Practices

### Middleware Best Practices

- ✅ Use middleware for concerns that should be applied **globally**
- ✅ Keep middleware functions **efficient** — they run for every request
- ✅ Avoid business logic in middleware; delegate it to route handlers or dependencies
- ✅ Use dependency injection for per-route logic instead of middleware if it applies only to certain endpoints

### CORS Best Practices

- ✅ **Whitelist only trusted origins** in production
- ❌ **Do not use** `allow_origins=["*"]` with `allow_credentials=True` — browsers will block it
- ✅ For multiple environments (dev, staging, prod), use **environment-based configuration** for CORS settings

### Example: Environment-Based CORS Configuration

```python
import os

# Get environment from environment variable
environment = os.getenv("ENVIRONMENT", "development")

if environment == "production":
    origins = [
        "https://your-production-domain.com",
    ]
elif environment == "staging":
    origins = [
        "https://your-staging-domain.com",
    ]
else:
    origins = [
        "http://localhost",
        "http://localhost:3000",
        "http://localhost:8000",
    ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

---

## Summary

- **Middleware** sits between the client request and your endpoint, allowing you to process requests and responses globally
- Use the `@app.middleware("http")` decorator for custom middleware
- Use `app.add_middleware()` for third-party or reusable middleware classes
- **CORS** is essential for allowing your frontend to communicate with your backend across different origins
- Always whitelist specific origins in production and avoid using `allow_origins=["*"]` with credentials enabled