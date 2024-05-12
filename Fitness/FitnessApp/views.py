from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from .form import UserProfileForm
from .models import UserProfile
from django.contrib import messages
def homepage(request):
    return render(request, 'homepage.html')

def profile(request):
    return render(request, 'profile.html')

def about(request):
    return render(request, 'about.html')


def register_view(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Registration successful. You can now log in.')
            return redirect('homepage')
        else:
            for field_name, errors in form.errors.items():
                for error in errors:
                    messages.warning(request, f"{field_name}: {error}")
    else:
        form = UserProfileForm()
    return render(request, "registration/register.html", {'form': form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('homepage')
        else:
            messages.error(request,'username or password not correct')
            return redirect('homepage')
    else:
        form = AuthenticationForm()
    return render(request, "registration/login.html", {'form': form})

def terms_and_privacy_view(request):
    return render(request, 'registration/terms_and_privacy.html')

def display_profile(request):
    profile = UserProfile.objects.get(user=request.user)
    return render(request, 'profile.html', {'profile': profile})

def check_gym_status(request):
    people_count = 30
    free_threshold = 20
    busy_threshold = 50
    if people_count < free_threshold:
        status = "Free"
    elif free_threshold <= people_count < busy_threshold:
        status = "Almost Busy"
    else:
        status = "Busy"

    return render(request, 'gym_status.html', {'status': status})
# Create your views here.
