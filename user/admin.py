from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    """
    Function to display and filter user in admin panel
    """
    list_display = ('username', 'email', 'is_staff', 'date_joined')
    search_fields = ('username', 'email', 'date_joined')
    ordering = ('-date_joined',)


admin.site.register(CustomUser, CustomUserAdmin)
