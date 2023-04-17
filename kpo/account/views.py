from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, "account/home.html", {})

def login(request):
    
    context = {}
    return render(request, "account/login.html", context)


def registration(request):
    
    context = {}
    return render(request, "account/registration.html", context)