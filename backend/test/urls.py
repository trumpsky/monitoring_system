from django.urls import path
from django.http import HttpResponse
from . import views

urlpatterns = [
    path('index1/', views.test),
    path('index2/', lambda x: HttpResponse('hello world')),
    path('logintest/', views.login_test)
]