from django import forms
from agalery.models import usuario

# Registros 
class registrouser(forms.Form):
      class Meta:
            model = usuario
            campos = ['usuario', 'clave', 'mail']     


  
    
# class registro_a(forms.Form): #falta ver como vincular con el usuario
#       nombre = forms.CharField(max_length=100, help_text="Nombre") 
#       apellido = forms.CharField(max_length=100, help_text="Apellido")
#       bio = forms.CharField(max_length=300, help_text="Descripción de la obre en 300 caracteres")

# Solo se ingresa desde la opción de artista
# class registro_obra(forms.Form): 
#       # artista = desde adentro de la web
#       titulo = forms.CharField(max_length=200, help_text="Titulo de la obra")
#       descripcion = forms.CharField(max_length=300, help_text="Descripción de la obre en 300 caracteres")
#       #obra_foto = # para el futuro fotos
#       precio = forms.IntegerField()
    
# class registro_c(forms.Form): #falta ver como vincular con el usuario
#      nombre = forms.CharField(max_length=100, help_text="Nombre") 
#      apellido = forms.CharField(max_length=100, help_text="Apellido")
