from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Image(models.Model):
    image=models.ImageField(upload_to='photos')
    name=models.CharField(max_length=20)
    caption=models.CharField(max_length=50)
    like=models.IntegerField(null=True)
    username=models.ForeignKey(User,on_delete=models.CASCADE)
    post_on = models.DateTimeField(auto_now_add= True,null=True)


    def __str__(self):
        return self.username


class Profile(models.Model):
    profile_pic = models.ImageField(upload_to= 'profile_pic/')
    name = models.CharField(max_length=150,null=True)
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    email= models.EmailField(null=True)
    bio = models.TextField(max_length = 50, blank= True)
        
    def __str__(self):
        return self.name

    @classmethod
    def search_profile(cls,search_term):
        profiles = cls.objects.filter(username__username=search_term)
        return profiles

class Comment(models.Model):
    username = models.ForeignKey(User,on_delete = models.CASCADE)
    Image = models.ForeignKey(Image,on_delete = models.CASCADE)
    comment = models.CharField(max_length= 70)
    post_on = models.DateTimeField(auto_now_add= True)