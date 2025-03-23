import django
from django.conf import settings
from django.db import utils
from django.views.generic import TemplateView
from django_tenants.utils import remove_www
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout

from customers.models import Client
from onus_base.models import OnUsUser
from .forms import UserForm, UserCreationForm


def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = OnUsUser.objects.get(username=username)
        except:
            messages.error(request, f'User with username {username} does not exist')
            user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index_doctor')
        else:
            messages.error(request, f'Username OR password does not exist. Email: {username}, Password: {password}')

    context = {'page': page}
    return render(request, 'onus_base/login_register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('index_doctor')


def registerPage(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration')

    return render(request, 'onus_base/login_register.html', {'form': form})

class HomeView(TemplateView):
    page = "home"
    template_name = "index_public.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        hostname_without_port = remove_www(self.request.get_host().split(':')[0])

        try:
            Client.objects.get(schema_name='public')
        except utils.DatabaseError:
            context['need_sync'] = True
            context['shared_apps'] = settings.SHARED_APPS
            context['tenants_list'] = []
            return context
        except Client.DoesNotExist:
            context['no_public_tenant'] = True
            context['hostname'] = hostname_without_port

        if Client.objects.count() == 1:
            context['only_public_tenant'] = True

        context['tenants_list'] = Client.objects.all()
        return context
