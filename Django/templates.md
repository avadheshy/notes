Here's a detailed explanation of Django templates, covering inheritance, filters/tags, context rendering, and custom template tags & filters:

# 1. Template Inheritance ({% extends %})
Django templates use inheritance to avoid duplication and promote reusability.

🔹 base.html
```
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}My Site{% endblock %}</title>
</head>
<body>
    <div>{% block content %}{% endblock %}</div>
</body>
</html>
```
🔹 home.html (extends base)
```
{% extends "base.html" %}

{% block title %}Home{% endblock %}

{% block content %}
  <h1>Welcome!</h1>
{% endblock %}
```
# 2. Template Filters and Tags
🔹 Built-in Template Filters
Used to format variables in templates.
```
{{ name|upper }}        → uppercase
{{ date|date:"F Y" }}   → formats date
{{ list|length }}       → length of a list
{{ price|floatformat:2 }} → show 2 decimal places
```
🔹 Built-in Template Tags
```
{% for item in items %}
  {{ item.name }}
{% endfor %}

{% if user.is_authenticated %}
  Welcome back!
{% else %}
  Please log in.
{% endif %}
Other tags: {% include %}, {% load %}, {% csrf_token %}, {% url %}, {% static %}
```

✅ 3. Context Data and Rendering
🔹 In Views:
```
from django.shortcuts import render

def home(request):
    context = {
        'user_name': 'Avadhesh',
        'items': ['Pen', 'Book', 'Laptop']
    }
    return render(request, 'home.html', context)
```
🔹 In Template:
```
<h2>Hello {{ user_name }}</h2>
<ul>
  {% for item in items %}
    <li>{{ item }}</li>
  {% endfor %}
</ul>
```
The context dictionary binds data to the template.

✅ 4. Custom Template Tags & Filters
🔹 Directory structure:
```
myapp/
├── templatetags/
│   ├── __init__.py
│   └── custom_tags.py
```
🔹 Create a custom filter:
```
# myapp/templatetags/custom_tags.py
from django import template

register = template.Library()

@register.filter
def multiply(value, arg):
    return value * arg
```
In template:

```
{% load custom_tags %}
{{ 5|multiply:3 }}   → Output: 15
```
🔹 Create a custom tag:
```
@register.simple_tag
def greet(name):
    return f"Hello, {name}!"
```
In template:

```
{% load custom_tags %}
{% greet "Avadhesh" %}
```
# Summary
```
| Feature              | Example                                    | Purpose                           |                            |
| -------------------- | ------------------------------------------ | --------------------------------- | -------------------------- |
| Template inheritance | `{% extends "base.html" %}`                | DRY templates                     |                            |
| Filters              | \`{{ name                                  | upper }}\`                        | Format or modify variables |
| Tags                 | `{% for %}`, `{% if %}`                    | Logic control                     |                            |
| Context rendering    | `render(request, template, ctx)`           | Send data from views to templates |                            |
| Custom filters/tags  | `@register.filter`, `@register.simple_tag` | Extend template engine            |                            |

```