from django.shortcuts import render
from django.http import HttpResponse
from agalery.models import *
from agalery.forms import registro_obra, registrouser, registro_a
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.

def inicio(request):
    return render(request, 'agalery/inicio.html')
   # return HttpResponse('inicio')

def usuarios(request):
    return render(request, 'agalery/inicio.html')
    #return HttpResponse('USUARIO')

def artistas(request):
    return render(request, 'agalery/artista.html')
    #return HttpResponse('artista')

def obras(request):
    return render(request, 'agalery\obra.html')
    #return HttpResponse('obra') 

# def compra(request):
#     return render(request, 'galery/comprador.html')
#     #return HttpResponse('Comprador')
    
def ingresar(request):
    return render(request, 'agalery/ingresar.html')
    #return HttpResponse('Comprador')
    
def buscarobras(request):
    query = request.GET.get('titulo')
    if query is not None:
        resultados = obra.objects.filter(titulo__icontains=query)
    else:
        resultados = []
    return render(request, 'agalery/buscar_obra.html', {'resultados': resultados})
    
def todas_obras(request):
     obras = obra.objects.all()
     return render(request, 'agalery/obra.html', {'obras': obras})   
    
def lista_artistas(request):
    art = artista.objects.all()
    return render(request, 'agalery/artista.html', {'art': art})   

def lista_compradores(request):
    comprar = comprador.objects.all()
    return render(request, 'agalery/comprador.html', {'comprar': comprar})   
    
def registrar_obra(request):
    form = registro_obra()
    if request.method == 'POST':
        form = registro_obra(request.POST)
        if form.is_valid():
            titulo = form.cleaned_data['titulo']
            descripcion = form.cleaned_data['descripcion']
            precio = form.cleaned_data['precio']
            obra_nueva = obra(titulo=titulo, descripcion=descripcion, precio=precio)
            obra_nueva.save()
            return render(request, 'agalery/obra.html')
    return render(request, 'agalery/registro_obra.html', {'form': form, 'registro_obra': registro_obra})   
    
def crear_user(request):
    users = registrouser()
    if request.method == 'POST':
        users = registrouser(request.POST)
        if users.is_valid():
            mail = users.cleaned_data['mail']
            usuario = users.cleaned_data['usuario']
            clave = users.cleaned_data['clave']
            user_nuevo = user(mail=mail, usuario=usuario, clave=clave)
            user_nuevo.save()
            return render(request, 'agalery/registro_obra.html')
    return render(request, 'agalery/crear_user.html', {'users': users,})   

# Da error a guardar los datos   
def nuevo_artista(request):
    artist = registro_a()
    if request.method == 'POST':
        artist = registro_a(request.POST)
        if artist.is_valid():
            usuario = artist.cleaned_data['Usuario']
            nombre = artist.cleaned_data['Nombre']
            apellido = artist.cleaned_data['Apelldio']
            bio = artist.cleaned_data['Bio']
            nuevoa = artista(usuario=usuario, nombre=nombre, apellido=apellido, bio=bio)
            nuevoa.save()
            return render(request, 'agalery/nuevo_art.html')
    return render(request, 'agalery/nuevo_art.html', {'artist': artist, 'registro_a': registro_a})   