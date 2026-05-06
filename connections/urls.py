from django.urls import path
from . import views

urlpatterns = [
     path('follow/<int:user_id>/', views.follow_unfollow, name='follow_unfollow'),
     path('<str:username>/followers/', views.followers_list, name='followers_list'),

     path('<str:username>/following/', views.following_list, name='following_list'),
]