from django.urls import path
from .views import feed, create_post
urlpatterns = [
    path('create/', create_post, name='create_post'),
    path('', feed, name='feed'),
    
]
