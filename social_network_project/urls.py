from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static


def home_redirect(request):
    if request.user.is_authenticated:
        return redirect('/posts/')
    return redirect('/users/login/')


urlpatterns = [
    path('', home_redirect),
    path('admin/', admin.site.urls),
   
    path('users/', include('users.urls')),
    path('posts/', include('posts.urls')),
    path('connections/', include('connections.urls')),
    path('notifications/', include('notifications.urls')),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]

# MEDIA FILES (FIXED PLACE)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)