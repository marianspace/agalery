from django import forms
from agalery.models import usuario

# Registros 

class registrouser(forms.ModelForm):
      class Meta:
            model = usuario
            fields = ('user', 'text')
      
      #usuario = forms.CharField(max_length=20, min_length=5, required=True)
      #clave = forms.CharField(max_length=10, help_text="Contraseña alfanumerica de diez caracteres")
      #mail = forms.EmailField(label='mail',max_length=100, required=True) 
     
class registro_a(forms.Form): #falta ver como vincular con el usuario
      nombre = forms.CharField(max_length=100, help_text="Nombre") 
      apellido = forms.CharField(max_length=100, help_text="Apellido")
      bio = forms.CharField(max_length=300, help_text="Descripción de la obre en 300 caracteres")

# Solo se ingresa desde la opción de artista
class registro_obra(forms.Form): 
    # artista = desde adentro de la web
    titulo = forms.CharField(max_length=200, help_text="Titulo de la obra")
    descripcion = forms.CharField(max_length=300, help_text="Descripción de la obre en 300 caracteres")
    #obra_foto = # para el futuro fotos
    #precio = forms.IntegerField(default=1)  # Me tira error
    
class registro_c(forms.Form): #falta ver como vincular con el usuario
    nombre = forms.CharField(max_length=100, help_text="Nombre") 
    apellido = forms.CharField(max_length=100, help_text="Apellido")
    
    