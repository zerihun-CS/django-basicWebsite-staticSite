from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Catagory(models.Model):
   title = models.CharField(max_length=23)
   def __str__(self) -> str:
      return self.title
class Post(models.Model):
   title = models.CharField(max_length=100)
   description = models.TextField()
   image = models.ImageField()
   catagory = models.ForeignKey(Catagory, on_delete=models.CASCADE)
   author = models.ForeignKey(User, on_delete=models.CASCADE)
   date = models.DateTimeField(auto_now=True)
   
   def __str__(self) -> str:
      return self.title
   
class ContactUs(models.Model):
   name = models.CharField(max_length=50)
   email = models.EmailField()
   subject = models.CharField(max_length=100)
   message = models.TextField()
   gender = models.CharField(max_length=10,default="Male" )
   def __str__(self) -> str:
      return self.name + " "+self.email