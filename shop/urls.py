from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('auth', views.authenticate, name='auth'),
    path('verify', views.user_login, name='verify')
]
