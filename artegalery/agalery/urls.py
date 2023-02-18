from django.urls import path
from agalery import views
from agalery.views import *
#from django.contrib.staticfiles import staticfiles_urlpatterns

urlpatterns = [
    path("", views.inicio),
    path('usuarios/', views.usuario),
    path('artistas/', views.artista),
    path('obras/', views.obra),
    path('compradores/', views.comprador),
      ]