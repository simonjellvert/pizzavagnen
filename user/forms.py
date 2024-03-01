from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    """ Form for the signup page """

    email = forms.EmailField(required=True)
    username = forms.CharField(
        max_length=20,
        label='Username',
        help_text='',
    )
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput,
        help_text=_(
            "Must contain at least 8 characters.<br>"
            "Can't be to similar to your username"
        )
    )

    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput,
        help_text=""
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].required = True


class EditUserForm(forms.ModelForm):
    """ Function for editing user profile """
    class Meta:
        model = CustomUser
        username = forms.CharField(
            max_length=20,
            label='Username',
            help_text=''
        )
        fields = ['username', 'email']
