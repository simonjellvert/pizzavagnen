from django import forms
from allauth.account.forms import SignupForm
from .models import User


class CustomUserCreationForm(SignupForm):
    """Form for the owner signup page"""

    pass


class EditUserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = [
            'username',
            'email',
        ]