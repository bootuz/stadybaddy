from django.contrib import messages
from django.contrib.auth import login, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from users.forms import RegistrationForm, ProfileForm, UserForm
from users.models import Profile
from users.tokens import account_activation_token


def register(request):
    if request.user.is_authenticated:
        messages.info(request, 'You are already logged in. To create a new account you need to log out.')
        return redirect('index')
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! Activation link sent! Please check your mail.')
            user = form.save()
            subject = 'Please Activate Your Account'
            user.is_active = False
            user.save()
            current_site = get_current_site(request)

            message = render_to_string('users/activation_request.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            return redirect('/user/login')
        else:
            context = {
                'form': form
            }
            return render(request, 'users/register.html', context)
    else:
        form = RegistrationForm()
        context = {
            'form': form,
        }
        return render(request, 'users/register.html', context)


def reset(request):
    pass


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.signup_confirmation = True
        user.save()
        login(request, user)
        messages.success(request, f'Hey {user.username}, your account has been activated!')
        return redirect('index')
    return render(request, 'users/activation_invalid.html')


@login_required(login_url='login')
def profile(request):
    user = User.objects.get(username=request.user.username)
    prof = Profile.objects.get(user=user)
    context = {
        'profile': prof
    }
    return render(request, 'users/profile.html', context)


@login_required(login_url='login')
def edit_profile(request):
    user = User.objects.get(username=request.user.username)
    prof = Profile.objects.get(user=user)

    if request.method == 'POST':
        user_form = UserForm(request.POST, request.FILES, instance=user)
        prof_form = ProfileForm(request.POST, request.FILES, instance=prof)
        if user_form.is_valid() and prof_form.is_valid():
            user_form.save()
            prof_form.save()
            return redirect('profile')
    else:
        user_form = UserForm(instance=user)
        prof_form = ProfileForm(instance=prof)

    context = {
        'user_form': user_form,
        'prof_form': prof_form,
        'profile': prof,
    }
    return render(request, 'users/edit_profile.html', context)


@login_required(login_url='login')
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, "Your password has benn changed!")
            return redirect('profile')
        else:
            context = {
                'form': form
            }
            return render(request, 'users/change_password.html', context)
    else:
        form = PasswordChangeForm(user=request.user)

        context = {
            'form': form
        }
        return render(request, 'users/change_password.html', context)
