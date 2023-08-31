from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from app.forms.login_form import LoginModelForm
from app.forms.register_form import RegisterModelForm


def register_view(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == "POST":
            form = RegisterModelForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('index')
        else:
            form = RegisterModelForm()
    return render(request=request,
                  template_name='app/auth/register.html',
                  context={"form": form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            form = LoginModelForm(request=request, data=request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request=request,
                      user=user)
                return redirect('index')
        else:
            form = LoginModelForm()
    return render(request=request,
                  template_name='app/auth/login.html',
                  context={"form": form})


@login_required(login_url="login")
def logout_view(request):
    logout(request=request)
    return redirect('index')
