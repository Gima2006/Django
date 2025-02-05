from django.db import models

# Create your models here.

class Proyect(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulo")
    descripcion =models.TextField(verbose_name="Descripcion")
    image = models.ImageField(verbose_name="Imagen",upload_to="media/Proyects")
    link = models.URLField(verbose_name="Direccion web",null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creacion")
    updated = models.DateTimeField(auto_now=True,verbose_name="Modificado") 
   
    class Meta:
        verbose_name ="Proyecto"
        verbose_name_plural = "Proyectos"
        ordering = ["-created"]
    def __str__(self) -> str:
        return self.title