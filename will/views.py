from will.models import User
from django.shortcuts import render


def home(request):
    Users = User.objects.all()

    context = {'Users': Users}

    return render(request, 'base.html', context)
