from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm, EditUserForm
from .models import CustomUser


class CustomSignupView(CreateView):
    """
    Sign up view
    """
    template_name = 'user/user_registration.html'
    form_class = CustomUserCreationForm
    model = CustomUser

    def get_success_url(self):
        return reverse_lazy('account_login')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'User successfully created!')
        return response

    def form_invalid(self, form):
        response = super().form_invalid(form)
        messages.error(self.request, 'The form is invalid, please check your details.')
        return response


@login_required
def edit_profile(request):
    """
    Edit user view
    """
    if request.method == 'POST':
        form = EditUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('edit_profile')

    else:
        form = EditUserForm(instance=request.user)

    return render(request, 'user/profile.html', {
        'form': form,
    })


@login_required
def delete_user_view(request):
    """
    Deletes user view
    """

    if request.method == 'POST':
        user = request.user

        logout(request)

        user.delete()

        messages.success(request, 'Account deleted!')
        return redirect('home')

    return render(request, 'home/index.html')


def change_password(request):
    """
    Change password view
    """
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(
                request, 'Your password was successfully updated!')
            return redirect('edit_profile')
        else:
            messages.error(request, 'Please correct the error(s) below.')
    else:
        form = PasswordChangeForm(request.user)

    return render(request, 'account/password_change.html', {'form': form})
