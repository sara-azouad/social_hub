from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post
from django.contrib.auth.models import User
from .models import Post, Comment

@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == "POST":
        text = request.POST.get('text')
        if text:
            Comment.objects.create(
                post=post,
                user=request.user,
                text=text
            )

    return redirect(request.META.get('HTTP_REFERER', 'home'))
@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.user == post.user:
        post.delete()

    return redirect(request.META.get('HTTP_REFERER', 'home'))
@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.user in post.likes.all():
        post.likes.remove(request.user)   # unlike
    else:
        post.likes.add(request.user)      # like

    return redirect(request.META.get('HTTP_REFERER', 'home'))

# HOME PAGE (ALL POSTS)
def home(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, "home.html", {"posts": posts})


# FEED (same as home but protected)
@login_required
def feed(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'connections/home.html', {'posts': posts})


# CREATE POST
@login_required
def create_post(request):
    if request.method == "POST":
        content = request.POST.get("content")

        image = request.FILES.get("image")

        if content or image:
            Post.objects.create(
                user=request.user,
                content=content,
                image=image
            )

        return redirect('home')

    return render(request, 'posts/create_post.html')


# PROFILE
@login_required
def profile_view(request, username):
    user = get_object_or_404(User, username=username)
    profile = user.userprofile

    posts = Post.objects.filter(user=user).order_by('-created_at')

    return render(request, 'users/profile.html', {
        'profile_user': user,
        'profile': profile,
        'posts': posts,
        'is_own_profile': request.user == user
    })