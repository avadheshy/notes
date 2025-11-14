# FastAPI Forms, Files & Static Files - Complete Guide

A comprehensive guide to handling forms, file uploads, and static files in FastAPI applications.

---

## Table of Contents
1. [Forms](#1-forms)
2. [File Uploads](#2-file-uploads)
3. [Static Files](#3-static-files)
4. [Best Practices](#4-best-practices)

---

## 1. Forms

FastAPI makes it easy to handle HTML form data using the `Form` class, which inherits directly from `Body`.

### Basic Form Handling

```python
from typing import Annotated
from fastapi import FastAPI, Form

app = FastAPI()

@app.post("/login/")
async def login(
    username: Annotated[str, Form()],
    password: Annotated[str, Form()]
):
    return {"username": username, "message": "Login successful"}
```

### Using Pydantic Models for Forms

For better organization and validation, use Pydantic models with forms:

```python
from pydantic import BaseModel, Field
from fastapi import FastAPI, Form
from typing import Annotated

class LoginForm(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    password: str = Field(..., min_length=8)
    remember_me: bool = False
    
    model_config = {"extra": "forbid"}  # Reject extra fields

@app.post("/login/")
async def login(data: Annotated[LoginForm, Form()]):
    return {"username": data.username, "status": "authenticated"}
```

**Benefits:**
- Automatic validation
- Type safety
- Clear documentation
- Reusable across endpoints
- Extra field protection with `model_config`

---

## 2. File Uploads

FastAPI provides robust file handling capabilities through the `File` and `UploadFile` classes.

### Method 1: Using `bytes` (Small Files)

Best for small files where you need the entire content in memory:

```python
from typing import Annotated
from fastapi import FastAPI, File

app = FastAPI()

@app.post("/upload-small/")
async def upload_small_file(file: Annotated[bytes, File()]):
    return {
        "size": len(file),
        "message": "File uploaded successfully"
    }
```

**Limitations:**
- Entire file loaded into memory
- Not suitable for large files
- No metadata available

### Method 2: Using `UploadFile` (Recommended)

The preferred method for most file uploads:

```python
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    contents = await file.read()
    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "size": len(contents)
    }

@app.get("/")
async def main():
    return HTMLResponse("""
    <!DOCTYPE html>
    <html>
        <head><title>File Upload</title></head>
        <body>
            <h2>Upload a File</h2>
            <form action="/upload/" enctype="multipart/form-data" method="post">
                <input name="file" type="file" required>
                <button type="submit">Upload</button>
            </form>
        </body>
    </html>
    """)
```

**UploadFile Attributes:**
- `filename`: Original file name (str)
- `content_type`: MIME type (str)
- `file`: Actual file-like object
- `read()`: Async method to read file
- `write()`: Async method to write to file
- `seek()`: Async method to move file position
- `close()`: Async method to close file

### Optional File Upload

Make file uploads optional:

```python
@app.post("/upload-optional/")
async def upload_optional_file(file: UploadFile | None = None):
    if not file:
        return {"message": "No file provided"}
    
    contents = await file.read()
    return {"filename": file.filename, "size": len(contents)}
```

### Multiple File Uploads

Handle multiple files in a single request:

```python
from typing import List

@app.post("/upload-multiple/")
async def upload_multiple_files(files: List[UploadFile] = File(...)):
    file_info = []
    
    for file in files:
        contents = await file.read()
        file_info.append({
            "filename": file.filename,
            "content_type": file.content_type,
            "size": len(contents)
        })
    
    return {"files": file_info, "total_count": len(files)}
```

### Combining Forms and Files

Upload files along with form data:

```python
@app.post("/submit-profile/")
async def submit_profile(
    name: Annotated[str, Form()],
    email: Annotated[str, Form()],
    bio: Annotated[str, Form()] = "",
    profile_picture: UploadFile = File(...)
):
    contents = await profile_picture.read()
    
    return {
        "name": name,
        "email": email,
        "bio": bio,
        "picture_filename": profile_picture.filename,
        "picture_size": len(contents)
    }
```

### Handling Large File Uploads

#### Stream Files in Chunks

Process large files efficiently without loading everything into memory:

```python
import aiofiles
from pathlib import Path

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

@app.post("/upload-large/")
async def upload_large_file(file: UploadFile = File(...)):
    file_path = UPLOAD_DIR / file.filename
    
    async with aiofiles.open(file_path, 'wb') as buffer:
        while chunk := await file.read(1024 * 1024):  # Read 1MB at a time
            await buffer.write(chunk)
    
    return {
        "filename": file.filename,
        "message": "Large file uploaded successfully",
        "path": str(file_path)
    }
```

#### Configure Server Limits

**Uvicorn:** FastAPI doesn't impose upload size limits, but your ASGI server might.

```bash
# Run with appropriate timeout settings
uvicorn main:app --timeout-keep-alive 300
```

**Nginx Configuration:**

```nginx
http {
    client_max_body_size 100M;
    client_body_timeout 300s;
}
```

### File Upload Comparison

| Feature | `bytes` | `UploadFile` |
|---------|---------|--------------|
| Memory Usage | Full file in memory | Spooled (memory → disk) |
| Large Files | ❌ Not recommended | ✅ Efficient |
| Metadata Access | ❌ No | ✅ Yes |
| Streaming | ❌ No | ✅ Yes |
| Methods | Basic | `.read()`, `.write()`, `.seek()` |
| Best For | Small files (<1MB) | All file sizes |

---

## 3. Static Files

Serve static files (CSS, JavaScript, images) directly from your FastAPI application.

### Basic Setup

```python
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Mount static files directory
app.mount("/static", StaticFiles(directory="static"), name="static")
```

**Directory Structure:**
```
project/
├── main.py
└── static/
    ├── css/
    │   └── style.css
    ├── js/
    │   └── script.js
    └── images/
        └── logo.png
```

### Accessing Static Files

Once mounted, access files via the `/static` path:

```html
<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" href="/static/css/style.css">
</head>
<body>
    <img src="/static/images/logo.png" alt="Logo">
    <script src="/static/js/script.js"></script>
</body>
</html>
```

### Multiple Static Directories

Serve multiple static directories:

```python
app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/media", StaticFiles(directory="media"), name="media")
app.mount("/downloads", StaticFiles(directory="downloads"), name="downloads")
```

### Static Files with HTML Template

Complete example serving an HTML page with static assets:

```python
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>My FastAPI App</title>
        <link rel="stylesheet" href="/static/css/style.css">
    </head>
    <body>
        <h1>Welcome to FastAPI</h1>
        <img src="/static/images/logo.png" alt="Logo">
        <script src="/static/js/app.js"></script>
    </body>
    </html>
    """
```

---

## 4. Best Practices

### File Upload Security

1. **Validate File Types**
```python
ALLOWED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".gif", ".pdf"}

@app.post("/upload-secure/")
async def upload_secure(file: UploadFile = File(...)):
    file_ext = Path(file.filename).suffix.lower()
    
    if file_ext not in ALLOWED_EXTENSIONS:
        raise HTTPException(400, f"File type {file_ext} not allowed")
    
    # Process file...
    return {"message": "File uploaded successfully"}
```

2. **Limit File Size**
```python
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB

@app.post("/upload-limited/")
async def upload_with_limit(file: UploadFile = File(...)):
    contents = await file.read()
    
    if len(contents) > MAX_FILE_SIZE:
        raise HTTPException(413, "File too large")
    
    # Process file...
    return {"message": "File uploaded"}
```

3. **Sanitize Filenames**
```python
import secrets
from pathlib import Path

def secure_filename(filename: str) -> str:
    """Generate a secure filename"""
    ext = Path(filename).suffix
    return f"{secrets.token_urlsafe(16)}{ext}"

@app.post("/upload-safe/")
async def upload_safe(file: UploadFile = File(...)):
    safe_name = secure_filename(file.filename)
    file_path = UPLOAD_DIR / safe_name
    
    async with aiofiles.open(file_path, 'wb') as buffer:
        contents = await file.read()
        await buffer.write(contents)
    
    return {"filename": safe_name}
```

### Form Validation Best Practices

```python
from pydantic import BaseModel, EmailStr, Field, validator

class RegistrationForm(BaseModel):
    username: str = Field(..., min_length=3, max_length=50, pattern="^[a-zA-Z0-9_]+$")
    email: EmailStr
    password: str = Field(..., min_length=8)
    confirm_password: str
    
    @validator('confirm_password')
    def passwords_match(cls, v, values):
        if 'password' in values and v != values['password']:
            raise ValueError('Passwords do not match')
        return v
    
    model_config = {"extra": "forbid"}
```

### Cloud Storage Integration

For production applications, consider using cloud storage:

```python
import boto3
from fastapi import FastAPI, UploadFile, File

s3_client = boto3.client('s3')
BUCKET_NAME = "my-app-uploads"

@app.post("/upload-to-s3/")
async def upload_to_s3(file: UploadFile = File(...)):
    contents = await file.read()
    
    # Upload to S3
    s3_client.put_object(
        Bucket=BUCKET_NAME,
        Key=file.filename,
        Body=contents,
        ContentType=file.content_type
    )
    
    return {
        "message": "File uploaded to S3",
        "filename": file.filename
    }
```

### Error Handling

```python
from fastapi import HTTPException

@app.post("/upload-with-errors/")
async def upload_with_error_handling(file: UploadFile = File(...)):
    try:
        # Validate file
        if not file.filename:
            raise HTTPException(400, "No filename provided")
        
        # Read and process
        contents = await file.read()
        
        if len(contents) == 0:
            raise HTTPException(400, "Empty file")
        
        # Save file logic here...
        
        return {"message": "Success", "filename": file.filename}
        
    except Exception as e:
        raise HTTPException(500, f"Upload failed: {str(e)}")
```

---

## Quick Reference

### Import Checklist
```python
from typing import Annotated, List
from fastapi import FastAPI, File, Form, UploadFile, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import aiofiles
```

### Common Patterns

**Single file upload:**
```python
async def upload(file: UploadFile = File(...))
```

**Multiple files:**
```python
async def upload(files: List[UploadFile] = File(...))
```

**Form with file:**
```python
async def submit(name: Annotated[str, Form()], file: UploadFile = File(...))
```

**Static files:**
```python
app.mount("/static", StaticFiles(directory="static"), name="static")
```

---

## Additional Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [Starlette Documentation](https://www.starlette.io/) (FastAPI's foundation)

---

**Last Updated:** November 2025