from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from posts.models import Post
from .models import UserProfile


# ======================
# EDIT PROFILE
# ======================
@login_required
def edit_profile(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        profile.bio = request.POST.get("bio", "").strip()

        if request.FILES.get("profile_picture"):
            profile.profile_picture = request.FILES["profile_picture"]

        profile.save()

        return redirect('profile', username=request.user.username)

    return render(request, "users/edit_profile.html", {
        "profile": profile
    })


# ======================
# LOGIN
# ======================
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('profile', username=user.username)
        else:
            return render(request, 'users/login.html', {
                'error': 'Invalid username or password'
            })

    return render(request, 'users/login.html')


# ======================
# REGISTER
# ======================
def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            return render(request, 'users/register.html', {
                'error': 'Username already exists'
            })

        user = User.objects.create_user(username=username, password=password)
        login(request, user)

        return redirect('profile', username=user.username)

    return render(request, 'users/register.html')


# ======================
# PROFILE
# ======================
@login_required
def profile_view(request, username):
    user = get_object_or_404(User, username=username)

    profile, created = UserProfile.objects.get_or_create(user=user)

    posts = Post.objects.filter(user=user).order_by('-created_at')

    return render(request, 'users/profile.html', {
        'profile_user': user,
        'profile': profile,
        'posts': posts,
    })


# ======================
# LOGOUT
# ======================
def logout_view(request):
    logout(request)
    return redirect('login')