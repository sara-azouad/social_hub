from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from posts.models import Post
from .models import UserProfile
from connections.models import Follow


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
from connections.models import Follow
from connections.models import Follow
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
@login_required
def profile_view(request, username):
    user = get_object_or_404(User, username=username)

    profile = user.userprofile
    posts = Post.objects.filter(user=user).order_by('-created_at')

    users = User.objects.exclude(id=request.user.id)

    following_ids = Follow.objects.filter(
        follower=request.user
    ).values_list('following_id', flat=True)

    is_following = Follow.objects.filter(
        follower=request.user,
        following=user
    ).exists()

    followers_count = Follow.objects.filter(following=user).count()
    following_count = Follow.objects.filter(follower=user).count()

    return render(request, 'users/profile.html', {
        'profile_user': user,
        'profile': profile,
        'posts': posts,
        'users': users,
        'following_ids': list(following_ids),

        # ✅ ADD THESE (IMPORTANT)
        'is_following': is_following,
        'followers_count': followers_count,
        'following_count': following_count,

        'is_own_profile': request.user == user
    })

# ======================
# FOLLOW / UNFOLLOW
# ======================
@login_required
def follow_unfollow(request, user_id):
    target_user = get_object_or_404(User, id=user_id)

    if request.user == target_user:
        return redirect(request.META.get("HTTP_REFERER"))

    follow, created = Follow.objects.get_or_create(
        follower=request.user,
        following=target_user
    )

    if not created:
        follow.delete()

    return redirect(request.META.get("HTTP_REFERER"))


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
# LOGOUT
# ======================
def logout_view(request):
    logout(request)
    return redirect('login')
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from connections.models import Follow

def followers_list(request, username):
    user = get_object_or_404(User, username=username)

    followers = Follow.objects.filter(following=user)

    return render(request, "connections/listefolower.html", {
        "profile_user": user,
        "followers": followers
    })