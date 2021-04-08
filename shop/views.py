from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader


def index(request):
    return render(request, 'index.html')


def authenticate(request):
    return render(request, 'login.html')


def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        if email == 'thayQueDepTrai' and password == '123':
            return render(template_name='index.html', request=request)
        else:
            return render(template_name='login.html', request=request  )

