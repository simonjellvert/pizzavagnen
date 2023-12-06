from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    """Form for the signup page"""

    class Meta:
        model = CustomUser
        username = forms.CharField(
            max_length=20,
            label='Username',
            help_text='',
        )
        fields = ['username', 'email']


class EditUserForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        username = forms.CharField(
            max_length=20,
            label='Username',
            help_text=''
        )
        fields = ['username', 'email']
