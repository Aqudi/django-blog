from django.shortcuts import render, redirect, get_object_or_404
from .models import *

# Create your views here.
def home(request, page_number=1):
    blogs = Blog.objects.all().order_by('-id')

    page_n = blogs.count() // 5 + 1
    if blogs.count() % 5:
        page_n = blogs.count() // 5 + 2

    ranges = list(range(1, page_n))
    start = 0 + (page_number-1) * 5
    end = page_number * 5
    return render(request, 'home.html', {'blogs':blogs[start:end], 'range':ranges, "page":page_n-1, "current":page_number})

def homed(request):
    blogs = Blog.objects.all().order_by('-id')
    page_number = 1
    page_n = blogs.count() // 5 + 1
    if blogs.count() % 5:
        page_n = blogs.count() // 5 + 2

    ranges = list(range(1, page_n))
    start = 0 + (page_number-1) * 5
    end = page_number * 5
    return render(request, 'home.html', {'blogs':blogs[start:end], 'range':ranges, "page":page_n-1, "current":page_number})


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