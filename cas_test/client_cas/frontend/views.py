from django.shortcuts import render
from django.http import HttpResponse


def homepage(request):
    if request.user.is_authenticated:
        return HttpResponse("Hello {}. <a href='/accounts/logout'>Logout</a>".format(request.user.username))
    else:
        return HttpResponse("Not logged in. <a href='/accounts/login'>Login</a>")
