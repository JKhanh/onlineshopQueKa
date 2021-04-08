from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader


def index(request):
    return render(request, 'index.html')


def authenticate(request):
    return render(request, 'login.html')


def verifyAuth(request, email, password):
    if email == 'thayQueDepTrai' and password == '123':
        render(request, 'index.html')
    else:
        render(request, 'login.html')

