from typing import Any
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.forms import CharField, ModelForm, TextInput
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from music.forms import FileForm
from music.models import Concert, Song, Part

from icecream import ic

def FileUploadView(request):
    context ={}
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            # TODO: Add automated fields here (e.g, page_num, if used)
            form.save()
            return HttpResponse('The file is saved')
    else:
        form = FileForm()
        context = {
            'form':form,
        }
    return render(request, 'music/UploadFile.html', context)

def Parts(request):
    return HttpResponse("This page shows all available parts.")

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


class ConcertBaseView(View):
    model = Concert
    fields = ["title", "season"]
    success_url = reverse_lazy("music:concert_list")

class ConcertListView(ConcertBaseView, ListView):
    """View to list all concerts.
    Use the 'concert_list' variable in the template
    to access all Concert objects."""

class ConcertDetailView(ConcertBaseView, DetailView):
    """View to list the details from one concert.
    Use the 'concert' variable in the template to access
    the specific concert here and in the Views below."""

    # def get_context_data(self, **kwargs):
    #     ic(self.args)
    #     ic(self.kwargs)
    #     ic(kwargs)
    #     return super().get_context_data(**kwargs)

class ConcertCreateView(ConcertBaseView, CreateView):
    """View to create a new concert."""

class ConcertUpdateView(ConcertBaseView, UpdateView):
    """View to update a concert."""

class ConcertDeleteView(ConcertBaseView, DeleteView):
    """View to delete a concert."""


class SongBaseView(View):
    model = Song
    fields = ["title", "concert"]

    def get_success_url(self):
        """returns url for redirect after successful 
        creation, deletion, or update of Song."""
        ic(self.kwargs)
        # if "concert_pk" in self.kwargs:
        #     key = self.kwargs["concert_pk"]
        # else:
        #     ic("!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        #     ic("No concert_pk in self.kwargs")
        #     ic("!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        #     key = self.kwargs["pk"]
        return reverse("music:concert_detail", 
                        kwargs={"pk": self.kwargs["concert_pk"]})

class SongListView(SongBaseView, ListView):
    """View to list all songs.
    Use the 'song_list' variable in the template
    to access all Song objects."""

class SongDetailView(SongBaseView, DetailView):
    """View to list the details from one song.
    Use the 'song' variable in the template to access
    the specific song here and in the Views below."""

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        concert = Concert.objects.get(id=self.kwargs["concert_pk"])
        context["concert_title"] = concert.title
        context["concert_pk"] = concert.pk
        return context

class SongCreateView(SongBaseView, CreateView):
    """View to create a new song."""
    fields = ["title"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["concert_pk"] = self.kwargs["concert_pk"]
        return context
    
    def form_valid( self, form):
        song = form.save()
        song.concert.set([self.kwargs["concert_pk"]])
        song.save()
        return HttpResponseRedirect( self.get_success_url())
    
    def get_success_url(self):
        return reverse_lazy("music:concert_detail", 
                            kwargs={"pk": self.kwargs["concert_pk"]})

class SongUpdateView(SongBaseView, UpdateView):
    """View to update a song."""

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["concert_pk"] = self.kwargs["concert_pk"]
        return context

class SongDeleteView(SongBaseView, DeleteView):
    """View to delete a song."""

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["concert_pk"] = self.kwargs["concert_pk"]
        return context


class PartBaseView(View):
    model = Part
    fields = ["name"]

    def get_success_url(self):
        return reverse("music:part_detail", 
                        kwargs={"concert_pk": self.kwargs["concert_pk"],
                                "song_pk": self.kwargs["song_pk"],
                                "part_pk": self.kwargs["part_pk"]})


class PartListView(PartBaseView, ListView):
    """View to list all concerts.
    Use the 'concert_list' variable in the template
    to access all Concert objects."""

class PartDetailView(PartBaseView, DetailView):
    """View to list the details from one concert.
    Use the 'concert' variable in the template to access
    the specific concert here and in the Views below."""

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        concert = Concert.objects.get(id=self.kwargs["concert_pk"])
        context["concert_title"] = concert.title
        context["concert_pk"] = concert.pk
        song = Song.objects.get(id=self.kwargs["song_pk"])
        context["song_title"] = song.title
        context["song_pk"] = song.pk
        return context
class PartCreateView(PartBaseView, CreateView):
    """View to create a new concert."""

class PartUpdateView(PartBaseView, UpdateView):
    """View to update a concert."""

class PartDeleteView(PartBaseView, DeleteView):
    """View to delete a concert."""

