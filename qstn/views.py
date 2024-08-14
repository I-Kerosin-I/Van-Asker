from django.contrib.auth import authenticate, login as auth_login, logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render

from qstn.forms import *


@login_required(login_url='/login/')
def index(request):
    return render(request, 'qstn/index.html')


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('home')  # перенаправление на главную страницу после успешного входа
    else:
        form = AuthenticationForm()
    form.fields['username'].label = 'Имя пользователя'
    form.fields['password'].label = 'Пароль'

    return render(request, 'registration/login.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('login')


def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('home')
            except:
                form.add_error(None, 'Ошибка регистрации')

    else:
        form = RegistrationForm()

    return render(request, 'registration/registration.html', {'registration_form': form})
