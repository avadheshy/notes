Heres a detailed guide covering Django's async support, caching, Celery, and Django Channels for WebSockets — essential tools for building scalable, performant Django apps:

# 1. Django’s Async Capabilities (3.1+)
Django 3.1+ introduced async views and middleware support, allowing non-blocking operations.

🔹 Async View Example:
```
from django.http import JsonResponse
import asyncio

async def async_view(request):
    await asyncio.sleep(1)
    return JsonResponse({'status': 'async response'})
```
🔹 Notes:
You can mix sync & async views.

Django ORM is still synchronous, unless you use third-party async ORM (e.g., Tortoise-ORM).

Use Cases:
External API calls

Non-blocking I/O

Real-time dashboards

# 2. Caching in Django
Django supports several backends: local memory, Memcached, Redis, etc.

🔹 Set Up Cache in settings.py (Redis Example):
```
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
    }
}
```
🔹 cache.set() / cache.get():
```
from django.core.cache import cache

cache.set('greeting', 'Hello', timeout=60)  # 1 minute
value = cache.get('greeting')               # "Hello"
```
🔹 @cache_page decorator:
```
from django.views.decorators.cache import cache_page

@cache_page(60 * 5)  # Cache for 5 minutes
def product_list(request):
    ...
```
 Reduces DB load and response time

# 3. Celery for Background Tasks
Celery lets you run time-consuming tasks (emails, reports, etc.) asynchronously.

🔹 Install:
```
pip install celery redis
```
🔹 Create celery.py in your project root:
```
import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
app = Celery("myproject")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
```
🔹 Update __init__.py in project:
```
from .celery import app as celery_app
__all__ = ["celery_app"]
```
🔹 Create a task:

# app/tasks.py
```
from celery import shared_task

@shared_task
def send_email_task(email):
    # send email logic
    return "Email sent"
```
🔹 Run worker:
```
celery -A myproject worker --loglevel=info
```
Use Redis or RabbitMQ as the message broker.

# 4. Channels for WebSockets (Real-Time)
Django Channels adds WebSocket support to Django using ASGI.

🔹 Install:
```
pip install channels
```
🔹 settings.py:
```
INSTALLED_APPS = [
    ...
    'channels',
]
```

ASGI_APPLICATION = "myproject.asgi.application"
🔹 asgi.py:
```
import os
from channels.routing import ProtocolTypeRouter

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    # "websocket": ...
})
```
🔹 Use Cases:
Chat apps

Live notifications

Real-time data dashboards

# Channels replaces WSGI with ASGI, enabling async support natively.

# Summary Table
```
Feature	`               Tool/Method	                Use Case
Async Views	            async def view()	        Non-blocking I/O, real-time fetches
Caching	                cache.set, @cache_page	    Reduce DB load and speed up views
Background Tasks	    Celery + Redis/RabbitMQ	    Emails, report generation, scraping
Real-Time	            Django Channels	            WebSockets, chat, notifications
```
---
Celery sends programing tasks (in api background task) and celery beat sends scheduled tasks to the task queue.If you want to run more than one worker you have to run worker command that many times. Each worker has it own pool. concorency defines size of pool for the worker.