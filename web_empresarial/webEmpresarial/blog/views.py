from django.shortcuts import render , get_object_or_404
from .models import Post, Categoria
# Create your views here.

def blog(request):
    post = Post.objects.all()
    return render(request,"blog/blog.html", {"post": post})

def category(request, category_id):
    category = get_object_or_404(Categoria, id= category_id)
    # post = Post.objects.filter(categories = category)
    return render(request, "blog/category.html", {'category': category})