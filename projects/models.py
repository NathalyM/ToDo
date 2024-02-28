from django.db import models

# Create your models here.
class Project(models.Model):
    titulo = models.CharField(max_length=200)
    comentario = models.TextField()
    usuario = models.TextField()
    fecha_crea =models.DateField(auto_now_add=True)
