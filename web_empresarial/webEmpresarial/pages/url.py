from django.urls import path
from . import views as sample_views

urlpatterns = [
 
    path('<int:page_id>/', sample_views.pages, name = "page")  

]