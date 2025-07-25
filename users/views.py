from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render
from .forms import ProfileForm
from users.models import Profile
from django.contrib.auth import get_user_model
from courses.models import Course
from courses.models import Enrollment 


def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')  # change this if your home/dashboard URL name is different
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})


@login_required
def dashboard_view(request):
    profile = request.user.profile
    enrollments = Enrollment.objects.filter(user=request.user).select_related('course')

    return render(request, 'users/dashboard.html', {
        'profile': profile,
        'enrollments': enrollments
    })

def logout_view(request):
    logout(request)
    return redirect('login')

def student_dashboard(request):
    return HttpResponse("Welcome Student!")

def creator_dashboard(request):
    return HttpResponse("Welcome Creator!")

def csrf_failure_view(request, reason=""):
    return render(request, 'users/csrf_failure.html', status=403)

def profile_view(request):
    profile = request.user.profile
    form = ProfileForm(request.POST or None, instance=profile)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('dashboard')

    return render(request, 'users/profile.html', {'form': form})

def profiles_view(request):
    profiles = Profile.objects.all()
    return render(request, 'users/all_profiles.html', {'profiles': profiles})

def home_view(request):
    return render(request, 'users/home.html')