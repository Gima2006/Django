from django.contrib import admin
from .models import Categoria,Post
# Register your models here.

class Categoria_Admin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    
class Post_Admin(admin.ModelAdmin):

    readonly_fields = ('created','updated')
    list_display = ("title","author","published","post_categories")
    ordering = ("author", "published")
    search_fields = ("title","content","categories__name")
    date_hierarchy = "published"
    list_filter = ['author__username',"categories__name"]
    
    def post_categories(self,obj)-> str:
        return ", ".join(c.name for c in obj.categories.all().order_by("name"))
     
    post_categories.short_description = "Categoria"
    
   

admin.site.register(Categoria,Categoria_Admin)

admin.site.register(Post,Post_Admin)