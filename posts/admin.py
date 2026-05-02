from django.contrib import admin
from .models import Post, Comment, Like, Report


# =========================
# POST ADMIN
# =========================
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'content', 'created_at', 'report_count', 'is_flagged')
    list_filter = ('is_flagged', 'created_at')
    search_fields = ('content', 'user__username')

    # 🔥 Admin actions
    actions = ['mark_as_flagged']

    def mark_as_flagged(self, request, queryset):
        queryset.update(is_flagged=True)

    mark_as_flagged.short_description = "Mark selected posts as flagged"


# =========================
# COMMENT ADMIN
# =========================
admin.site.register(Comment)


# =========================
# LIKE ADMIN
# =========================
admin.site.register(Like)


# =========================
# REPORT ADMIN
# =========================
@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'post')
    list_filter = ('user',)