# What is JWT?
JWT (JSON Web Token) is a compact and self-contained way to securely transmit information between parties as a JSON object. Commonly used for authentication and authorization.

 FastAPI JWT Authentication Flow
User logs in with credentials

If valid, return a signed JWT access token

Use token for protected routes

Token is verified on each request

# Libraries Required
```
pip install fastapi[all] python-jose[cryptography] passlib[bcrypt]
```
# Step-by-Step Implementation
1. Setup Settings and Secret Key
```
# config.py
SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
```
2.  Utility for JWT Token Creation & Verification
```
# auth.py
from datetime import datetime, timedelta
from jose import JWTError, jwt
from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload  # e.g., {'sub': username}
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
            headers={"WWW-Authenticate": "Bearer"},
        )
```
3.  Password Hashing
```
# utils.py
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain, hashed):
    return pwd_context.verify(plain, hashed)

def hash_password(password):
    return pwd_context.hash(password)
```
4.  Token Request & Login Route
```
# main.py
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from auth import create_access_token, verify_token, oauth2_scheme
from utils import verify_password
from pydantic import BaseModel
from datetime import timedelta

app = FastAPI()

# Dummy user DB
fake_users_db = {
    "john": {"username": "john", "hashed_password": "$2b$12$hashed_here"}
}

class Token(BaseModel):
    access_token: str
    token_type: str

@app.post("/token", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = fake_users_db.get(form_data.username)
    if not user or not verify_password(form_data.password, user["hashed_password"]):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    access_token = create_access_token(
        data={"sub": user["username"]},
        expires_delta=timedelta(minutes=30)
    )
    return {"access_token": access_token, "token_type": "bearer"}
```
5.  Protected Route (Require JWT)
```
@app.get("/secure-data")
def secure_route(token: str = Depends(oauth2_scheme)):
    payload = verify_token(token)
    return {"msg": f"Welcome {payload['sub']}"}
```
# Full Flow Summary
| Step                   | Endpoint      | Details                             |
| ---------------------- | ------------- | ----------------------------------- |
| Login                  | `POST /token` | Use `OAuth2PasswordRequestForm`     |
| Get Access Token       | → response    | Contains JWT                        |
| Authenticated Requests | Any route     | Use `Authorization: Bearer <token>` |
| Verify & Decode Token  | In `Depends`  | Use `verify_token()`                |


# Optional: Refresh Tokens
You can extend this by issuing:

Short-lived access tokens

Long-lived refresh tokens for renewal

# Good Practices
Use HTTPS in production

Store secrets securely

Set appropriate exp, iat, nbf claims

Use sub for user identification