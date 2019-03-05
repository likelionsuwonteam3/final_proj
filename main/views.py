from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .models import Portfolio
from .models import Blog

def home(request): 
    portfolios = Portfolio.objects
    return render(request, 'home.html',{'portfolios': portfolios})
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

def portfolio(request):
    portfolios = Portfolio.objects
    return render(request, 'portfolio.html',{'portfolios': portfolios})

def create_port(request):
    portfolio = Portfolio(image= request.FILES['image']) # 블로그 객체 생성
    portfolio.title = request.POST['title']
    # portfolio.image = request.['image']
    portfolio.description = request.POST['description']
    portfolio.save()
    return redirect('/')