from django.shortcuts import render
from django.http import HttpResponse
from agalery.models import *
from agalery.forms import registrouser
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

def compra(request):
    return render(request, 'galery/comprador.html')
    #return HttpResponse('Comprador')
    
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
   # artistas = artista.objects.all()   
   # return render(request, 'agalery/artista.html', {'artistas': artistas})
    
def crear_user(request): # no funca
    if request.method == 'POST':
        form = registrouser(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'agalery/usuario.html')
    else:
        form = registrouser()
    return render(request, 'agalery/crear_user.html', {'form': form})
    
    
    # def crear_user(request): # otra formaula
    # if request.method == 'POST':
    #     form = registrouser(request.POST)
    #     if form.is_valid():
    #         user = usuario(
    #             mail=form.cleaned_data['mail'],
    #             usuario=form.cleaned_data['usuario'],
    #             clave=form.cleaned_data['clave']
    #         )
    #         user.save()  # Guarda
    #         return render('agalery/usuario.html')
    # else:
    #     form = registrouser()
    # return render(request, 'agalery/crear_user.html', {'form': form})
    
    
    
    
    
    # form = registrouser(request.POST)
    # #if request.method == 'POST':
    # #    form = registrouser(request.POST)
    # if form.is_valid():
    #     user = form.save()
    #     return render(request, 'agalery/usuario.html', {'usuario':usuario})
    # else:
    #     form = registrouser()
    # return render(request, 'agalery/crear_user.html', {'form': form})
