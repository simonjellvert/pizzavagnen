from django.urls import path
from .views import register, edit_profile, CustomPasswordChangeView, delete_user_view
from django.contrib.auth.views import LoginView, PasswordChangeView


urlpatterns = [
    path('register/', register, name='register'),
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('change-password/', CustomPasswordChangeView.as_view(), name='password_change'),
    path('delete_account/', delete_user_view, name='delete_account'),
]
