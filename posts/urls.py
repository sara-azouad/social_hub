from django.urls import path
from .views import feed, create_post
from . import views
urlpatterns = [
    path("create-post/", views.create_post, name="create_post"),
    path('', feed, name='feed'),
    path('like/<int:post_id>/', views.like_post, name='like_post'),
    path('delete/<int:post_id>/', views.delete_post, name='delete_post'),
    path('comment/<int:post_id>/', views.add_comment, name='add_comment'),
]
