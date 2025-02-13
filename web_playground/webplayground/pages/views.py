from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Page
from django.contrib.admin.views.decorators import staff_member_required
from django.views.generic.list import ListView
from django.views.generic.detail import  DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from .forms import PageForm
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
# Create your views here.

class StaffRequireMixin(object):
    #paraa que el user sea miembro del staff
    @method_decorator(staff_member_required)
    def dispatch(self, request: HttpRequest, *args: reverse_lazy, **kwargs: reverse_lazy) -> HttpResponse:
        return super(StaffRequireMixin,self).dispatch(request, *args, **kwargs)

class PageListViews(ListView):
    model = Page


class Page_Detail_view(DetailView):
    model = Page

@method_decorator(staff_member_required,name='dispatch')
class PageCreateView(CreateView):
    model = Page
    form_class =PageForm
    success_url = reverse_lazy('pages:pages')

@method_decorator(staff_member_required,name='dispatch')
class PageUpdateView(UpdateView):
    model = Page
    fields = ["title",'content','order']
    template_name_suffix = "_update_form"
    def get_success_url(self):
        return reverse_lazy('pages:update',args=[self.object.id]) + '?ok'


@method_decorator(staff_member_required,name='dispatch')
class PageDeleteView(DeleteView):
    model = Page
    success_url = reverse_lazy("pages:pages")