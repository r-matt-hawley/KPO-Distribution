from django.shortcuts import render
from django.http import HttpResponse
from music.forms import FileForm

def FileUploadView(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('The file is saved')
    else:
        form = FileForm()
        context = {
            'form':form,
        }
    return render(request, 'music/UploadFile.html', context)

def Parts(request):
    return HttpResponse("This is a parts webpage")

def PartID(request, partid):
    return HttpResponse(f"The part ID is:{partid}")

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

