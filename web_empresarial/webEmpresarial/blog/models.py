from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
# Create your models here.

class Categoria(models.Model):
    
    name = models.CharField(max_length=100, verbose_name="Nombre")
    created = models.DateField(auto_now_add=True,verbose_name="Fecha de creacion")
    updated =  models.DateField(auto_now=True,verbose_name="Fecha de edicion")
    
    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = "categorias"
        ordering = ['-created']
    
    def __str__(self) -> str:
        return self.name
    pass


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name="Entradas")
    content = models.TextField(verbose_name="contenido")
    published = models.DateTimeField(verbose_name="Fecha de publicacion",default= now)
    image = models.ImageField(verbose_name="imagen", upload_to="blog", null=True, blank=True)
    author = models.ForeignKey(User, verbose_name="autor", on_delete=models.CASCADE)
    categories = models.ManyToManyField(Categoria, verbose_name="Categorias", related_name='get_post')
    created = models.DateField(auto_now_add=True,verbose_name="Fecha de creacion")
    updated =  models.DateField(auto_now=True,verbose_name="Fecha de edicion")
    
    class Meta:
        verbose_name = 'Entrada'
        verbose_name_plural = "Entradas"
        ordering = ['-created']
    
    def __str__(self) -> str:
        return self.title
    pass
    