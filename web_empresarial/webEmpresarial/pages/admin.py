from django.contrib import admin

# Register your models here.

from .models import Page

class Page_admin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_display = ("title",'order')
    

admin.site.register(Page,Page_admin)