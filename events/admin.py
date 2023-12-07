from django.contrib import admin
from .models import Post


@admin.register(Post)
"""
Filering and displaying events in admin panel
"""
class PostAdmin(admin.ModelAdmin):

    list_filter = ('status', 'created_on')
    list_display = ('title', 'status', 'created_on')
    search_fields = ['title', 'content']
    summernote_fields = ('content')
