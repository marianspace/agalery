from django import forms
from django.db import models
from agalery.models import user, artista

# Registros 
class registrouser(forms.Form):
    mail = models.EmailField() 
    usuario = models.CharField(max_length=20) # DEBERIA SER NEXO ENTRE TODAS LA TABLAS UNICO E IRREPETIBLE
    clave = models.CharField(max_length=8, help_text="Contraseña alfanumerica de diez caracteres")  
 
class registro_obra(forms.Form): 
       titulo = forms.CharField(max_length=200, help_text="Titulo de la obra")
       descripcion = forms.CharField(max_length=300, help_text="Descripción de la obre en 300 caracteres")
       #obra_foto = # para el futuro fotos
       precio = forms.IntegerField()
  
class registro_a(forms.Form): #falta ver como vincular con el usuario
     nombre = forms.CharField(max_length=100, help_text="Nombre")
     apellido = forms.CharField(max_length=100, help_text="Apellido")
     bio = forms.CharField(max_length=300, help_text="Descripción")

# FORMULARIOS NO USABLES AMBOS REQUIEREN VINCULAR CON USUARIO Y NO SUPE COMO
    
# class registro_c(forms.Form): #falta ver como vincular con el usuario
#      nombre = forms.CharField(max_length=100, help_text="Nombre") 
#      apellido = forms.CharField(max_length=100, help_text="Apellido")
