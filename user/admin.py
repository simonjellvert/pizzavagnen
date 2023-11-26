from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import CustomUser
from .forms import SignUpForm


@admin.register(CustomUser)
class CustomAdmin(UserAdmin):
    model = CustomUser
    list_display = (
        'first_name',
        'last_name',
        'username',
        'email',
        'date_joined',
        )
