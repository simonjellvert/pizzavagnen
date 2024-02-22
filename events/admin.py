from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """ Filtering and displaying events in admin panel """

    list_display = ('title', 'status')
    search_fields = ['title', 'content']
