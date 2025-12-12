# Security Considerations in FastAPI Development
Security is critical when building APIs. FastAPI provides built-in tools to address many common security requirements.

Key Considerations:
Authentication and Authorization
Verify user identity (authentication) and restrict access based on permissions (authorization).

Data Validation
Prevent injection attacks or malformed data using Pydantic models.

HTTPS Enforcement
Always deploy FastAPI with HTTPS in production.

Rate Limiting
Prevent abuse of endpoints via rate-limiting strategies.

Input Sanitization
Sanitize user inputs to protect against XSS and SQL injection.

CORS Configuration
Use CORS middleware to restrict resource access from unauthorized origins.

# Security Features in FastAPI (with Examples)
1. HTTP Basic Authentication
```
from fastapi import FastAPI, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials

app = FastAPI()
security = HTTPBasic()

@app.get("/secure-data/")
def read_secure_data(credentials: HTTPBasicCredentials = Depends(security)):
    return {"username": credentials.username}
```
2. OAuth2 with Password and Bearer
```
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
app = FastAPI()

@app.get("/users/me")
async def read_users_me(token: str = Depends(oauth2_scheme)):
    return {"token": token}
```
# Securing FastAPI Endpoints with OAuth2
Overview:
FastAPI supports OAuth2 flows using OAuth2PasswordBearer for token-based authentication.

Steps to Secure Endpoints:
Create a Token Endpoint:

```
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta

app = FastAPI()

@app.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    if form_data.username == "admin" and form_data.password == "secret":
        return {"access_token": form_data.username, "token_type": "bearer"}
    raise HTTPException(status_code=400, detail="Incorrect username or password")
```
Use Token in Protected Routes:

```
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.get("/secure-info/")
async def secure_info(token: str = Depends(oauth2_scheme)):
    if token != "admin":
        raise HTTPException(status_code=403, detail="Unauthorized")
    return {"message": "Secure content"}
```
#  Best Practices for Security in FastAPI
Use OAuth2 or JWT for authentication.

Always hash passwords (e.g., with bcrypt) before storing them.

Validate all input data using Pydantic models.

Use Depends to apply reusable authentication logic.

Enable CORS only for trusted domains using CORSMiddleware.

Deploy behind HTTPS with proper certificates (e.g., using Nginx or a proxy).

Oauth2
Oauth1
OpenID Connect¶
OpenID (not "OpenID Connect")
OpenAPI
what is the difference between decoding/hashing/signing
root path