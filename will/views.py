from will.models import User
from will.forms import LoginForm

from django.shortcuts import render, redirect


def home(request):
    Users = User.objects.all()

    context = {'Users': Users}

    return render(request, 'index.html', context)


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            return redirect('account_page/', form.email, form.password)
    else:
        form = LoginForm()

    return render(request, 'login_page.html', {'form': form})


def account_page(request, email, password):
    return render(request, 'base.html', {})
