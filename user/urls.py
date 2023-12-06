from django.urls import path
from .views import (
    CustomSignupView,
    edit_profile,
    change_password,
    delete_user_view,
)


urlpatterns = [
    path('signup/', CustomSignupView.as_view(), name='user_signup'),
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('change-password/', change_password,
         name='change_password'),
    path('user/delete_account/', delete_user_view, name='delete_user_view'),
]
