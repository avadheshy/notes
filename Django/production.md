Here’s a production-ready Django deployment guide, covering everything from secure settings to file serving and database configs:

# 1. Production Settings
🔹 settings.py for Production:
```
DEBUG = False

ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']

# Security settings
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
X_FRAME_OPTIONS = 'DENY'
SECURE_HSTS_SECONDS = 31536000
```
Keep SECRET_KEY, DB credentials, and API keys out of code. Use environment variables instead.

# 2. Using Gunicorn or uWSGI with Nginx
🔹 Gunicorn:
A WSGI server that runs your Django app.

```
pip install gunicorn
gunicorn myproject.wsgi:application --bind 0.0.0.0:8000
```
🔹 Nginx (reverse proxy):
Handles static files, media, and forwards requests to Gunicorn.

🔹 Sample Nginx Config:
```
server {
    server_name yourdomain.com;

    location /static/ {
        alias /path/to/static/;
    }

    location /media/ {
        alias /path/to/media/;
    }

    location / {
        proxy_pass http://127.0.0.1:8000;
    }
}
```
Nginx serves static/media; Gunicorn runs Django.

# 3. Static & Media Files in Production
🔹 settings.py:
```
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```
🔹 Collect static files:
```
python manage.py collectstatic
```
🔹 Serve:
Static: via Nginx using alias to STATIC_ROOT

Media: via Nginx using alias to MEDIA_ROOT

 Don’t serve media/static via Django in production!

# 4. Using Environment Variables (django-environ)
🔹 Install:
```
pip install django-environ
```
🔹 .env file:
```
DEBUG=False
SECRET_KEY=your-secret
DATABASE_URL=postgres://user:pass@localhost:5432/mydb
```
🔹 settings.py usage:
```
import environ
env = environ.Env()
environ.Env.read_env()

DEBUG = env.bool("DEBUG")
SECRET_KEY = env("SECRET_KEY")
DATABASES = {
    'default': env.db()
}
```
# 5. Database Configuration
🔹 PostgreSQL example:
```
pip install psycopg2
```
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydb',
        'USER': 'myuser',
        'PASSWORD': 'mypassword',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```
🔹 MySQL example:
```
pip install mysqlclient
```
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mydb',
        'USER': 'myuser',
        'PASSWORD': 'mypassword',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```
Always use strong DB credentials and non-root users in production.

# Summary
```
Topic	                Tool/Setting	                            Purpose
Debug off	            DEBUG=False	                                Prevent info leak
Allowed domains	        ALLOWED_HOSTS	                            Avoid host header attacks
Production server	    Gunicorn or uWSGI	                        Run Django app
Reverse proxy	        Nginx	                                    Serves static/media, forwards reqs
Static/media	        collectstatic, Nginx alias	                Serve efficiently
Env vars	            django-environ, .env	                    Keep secrets/configs outside code
Database	            PostgreSQL/MySQL	                        Scalable production databases

```