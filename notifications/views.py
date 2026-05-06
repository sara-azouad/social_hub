from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Notification
from django.contrib.auth.models import User
from connections.models import Follow   # adjust if needed

@login_required
def notifications(request):

    notifications = Notification.objects.filter(
        receiver=request.user
    ).order_by('-created_at')

    users = User.objects.exclude(id=request.user.id)

    following_ids = Follow.objects.filter(
        follower=request.user
    ).values_list('following_id', flat=True)

    return render(request, 'notifications/notifications.html', {
        'notifications': notifications,
        'users': users,
        'following_ids': list(following_ids),
    })