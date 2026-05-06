from django.urls import path
from . import views

urlpatterns = [
     path('follow/<int:user_id>/', views.follow_unfollow, name='follow_unfollow'),
]