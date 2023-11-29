from django.urls import path
from .views import register, user_view, edit_profile, CustomPasswordChangeView
from django.contrib.auth.views import LoginView, PasswordChangeView


urlpatterns = [
    path('register/', register, name='register'),
    # path('user_view/', user_view, name='user_view'),
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('change-password/', CustomPasswordChangeView.as_view(), name='password_change'),
]
