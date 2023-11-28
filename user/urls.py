from django.urls import path
from .views import register, user_view
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('register/', register, name='register'),
    path('user/', user_view, name='user_view'),
]
