from django.urls import path
from .views import register
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('register/', register, name='register'),
]
