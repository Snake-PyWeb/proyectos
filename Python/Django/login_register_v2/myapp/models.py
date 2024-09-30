from django.db import models

# Create your models here.

class Posts(models.Model):
    titulo=models.CharField(max_length=200)
    contenido=models.TextField()
    fecha_creacion=models.DateTimeField(auto_now_add=True) # Fecha de creacion
    fecha_actualizacion= models.DateTimeField(auto_now=True)# Fecha de Actualizacion 
    
    def __str__(self): # Esta funcion sirve para mostrar variables de la base de datos o campos 
        return self.titulo  # Devuelve el título del post como representación del objeto