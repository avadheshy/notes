Here's a complete explanation of Django’s authentication system, covering:

# 1. Django Auth System Overview
Django provides built-in models and features to handle users, groups, permissions, and sessions.

✳️ User Model

```
from django.contrib.auth.models import User

# Create user
user = User.objects.create_user(username='john', password='pass1234')

```
✳️ Group Model
```
from django.contrib.auth.models import Group

group = Group.objects.create(name='Editors')
user.groups.add(group)

```
✳️ Permission Model

Fine-grained control over what a user/group can do (e.g., add_product, delete_order).

```
from django.contrib.auth.models import Permission

perm = Permission.objects.get(codename='change_product')
user.user_permissions.add(perm)

```
# 2. Login, Logout, Password Change/Reset
🔹 Login
```
from django.contrib.auth import authenticate, login

user = authenticate(username='john', password='pass1234')
if user is not None:
    login(request, user)

```
🔹 Logout
```
from django.contrib.auth import logout

logout(request)
```
🔹 Password Change (logged-in user)
```
from django.contrib.auth.forms import PasswordChangeForm

form = PasswordChangeForm(user, request.POST)
if form.is_valid():
    form.save()
```
🔹 Password Reset (email link)
Use Django’s built-in views:

PasswordResetView

PasswordResetConfirmView

Add to urls.py:

```
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
]

```
#3. Permissions & @permission_required
```
#Decorator
from django.contrib.auth.decorators import permission_required

@permission_required('app_label.view_product', raise_exception=True)
def my_view(request):
    ...
```

# 4. Role-Based Access Control (RBAC) in Django
RBAC = Assign roles (groups) → assign permissions → check permissions in views.

🔸 Step-by-Step Example
1. Define Groups and Permissions (can also be done via admin)
```
from django.contrib.auth.models import Group, Permission

editor_group = Group.objects.create(name='Editor')
perm = Permission.objects.get(codename='change_product')
editor_group.permissions.add(perm)
```
2. Assign User to Role
```
user.groups.add(editor_group)
```
3. Check in View or Decorator
```
from django.contrib.auth.decorators import user_passes_test

def is_editor(user):
    return user.groups.filter(name='Editor').exists()

@user_passes_test(is_editor)
def editor_only_view(request):
    ...
```
4. OR Use Permissions Directly
```
@permission_required('products.change_product', raise_exception=True)
def update_product(request):
    ...
```

# Summary
```
Feature	                    Tools/API Used
Auth Models	                User, Group, Permission
Login/Logout	            authenticate(), login(), logout()
Password Handling	        PasswordChangeForm, PasswordResetView
Check Permissions	        @permission_required, user.has_perm()
Role-Based Access           Use Groups as roles + permissions
```