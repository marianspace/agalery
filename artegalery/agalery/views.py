from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, Template
from agalery.models import *
#from agalery.forms import formularios

# Create your views here.

def inicio(request):
    return render(request, 'agalery/inicio.html')
   # return HttpResponse('inicio')

def usuario(request):
    return render(request, 'agalery/inicio.html')
    #return HttpResponse('USUARIO')

def artista(request):
    return render(request, 'agalery/artista.html')
    #return HttpResponse('artista')

def obra(request):
    return render(request, 'agalery\obra.html')
    #return HttpResponse('obra') 

def comprador(request):
    return render(request, 'galery/comprador.html')
    #return HttpResponse('Comprador')
    
def ingresar(request):
    return render(request, 'agalery/ingresar.html')
    #return HttpResponse('Comprador')