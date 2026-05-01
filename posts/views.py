from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post
def home(request):
    return render(request, 'connections/home.html')
@login_required
def feed(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'connections/home.html', {'posts': posts})
@login_required
def create_post(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')

        Post.objects.create(
            user=request.user,
            title=title,
            content=content
        )

        return redirect('/')  

    return render(request, 'posts/create_post.html')
@login_required
def profile_view(request, username):
    from django.contrib.auth.models import User

    user = get_object_or_404(User, username=username)
    profile = user.userprofile

    posts = Post.objects.filter(user=user).order_by('-created_at')

    return render(request, 'users/profile.html', {
        'profile_user': user,
        'profile': profile,
        'posts': posts,
        'is_own_profile': request.user == user
    })