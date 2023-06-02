from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index),
    path("download/", views.download, name="download"),
    path("view_list/", views.view_list, name="view_list"),
    path("file/upload", views.FileUploadView, name="FileUploadView"),
    path("Parts/", views.Parts, name="Parts"),
    path("Parts/<int:partid>", views.PartID, name="PartID"),
]