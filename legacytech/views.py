from django.http import HttpResponse


def home(request):
    return render(request, 'index.html', context)
