from will.models import User
from django.shortcuts import render


def home(request):
    all_users = User.objects.all()

    context = {'all_users': all_users}

    return render(request, 'base.html', context)
