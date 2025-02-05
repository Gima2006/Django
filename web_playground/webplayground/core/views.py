from typing import Any
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render
from django.views.generic.base import TemplateView


class HomePageView(TemplateView):
    template_name ="core/home.html"
    
#    def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)
#       context["latest_articles"] = Article.objects.all()[:5]
#       return context
    
    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        return render(request, self.template_name,{'title':'Mi APP de playground'})
   

class SamplePageView(TemplateView):
    template_name ="core/sample.html"
   
   
