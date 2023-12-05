from django.urls import path
from .views import CustomSignupView, edit_profile, CustomPasswordChangeView, delete_user_view

urlpatterns = [
    path('signup/', CustomSignupView.as_view(), name='signup'),
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('change-password/', CustomPasswordChangeView.as_view(),
         name='password_change'),
path('user/delete_account/', delete_user_view, name='delete_user_view'),
]
