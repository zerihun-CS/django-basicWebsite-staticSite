from django.shortcuts import render,get_object_or_404
from .models import Catagory, Post
# Create your views here.

def home(request):
   
   return render(request, 'home.html')

def about(request):
   
   return render(request, 'about.html')

def blog(request):
   news = Post.objects.all()
   return render(request, 'blog.html',{'news':news})

def blog_detail(request, id):
   news = get_object_or_404(Post,id = id)
   # news = Post.objects.get(Post,id = id)
   # news = Post.objects.filter(Post,id = id).first()
   return render(request,'blog-single.html',{'news':news})


def contactus(request):
   return render(request,'contact.html')


def service(request):
   return render(request,'service.html')
