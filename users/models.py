#migration is Think of migrations like a history of changes for your database.Every time you create a new model (like UserProfile) or change an existing model, Django needs to update the database to reflect those changes.Migrations are scripts that tell Django what changes to make in the database. 
#models.py is where Django looks for database models.
#Each class becomes a database table when we migrate
 #this code Adds bio and profile picture fields to every user
 # -------------------------------------------
# User <----1:1----> UserProfile
#
# Django User model (built-in)
# ----------------------------
# id          (primary key)
# username
# email
# password
# ...
#
# UserProfile model (your model)
# -------------------------------
# id          (primary key)
# user_id     (OneToOneField linking to User)
# bio         (optional text field)
# profile_picture (optional image field)
#
# Explanation:
# - Each User has exactly one UserProfile
# - Each UserProfile belongs to exactly one User
# - If a User is deleted, the linked UserProfile is also deleted (CASCADE)
# - The __str__ method returns user.username for easy identification
from django.db import models  # Import Django’s database tools to define models (tables)
from django.contrib.auth.models import User  # Import Django’s built-in User model for authentication

class UserProfile(models.Model):  # Define a new database table called UserProfile
    # Link this profile to exactly one User
    # on_delete=models.CASCADE → if the User is deleted, the profile is also deleted
    user = models.OneToOneField(User, on_delete=models.CASCADE)  

    # A text field to store the user's bio (optional)
    bio = models.TextField(blank=True)  

    # An image field to store the user's profile picture (optional)
    # upload_to='profile_pics/' → uploaded pictures are saved in this folder
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)  
#ImageField is a special type of field in Django used to store image files (like .jpg, .png) in your project.Django itself cannot handle image files directly. It needs a library to process images (resize, validate, save).Pillow is that library for Python.
    # Define what is shown when we look at this object (admin panel, shell)
    # Here, it will show the linked user's username
    def __str__(self):  
        return self.user.username
