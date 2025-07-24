# 1. WebSockets: Concept and Use Cases
##  What are WebSockets?
WebSockets provide a full-duplex communication channel over a single TCP connection. Unlike HTTP, which is request-response, WebSockets enable real-time bidirectional communication between client and server.

# Use Cases:
- Chat applications

- Real-time notifications

- Live dashboards/analytics

- Online multiplayer games

- Collaborative editing tools (e.g., Google Docs)

# 2. Implementing WebSockets in FastAPI
FastAPI supports WebSockets using its built-in WebSocket class.

Example:
```
from fastapi import FastAPI, WebSocket, WebSocketDisconnect

app = FastAPI()

@app.websocket("/ws/chat")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"Message text was: {data}")
    except WebSocketDisconnect:
        print("Client disconnected")
```
 Test with JavaScript in browser console:
```
let ws = new WebSocket("ws://localhost:8000/ws/chat");
ws.onmessage = (e) => console.log(e.data);
ws.send("Hello FastAPI");
```
# 3. WebSocket: Challenges and Best Practices
#  Challenges:
- No built-in user/session authentication

- Harder to scale across multiple processes/servers

- State management (rooms, users)

- Disconnection handling

# Best Practices:
- Authenticate user on connection (e.g., via query token or cookie)

- Use try/except to gracefully handle WebSocketDisconnect

- Maintain a connection manager to handle rooms and clients

- Consider using message brokers (e.g., Redis Pub/Sub) for scalability

- Implement ping/pong heartbeats for client liveness

# 4. Background Tasks: Concept and Use Cases
##  What are Background Tasks?
Tasks that are executed after returning a response. They allow FastAPI to return responses quickly while deferring non-critical work.

# Use Cases:
- Sending confirmation emails

- Logging or analytics

- Cleanup tasks

- Sending notifications

#  5. Creating Background Tasks in FastAPI
FastAPI provides a simple BackgroundTasks dependency.

```
from fastapi import FastAPI, BackgroundTasks

app = FastAPI()

def send_email_notification(email: str):
    # Simulate sending email
    print(f"Sending email to {email}")

@app.post("/register/")
def register_user(email: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(send_email_notification, email)
    return {"message": f"User registered, email will be sent to {email}"}
```
# How it works:
```
add_task() schedules the function to run after sending the response.
```

# 6. Best Practices for Background Tasks
- Avoid long-running tasks in FastAPI's built-in background tasks (prefer Celery for that)

- Ensure tasks are idempotent (can be retried safely)

- Use logging inside tasks to monitor failures

- Be aware of server shutdowns – tasks may not complete

- For reliability & retries, prefer Celery + Redis/RabbitMQ

# 7. Securing WebSockets and Background Tasks
WebSocket Security:

Authenticate on connect:

```
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket, token: str = Query(...)):
    user = verify_token(token)
    if not user:
        await websocket.close()
        return
    await websocket.accept()
```
Use JWT tokens or session cookies

Avoid exposing sensitive data over unsecured channels (use wss:// in prod)

Disconnect inactive clients

# Background Task Security:
- Ensure only authorized users can trigger endpoints that start background tasks

- Validate inputs before adding tasks

- Use per-user rate limits or throttling

