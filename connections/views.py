from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.http import JsonResponse
from .models import Follow
from notifications.models import Notification

def follow_unfollow(request, user_id):
    target_user = get_object_or_404(User, id=user_id)

    if request.user == target_user:
        return JsonResponse({"error": "You cannot follow yourself"}, status=400)

    relation = Follow.objects.filter(
        follower=request.user,
        following=target_user
    )

    if relation.exists():
        relation.delete()
        status = "unfollowed"

    else:
        Follow.objects.create(
            follower=request.user,
            following=target_user
        )
        status = "followed"

        # 🔔 CREATE NOTIFICATION HERE (ONLY WHEN FOLLOWING)
        Notification.objects.create(
            sender=request.user,
            receiver=target_user,
            notif_type='follow',
            text=f"{request.user.username} started following you"
        )

    followers_count = Follow.objects.filter(following=target_user).count()

    return JsonResponse({
        "status": status,
        "followers_count": followers_count
    })
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from .models import Follow


def followers_list(request, username):

    user = get_object_or_404(User, username=username)

    followers = Follow.objects.filter(
        following=user
    )

    return render(request, 'connections/listefolower.html', {
        'profile_user': user,
        'followers': followers
    })


def following_list(request, username):

    user = get_object_or_404(User, username=username)

    following = Follow.objects.filter(
        follower=user
    )

    return render(request, 'connections/listefolowing.html', {
        'profile_user': user,
        'following': following
    })