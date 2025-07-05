```
myproject/
│
├── manage.py
├── myproject/            ← Project package
│   ├── __init__.py
│   ├── settings.py       ← Project settings/configuration
│   ├── urls.py           ← Root URLconf
│   ├── wsgi.py           ← WSGI entry point (for deployment)
│   └── asgi.py           ← ASGI entry point (for async support)
│
├── myapp/                ← Custom application
│   ├── migrations/       ← Database migrations
│   │   └── __init__.py
│   ├── __init__.py
│   ├── admin.py          ← Admin interface configuration
│   ├── apps.py           ← App configuration
│   ├── models.py         ← Database models
│   ├── tests.py          ← Test cases
│   ├── views.py          ← View logic (controllers)
│   ├── urls.py           ← App-specific URLs (you may create this)
│   └── serializers.py    ← (For DRF – if you're using it)
│
├── templates/            ← (Optional) HTML templates
├── static/               ← (Optional) Static files (CSS/JS)
├── media/                ← (Optional) Uploaded media files
└── requirements.txt      ← (Optional) List of dependencies

```
```
| File/Folder        | Description                                                   |
| ------------------ | ------------------------------------------------------------- |
| `manage.py`        | CLI utility to manage your project (runserver, migrate, etc.) |
| `myproject/`       | Main settings/config for your Django project                  |
| `settings.py`      | Contains configuration like DB, installed apps, middleware    |
| `urls.py`          | Root URL dispatcher                                           |
| `wsgi.py/asgi.py`  | Server gateway interface (used for deployment)                |
| `myapp/`           | A Django app inside the project (can have multiple apps)      |
| `models.py`        | Defines data models (ORM)                                     |
| `views.py`         | Contains logic to handle requests/responses                   |
| `admin.py`         | Registers models with Django admin                            |
| `apps.py`          | App-specific config (class-based)                             |
| `templates/`       | Stores HTML templates                                         |
| `static/`          | Stores static files like CSS/JS/images                        |
| `media/`           | Stores uploaded user files                                    |
| `requirements.txt` | Python dependencies list                                      |

```
# 1. wsgi.py Web Server Gateway Interface
This file is used for synchronous(one at a time) communication between the web server(e.g., Apache, Nginx with Gunicorn) and the Django application.
# 2. asgy.py Asynchronous Server Gateway Interface
Enables Django to handle both synchronous and asynchronous communication, including WebSockets, HTTP/2, and long-lived connections.
# use of Nginix and Gunicorn
A client sends a request to Nginx, which serves static content directly or forwards dynamic requests to Gunicorn; Gunicorn translates the request for Django, where it's processed, then returns the response to Gunicorn, which sends it back to Nginx, and finally to the client.
# use of differnt apps in django
## 1. django.contrib.admin
Purpose: Enables Django's built-in admin interface, a web-based tool for managing the application.
Feature
Provides a user-friendly interface for CRUD operations on models.
Allows developers to register and manage models without custom coding.
Use Case: Accessing and managing data via /admin/.
## 2. django.contrib.auth
Purpose: Provides user authentication and authorization functionality.
Features:
User models (e.g., User for login and password management).
Groups and permissions for role-based access control.
Password hashing and reset mechanisms.
Use Case: Managing user accounts, logins, and permissions.
## 3. django.contrib.contenttypes
Purpose: Supports generic relationships in Django models.
Features:
Allows models to relate to instances of other models dynamically.
Enables features like generic foreign keys.
Use Case: Applications requiring relationships between diverse models (e.g., tagging systems).
## 4. django.contrib.sessions
Purpose: Handles session management for storing data between HTTP requests.
Features:
Tracks user sessions using cookies or server-side storage.
Stores data (e.g., user preferences, login status) securely.
Use Case: Keeping users logged in or preserving their preferences.
## 5. django.contrib.messages
Purpose: Provides a framework for temporary, one-time messages to users.
Features:
Message storage and retrieval.
Integrates with views and templates to display notifications (e.g., "Profile updated successfully").
Use Case: Sending feedback messages in applications, such as success or error notifications.
## 6. django.contrib.staticfiles
Purpose: Manages static files like CSS, JavaScript, and images.
Features:
Collects static files from apps into a single directory for deployment (collectstatic).
Simplifies serving static assets during development.
Use Case: Serving front-end assets to enhance the application's user interface.

# Use of different middlewares in django
## 1. django.middleware.security.SecurityMiddleware
Purpose: Provides security enhancements for the application.
Functions:
Adds security headers (e.g., Strict-Transport-Security) for HTTPS.
Prevents content sniffing (X-Content-Type-Options header).
Configures secure cookie settings (SECURE_COOKIE_* settings).
Use Case: Ensures the application is more secure against common vulnerabilities.
## 2. django.contrib.sessions.middleware.SessionMiddleware
Purpose: Manages user sessions.
Functions:
Provides session support, storing data between requests (e.g., user preferences, login status).
Handles session data in cookies or server-side storage.
Use Case: Keeps track of a user’s state across requests (e.g., logged-in state).
## 3. django.middleware.common.CommonMiddleware
Purpose: Provides a set of common functionalities for request/response processing.
Functions:
Can redirect URLs that don’t end with a trailing slash (APPEND_SLASH setting).
Controls whether to send 304 Not Modified responses based on If-Modified-Since headers.
Use Case: Helps with URL normalization and some basic caching behaviors.
## 4. django.middleware.csrf.CsrfViewMiddleware
Purpose: Provides protection against Cross-Site Request Forgery (CSRF) attacks.
Functions:
Ensures that forms include a valid CSRF token, and the token matches the one in the request header.
Blocks malicious requests that don’t include the CSRF token.
Use Case: Protects sensitive data from being altered by external scripts or unauthorized users.
## 5. django.contrib.auth.middleware.AuthenticationMiddleware
Purpose: Associates the request with a user by managing user authentication.
Functions:
Adds the user to the request object, allowing views to access the logged-in user.
Ensures user authentication is handled for each request.
Use Case: Links a user to the request and handles user authentication.
## 6. django.contrib.messages.middleware.MessageMiddleware
Purpose: Manages temporary, one-time messages for the user.
Functions:
Stores messages in the session and retrieves them for display (e.g., success, error messages).
Uses a message queue to display messages after actions like form submissions.
Use Case: Displays feedback to users (e.g., success or error messages) after interactions.
## 7. django.middleware.clickjacking.XFrameOptionsMiddleware
Purpose: Prevents Clickjacking attacks by controlling whether your site can be embedded in a frame.
Functions:
Adds the X-Frame-Options header to responses, controlling iframe embedding.
Default is DENY (disallows embedding), but can be set to SAMEORIGIN to allow embedding from the same origin.
Use Case: Protects your site from being embedded in malicious iframes, reducing clickjacking vulnerabilities.