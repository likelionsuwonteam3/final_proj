from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .models import Blog
def home(request): 
    return render(request, 'home.html')
def detail(request):
    blogs = Blog.objects
    return render(request, 'detail.html', {'blogs': blogs})
def more(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'more.html', {'blog': blog_detail})
def new(request):
    return render(request, 'new.html')
def create(request):
    blog = Blog() # 블로그 객체 생성
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/' + str(blog.id))