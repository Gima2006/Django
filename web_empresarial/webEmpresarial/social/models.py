from django.db import models

# Create your models here.

class Link(models.Model):
    key = models.SlugField(verbose_name='Nombre clave',max_length=100 , unique=True)
    name =  models.CharField(verbose_name='Red social',max_length=200)
    url = models.URLField(verbose_name='Enlace',max_length=200, null=True,blank=True)
    created = models.DateField(auto_now_add=True,verbose_name="Fecha de creacion")
    updated =  models.DateField(auto_now=True,verbose_name="Fecha de edicion")
    class Meta:
        verbose_name = 'Enlaces'
        verbose_name_plural = "enlaces"
        ordering = ['name']
    
    def __str__(self) -> str:
        return self.name
    pass
    