from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from django.core.exceptions import ObjectDoesNotExist





def register_user(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'Регистрация прошла успешно.')
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('index')
        else:
            messages.error(request, 'Ошибка регистрации.')

    context = {
        'page': page,
        'form': form,
    }

    return render(request, 'users/register.html', context)

def login_user(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == "POST":
        username = request.POST['username'].lower()
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except ObjectDoesNotExist:
            messages.error(request, 'Пользователь не существует')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Некорректное имя пользователя или пароль')

    return render(request, 'users/register.html')

def logout_user(request):
    logout(request)
    messages.info(request, "Вы вышли из аккаунта")
    return redirect('index')
