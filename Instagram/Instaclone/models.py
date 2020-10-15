from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Image(models.Model):
    image=models.ImageField(upload_to='photos',null=True)
    image_name=models.CharField(max_length=20)
    image_caption=models.CharField(max_length=50)
    like=models.IntegerField(default=0)
    profile=models.ForeignKey(User,on_delete=models.CASCADE)


class Profile(models.Model):
    profile_pic = models.ImageField(upload_to= 'profile_pic/', null= True, blank= True)
    first_name = models.CharField(max_length =30,blank=True)
    last_name = models.CharField(max_length =30,blank=True)
    bio = models.TextField(max_length = 50, blank= True)


class Comment(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    Image = models.ForeignKey(Image,on_delete = models.CASCADE)
    comment = models.CharField(max_length= 70)
    post_on = models.DateTimeField(auto_now_add= True)