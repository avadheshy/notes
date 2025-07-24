# How Do You Upload Files in FastAPI?
FastAPI provides powerful and easy-to-use tools for handling file uploads using the File class from fastapi.

 Basic File Upload Example
```
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
UploadFile: A class that provides file metadata and an internal file-like object.

File(...): Used to declare a file parameter in a request.

# Upload Multiple Files
```
from typing import List

@app.post("/upload-multiple/")
async def upload_multiple_files(files: List[UploadFile] = File(...)):
    return [{"filename": file.filename} for file in files]
```
# Difference Between UploadFile and bytes
```
Type	        Behavior
UploadFile	    Efficient, uses spooled temporary files, supports .file, .read(), .write(), .seek()
bytes	        Loads entire content into memory, not recommended for large files
```

# How Do You Handle Large File Uploads in FastAPI?
1.  Use UploadFile Instead of bytes
UploadFile stores file contents in memory only if small, else stores them in a temporary file on disk, which is ideal for large files.

2.  Stream File Contents in Chunks
You can read large files in chunks to avoid memory overuse:

```
@app.post("/upload-stream/")
async def upload_large_file(file: UploadFile = File(...)):
    with open(f"/tmp/{file.filename}", "wb") as buffer:
        while chunk := await file.read(1024 * 1024):  # Read in 1MB chunks
            buffer.write(chunk)
    return {"message": "File saved"}
```
3.  Increase Default Upload Size Limits (Uvicorn/NGINX/etc.)
FastAPI itself doesn’t limit upload size, but the ASGI server (like Uvicorn) or proxy (like Nginx) might.

Example: Uvicorn
Use --limit-concurrency and --timeout-keep-alive if needed, but file size is mostly limited by reverse proxy:

Example: Nginx Configuration
```
client_max_body_size 100M;
```
# Best Practices
Validate the file type and size.

Store files using secure names (avoid direct file.filename usage).

Use cloud storage (S3, GCS) for very large files.

Apply authentication and authorization to upload endpoints.