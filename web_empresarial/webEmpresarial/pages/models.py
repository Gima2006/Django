from django.db import models

# Create your models here.

class Page(models.Model):
    title =  models.CharField(verbose_name='Titulo',max_length=200)
    content = models.TextField(verbose_name='Contenido')
    order = models.SmallIntegerField(verbose_name="Orden",default=0)
    created = models.DateField(auto_now_add=True,verbose_name="Fecha de creacion")
    updated =  models.DateField(auto_now=True,verbose_name="Fecha de edicion")
    class Meta:
        verbose_name = 'pagina'
        verbose_name_plural = "paginas"
        ordering = ['order','title']
    
    def __str__(self) -> str:
        return self.title

    