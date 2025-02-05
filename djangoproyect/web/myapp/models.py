from django.db import models

# Create your models here.

class Proyect(models.Model):
    name = models.CharField(max_length=2)

class Task(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    proyecto = models.ForeignKey(Proyect, on_delete= models.CASCADE)