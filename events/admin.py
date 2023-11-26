from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Post
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_filter = ('status', 'created_on')
    list_display = ('title', 'status', 'created_on')
    search_fields = ['title', 'content']
    summernote_fields = ('content')
