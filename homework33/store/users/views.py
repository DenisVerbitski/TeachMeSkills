from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy

from .forms import PasswordChangingForm, UserRegistrationForm


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Добро пожаловать, {user}!')
            return redirect('game:games')
        else:
            messages.success(request, ('Произошла Ошибка При Входе в Систему, Попробуйте Еще Раз...'))
            return redirect('user:login')
    else:
        return render(request, 'authenticate/login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, ('Вы Вышли из Системы!'))
    return redirect('game:games')


def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username =  form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f'{user}, регистрация прошла успешно!')
            return redirect('game:games')
    else:
        form = UserRegistrationForm()
    return render(request, 'authenticate/register_user.html', {'form': form})


class CustomPasswordChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    template_name='authenticate/password_change.html'
    success_url = reverse_lazy('user:password_success')

    def form_valid(self, form):
        form.save()
        self.request.session.flush()
        logout(self.request)
        return super().form_valid(form)