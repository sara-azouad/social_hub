from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('follow/<int:user_id>/', views.follow_unfollow, name='follow_unfollow'),
    path('profile/<str:username>/', views.profile_view, name='profile'),
    path('logout/', views.logout_view, name='logout'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path("users/<str:username>/followers/", views.followers_list, name="followers_list"),
]