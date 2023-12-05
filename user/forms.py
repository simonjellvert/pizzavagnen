from django import forms
from allauth.account.forms import SignupForm
from .models import CustomUser


class CustomUserCreationForm(SignupForm):
    """Form for the signup page"""

    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email']

    def save(self, request):
        user = super(CustomUserCreationForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user


class EditUserForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = [
            'first_name',
            'last_name',
            'email',
        ]
