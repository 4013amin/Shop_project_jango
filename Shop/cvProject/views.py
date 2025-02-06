from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from . import models
from django.contrib.auth.models import User
from .forms import loginForm


# Create your views here.
def home(request):
    pass
    return render(request, 'index.html')


def login_view(request):
    if request.method == "POST":
        form = loginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                user.is_superuser = False
                user.is_staff = False
                user.save()

                login(request, user)

                if request.GET.get('next'):
                    return HttpResponseRedirect(request.GET.get('next'))
                return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
            else:
                context = {
                    'username': username,
                    'error': "نام کاربری یا رمز عبور اشتباه است!"
                }
                return render(request, 'login.html', context)

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return render(request, 'index.html')


def dashboard(request):
    pass
    return render(request, 'dashboard.html')


def contact(request):
    return render(request, 'contact.html')


@login_required
def venue_view(request):
    venues = models.Concert.objects.all()
    return render(request, 'venues.html', {'venues': venues})


def venue_Index_view(request):
    venues = models.Concert.objects.all()[:5]
    context = {
        'venues': venues
    }
    return render(request, 'index.html', context)


@login_required
def venue_detail(request, id):
    venue = get_object_or_404(models.Concert, id=id)
    return render(request, 'venue_detail.html', {'venue': venue})
