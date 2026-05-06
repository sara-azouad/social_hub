from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post,Report
from django.contrib.auth.models import User
from .models import Post, Comment
from django.contrib import messages
from notifications.models import Notification
@login_required
def report_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    # check duplicate
    if Report.objects.filter(user=request.user, post=post).exists():
        messages.warning(request, "You already reported this post.")
        return redirect(request.META.get('HTTP_REFERER', '/'))

    # create report record
    Report.objects.create(user=request.user, post=post)

    # IMPORTANT: update counter
    post.report_count += 1
    post.save()

    # flag logic
    if post.report_count >= 3:
        post.is_flagged = True
        post.save()

    messages.success(request, "Post reported!")

    return redirect(request.META.get('HTTP_REFERER', '/'))

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
               # 🔔 notification
            if post.user != request.user:
                Notification.objects.create(
                    sender=request.user,
                    receiver=post.user,
                    notif_type='comment',
                    post=post,
                    text=f"{request.user.username} commented on your post"
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
        # 🔔 notification
        if post.user != request.user:
            Notification.objects.create(
                sender=request.user,
                receiver=post.user,
                notif_type='like',
                post=post,
                text=f"{request.user.username} liked your post"
            )

    return redirect(request.META.get('HTTP_REFERER', 'home'))
    
from connections.models import Follow

@login_required
def feed(request):

    # users current user is following
    following_ids = Follow.objects.filter(
        follower=request.user
    ).values_list('following_id', flat=True)

    # include yourself (Instagram style)
    following_ids = list(following_ids)
    following_ids.append(request.user.id)

    # posts from followed users + yourself
    posts = Post.objects.filter(
        user__id__in=following_ids
    ).order_by('-created_at')

    # suggestions (for sidebar)
    users = User.objects.exclude(id=request.user.id)

    return render(request, 'connections/home.html', {
        'posts': posts,
        'users': users,
        'following_ids': following_ids
    })


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