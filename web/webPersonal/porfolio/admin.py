from django.contrib import admin
from .models import Proyect
# Register your models here.

class Proyect_admin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

admin.site.register(Proyect,Proyect_admin)