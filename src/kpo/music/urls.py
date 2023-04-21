from django.urls import path
from . import views
 
urlpatterns = [
  path('', views.index),
  path('download/', views.download, name="download"), 
  path('view_list/', views.view_list, name="view_list"), 
]