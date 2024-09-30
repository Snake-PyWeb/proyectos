from django.db import models
from django.contrib.auth.models import User # importamos esta libreria para hacer la relacion entre la tabla User del admin de django con las publicaciones de los post esto para que se meustre el nombre en cada post


# Create your models here.

class post(models.Model):
    titulo=models.CharField(max_length=200)
    descripcion=models.TextField()
    fecha_creacion=models.DateTimeField(auto_now_add=True)
    fecha_actualizacion=models.DateTimeField(auto_now=True)
    autor=models.ForeignKey(User,on_delete=models.CASCADE) # relacion con la tabla user del admin de django para saber quien creo el post
    



