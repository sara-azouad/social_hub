from django.urls import path
from . import views

urlpatterns = [
    path('', views.feed, name='home'),  # main home page (FEED)

    path('create-post/', views.create_post, name='create_post'),
    path('like/<int:post_id>/', views.like_post, name='like_post'),
    path('delete/<int:post_id>/', views.delete_post, name='delete_post'),
    path('comment/<int:post_id>/', views.add_comment, name='add_comment'),
    path('report/<int:post_id>/', views.report_post, name='report_post'),
]