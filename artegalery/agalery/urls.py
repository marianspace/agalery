from django.urls import path
from agalery import views
from agalery.views import *


urlpatterns = [
    path("", views.inicio, name='inicio'),
    path('buscar_obras/', views.buscarobras, name='buscarobras'),
    path('registro_obra/', views.registrar_obra, name='nuevaobra'),
    path('nuevo_art/', views.nuevo_artista, name='nuevoart'),
    path('artista/', views.lista_artistas, name='artista'),
    path('obra/', views.todas_obras, name='obra'),
    path('comprador/', views.lista_compradores, name='mecenas'),
    path('ingresar/', views.ingresar, name='ingresar'),
    path('crear_user/', views.crear_user, name='usuarionuevo')
        ]