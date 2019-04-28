from django.contrib import admin

# Register your models here.
# dappx/admin.py

from django.contrib import admin
from login_signup.models import UserProfileInfo, User
# Register your models here.

admin.site.register(UserProfileInfo)
