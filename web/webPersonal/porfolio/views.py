from django.shortcuts import render
from .models import Proyect
# Create your views here.

def porfolio(request):
    proyects = Proyect.objects.all()
    return render(request,"porfolio/porfolio.html", {'proyects': proyects})
