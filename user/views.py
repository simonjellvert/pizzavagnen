from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import PasswordChangeView
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm, EditUserForm
from .models import User


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save(request)
            return redirect('user/account')
    else:
        form = CustomUserCreationForm()

    return render(request, 'account/signup.html', {'form': form})


def user_view(request):
    return render(request, 'user/account.html')


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('edit_profile')

    else:
        form = EditUserForm(instance=request.user)

    return render(request, 'user/account.html', {
        'form': form,
    })


class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'account/password_change.html'
    
    def get_success_message(self, cleaned_data):
        return "Your password was changed successfully."


@login_required
def delete_user_view(request):
    """
    Deletes user
    """

    if request.method == 'POST':
        user = request.user

        # Logout the user
        logout(request)

        # Delete the user
        user.delete()

        messages.success(request, 'Account deleted!')
        return redirect('home')

    # For GET requests, you can customize the template and context as needed
    return render(request, 'home/index.html')  # Update the template name
