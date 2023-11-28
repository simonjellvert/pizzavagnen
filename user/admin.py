from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import User
from .forms import SignUpForm


@admin.register(User)
class CustomAdmin(UserAdmin):
    model = User
    list_display = (
        'first_name',
        'last_name',
        'username',
        'email',
        'date_joined',
        )
