from django.shortcuts import render,get_object_or_404
from .models import Catagory, Post, ContactUs
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
   if request.method == "POST":
      # data from the form 
      # ***********************************
      name = request.POST.get('name')
      email = request.POST.get('email')
      subject = request.POST.get('subject')
      message = request.POST.get('message')
   # ***********************************
      contact = ContactUs()
      print("######################################")
      print(contact)
      contact.name = name
      contact.email = email
      contact.subject = subject
      contact.message = message
      contact.save()
      print(contact)
      
      print("######################################")
   return render(request,'contact.html')


def service(request):
   return render(request,'service.html')
