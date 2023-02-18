from django.urls import path
from agalery import views
from agalery.views import *
#from django.contrib.staticfiles import staticfiles_urlpatterns

urlpatterns = [
    path("", views.inicio),
    path('usuario/', views.usuario),
    path('artista/', views.artista),
    path('obra/', views.obra),
    path('comprador/', views.comprador),
      ]