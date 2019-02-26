from django.shortcuts import render
from .models import Blog
# Create your views here.
def home(request): 
    return render(request, 'home.html')
def detail(request):
    blogs = Blog.objects
    return render(request, 'detail.html', {'blogs': blogs})