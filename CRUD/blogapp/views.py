from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.utils import timezone
from django.core.paginator import Paginator
# Create your views here.
def home(request):
    blogs = Blog.objects.all()
    paginator = Paginator(blogs, 5)
    page = request.GET.get('page', 1)
    blog_page = paginator.get_page(page)
    return render(request, 'home.html', {'blogs':blog_page})

def new(request):
    return render(request, 'new.html')

def create(request):
    if request.method == "POST":
        blog = Blog()
        blog.title = request.POST.get('title')
        blog.writer = request.POST.get('writer')
        blog.body = request.POST.get('body')
        blog.save()
        return redirect('home', 1)

def detail(request, id):
    blog = get_object_or_404(Blog, pk=id)
    return render(request, 'detail.html', {'blog':blog})

def edit(request, id):
    blog = get_object_or_404(Blog, pk=id)
    return render(request, 'edit.html', {'blog':blog})

def update(request, id):
    blog = get_object_or_404(Blog, pk=id)
    if request.method == "POST":
        blog.title = request.POST.get('title')
        blog.writer = request.POST.get('writer')
        blog.body = request.POST.get('body')
        blog.save()
        return redirect('home', 1)

def delete(request, id):
    blog = Blog.objects.get(id=id)
    blog.delete()
    return redirect('home', 1)