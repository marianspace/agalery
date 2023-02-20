from django.urls import path
from agalery import views
from agalery.views import *


urlpatterns = [
    path("", views.inicio, name='inicio'),
    path('buscar_obras/', views.buscarobras, name='buscarobras'),
    path('crear_user/', views.crear_user, name='crearuser'),
    path('usuario/', views.usuarios, name='usuario'),
    #path('artista/', views.artistas, name='artista'),
    path('artista/', views.lista_artistas, name='artista'),
    path('obra/', views.todas_obras, name='obra'),
    path('comprador/', views.compra),
    path('ingresar/', views.ingresar, name='ingresar'),
        ]