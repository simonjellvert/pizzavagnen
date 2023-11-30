from django import forms
from allauth.account.forms import SignupForm
from .models import User


class CustomUserCreationForm(SignupForm):
    """Form for the owner signup page"""

    def save(self, request):
        user = super(CustomUserCreationForm, self).save(request)
        return user


class EditUserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = [
            'username',
            'email',
        ]