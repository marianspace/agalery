from django.urls import path
from agalery import views
from agalery.views import *
#from django.contrib.staticfiles import staticfiles_urlpatterns

urlpatterns = [
    path("", views.inicio, name='inicio'),
    path('usuario/', views.usuario),
    path('artista/', views.artista, name='artista'),
    path('obra/', views.obra, name='obra'),
    path('comprador/', views.comprador),
     path('ingresar/', views.ingresar, name='ingresar')
         ]