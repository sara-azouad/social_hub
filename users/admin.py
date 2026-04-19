from django.contrib import admin
#This makes the UserProfile table appear in the admin panel
from .models import UserProfile

admin.site.register(UserProfile)
