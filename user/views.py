from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from .forms import SignUpForm, EditUserForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('account')
    else:
        form = SignUpForm()

    return render(request, 'account/signup.html', {'form': form})


def user_view(request):
    return render(request, 'user/account.html')


@login_required
def edit_profile(request):
    if request.method == 'POST':
        user_form = EditUserForm(request.POST, instance=request.user)
        password_form = PasswordChangeForm(request.user, request.POST)

        if user_form.is_valid() and password_form.is_valid():
            user_form.save()
            password_form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('user_view')
        else:
            messages.error(request, 'Please correct the error below')

    else:
        user_form = EditUserForm(instance=request.user)
        password_form = PasswordChangeForm(request.user)

    return render(request, 'user/account.html', {
        'user_form': user_form,
        'password_form': password_form
    })
