from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib import auth
from .forms import RegisterForm, LoginForm


# Create your views here.
def register_user(request) -> HttpResponseRedirect | HttpResponse:
    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('user_app:login_page'))
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'register_form': form})


def login_user(request) -> HttpResponseRedirect | HttpResponse:
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username: str = request.POST['username']
            password: str = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index_page'))
    else:
        form = LoginForm()
    return render(request, 'login.html', {'login_form': form})


def logout_user(request) -> HttpResponseRedirect:
    auth.logout(request)
    return HttpResponseRedirect(reverse('index_page'))
