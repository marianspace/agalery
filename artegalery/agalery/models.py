from django.db import models

# Create your models here.
class usuario(models.Model):
    mail = models.EmailField(max_length=100) 
    usuario = models.CharField(max_length=20) # debería ser nexo entre todas la tablas 
    clave = models.CharField(max_length=8, help_text="Contraseña alfanumerica de diez caracteres")
    
    def __str__(self):
     return f"Ususario {self.usuario}"
 
 
class artista(models.Model):
    usuario = models.ForeignKey(usuario, verbose_name="Usuario Artista", default=1, on_delete=models.SET_DEFAULT) 
    nombre = models.CharField(max_length=100, help_text="Nombre") 
    apellido = models.CharField(max_length=100, help_text="Apellido")
    bio = models.TextField(max_length=300, help_text="Descripción de la obre en 300 caracteres")
    #obras = listado de obras de su autoria
    
    def __str__(self):
         return f"{self.nombre} {self.apellido}"

class obra(models.Model):
    artista = models.ForeignKey(artista, verbose_name="Nombre del artista", default=1, on_delete=models.SET_DEFAULT)
    titulo = models.CharField(max_length=200, help_text="Titulo de la obra")
    descripcion = models.TextField(max_length=300, help_text="Descripción de la obre en 300 caracteres")
    #obra_foto = # para el futuro fotos
    precio = models.IntegerField(default=1) 
    vendida = models.BooleanField(default= False)
    
    def __str__(self):
        return f'{self.artista} {self.titulo}'
 
class comprador(models.Model):
    usuario = models.ForeignKey(usuario, verbose_name="Usuario Comprador", default=1, on_delete=models.SET_DEFAULT)  
    nombre = models.CharField(max_length=100, help_text="Nombre") 
    apellido = models.CharField(max_length=100, help_text="Apellido")
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"