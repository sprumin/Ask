from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Domain manage admin class."""
    list_display = ('id', 'user', 'message', 'comment', 'message_at', 'thumbs')
    ordering = ('-id',)
    search_fields = ('user', )
