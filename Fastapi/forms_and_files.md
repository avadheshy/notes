# FastAPI Forms, Files & Static Files Guide

## 1. Forms

Create form parameters the same way you would for Body or Query:

```python
from fastapi import FastAPI, Form

async def login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
    pass
```

### Using Pydantic Models for Forms

You can use Pydantic models to declare form fields in FastAPI:

```python
class FormData(BaseModel):
    username: str
    password: str
    model_config = {"extra": "forbid"}  # If a client tries to send extra data, they will receive an error response

async def login(data: Annotated[FormData, Form()]):
    pass
```

---

## 2. Files

### How Do You Upload Files in FastAPI?

FastAPI provides powerful and easy-to-use tools for handling file uploads using the `File` class from `fastapi`.

Create file parameters the same way you would for Body or Form.

### Using bytes

If you declare the type of your path operation function parameter as `bytes`, FastAPI will read the file for you and you will receive the contents as bytes. Keep in mind that the whole contents will be stored in memory. This will work well for small files.

```python
async def create_file(file: Annotated[bytes, File()]):
    pass
```

### Basic File Upload Example

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
def main():
    return HTMLResponse("""
    <form action="/upload/" enctype="multipart/form-data" method="post">
    <input name="file" type="file">
    <input type="submit">
    </form>
    """)
```

**Key Components:**
- `UploadFile`: A class that provides file metadata and an internal file-like object
- `File(...)`: Used to declare a file parameter in a request

### Upload Multiple Files

```python
from typing import List

@app.post("/upload-multiple/")
async def upload_multiple_files(files: List[UploadFile] = File(...)):
    return [{"filename": file.filename} for file in files]
```

### Difference Between UploadFile and bytes

| Type | Behavior |
|------|----------|
| `UploadFile` | Efficient, uses spooled temporary files, supports `.file`, `.read()`, `.write()`, `.seek()` |
| `bytes` | Loads entire content into memory, not recommended for large files |

---

## How Do You Handle Large File Uploads in FastAPI?

### 1. Use UploadFile Instead of bytes

`UploadFile` stores file contents in memory only if small, else stores them in a temporary file on disk, which is ideal for large files.

### 2. Stream File Contents in Chunks

You can read large files in chunks to avoid memory overuse:

```python
@app.post("/upload-stream/")
async def upload_large_file(file: UploadFile = File(...)):
    with open(f"/tmp/{file.filename}", "wb") as buffer:
        while chunk := await file.read(1024 * 1024):  # Read in 1MB chunks
            buffer.write(chunk)
    return {"message": "File saved"}
```

### 3. Increase Default Upload Size Limits

FastAPI itself doesn't limit upload size, but the ASGI server (like Uvicorn) or proxy (like Nginx) might.

**Example: Uvicorn**

Use `--limit-concurrency` and `--timeout-keep-alive` if needed, but file size is mostly limited by reverse proxy.

**Example: Nginx Configuration**

```nginx
client_max_body_size 100M;
```

### Best Practices

- Validate the file type and size
- Store files using secure names (avoid direct `file.filename` usage)
- Use cloud storage (S3, GCS) for very large files
- Apply authentication and authorization to upload endpoints
- You can define files and form fields at the same time using `File` and `Form`

---

## 3. Static Files

You can serve static files automatically from a directory using `StaticFiles`.

### Steps:
1. Import `StaticFiles`
2. "Mount" a `StaticFiles()` instance in a specific path

```python
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
```

**Explanation:**
- The first `"/static"` refers to the sub-path this "sub-application" will be "mounted" on. So, any path that starts with `"/static"` will be handled by it
- The `directory="static"` refers to the name of the directory that contains your static files
- The `name="static"` gives it a name that can be used internally by FastAPI