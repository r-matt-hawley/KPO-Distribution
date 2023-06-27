from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "music"

urlpatterns = [
    path("concerts/", 
        views.ConcertListView.as_view(), 
        name="concert_list"),

    path("concerts/create/", 
        views.ConcertCreateView.as_view(), 
        name="concert_create"),

    path("concerts/<int:pk>/", 
        views.ConcertDetailView.as_view(), 
        name="concert_detail"),

    path("concerts/<int:pk>/delete/", 
        views.ConcertDeleteView.as_view(), 
        name="concert_delete"),

    path("concerts/<int:pk>/update/", 
        views.ConcertUpdateView.as_view(), 
        name="concert_update"),

    path("concerts/<int:concert_pk>/songs/create/",
        views.SongCreateView.as_view(), 
        name="song_create"),

    path("concerts/<int:concert_pk>/songs/<int:pk>/",
        views.SongDetailView.as_view(), 
        name="song_detail"),

    path("concerts/<int:concert_pk>/songs/<int:pk>/update/", 
        views.SongUpdateView.as_view(), 
        name="song_update"),

    path("concerts/<int:concert_pk>/songs/<int:pk>/delete/", 
        views.SongDeleteView.as_view(), 
        name="song_delete"),

    path("concerts/<int:concert_pk>/songs/<int:song_pk>/parts/create/", 
        views.PartCreateView.as_view(), 
        name="part_create"),

    path("concerts/<int:concert_pk>/songs/<int:song_pk>/parts/<int:pk>/", 
        views.PartDetailView.as_view(), 
        name="part_detail"),

    path("concerts/<int:concert_pk>/songs/<int:song_pk>/parts/<int:pk>/update/", 
        views.PartUpdateView.as_view(), 
        name="part_update"),

    path("concerts/<int:concert_pk>/songs/<int:song_pk>/parts/<int:pk>/delete/", 
        views.PartDeleteView.as_view(), 
        name="part_delete"),

    path("download/", views.download, name="download"),
    path("view_list/", views.view_list, name="view_list"),
    path("file/upload", views.FileUploadView, name="FileUploadView"),
    path("Parts/", views.Parts, name="Parts"),
    path("Parts/<int:partid>", views.PartID, name="PartID"),

]