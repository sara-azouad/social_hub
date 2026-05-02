from django.contrib import admin
from .models import Post, Comment,Like

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'content', 'created_at')

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Like)