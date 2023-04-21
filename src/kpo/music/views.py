from django.shortcuts import render

# Create your views here.

def index(request):
    context = {}
    return render(request, "music/index.html", context)

def download(request):
    context = {} 
    return render(request, "music/download.html", context)

def view_list(request):
    context = {} 
    return render(request, "music/view_list.html", context)
