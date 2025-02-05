from django.contrib import admin
from .models import Service
# Register your models here.

class Service_admin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    

admin.site.register(Service,Service_admin)