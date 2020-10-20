from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Image(models.Model):
    image=models.ImageField(upload_to='photos')
    name=models.CharField(max_length=150)
    caption=models.CharField(max_length=200)
    like=models.IntegerField(default=0)
    username=models.ForeignKey(User,on_delete=models.CASCADE)
    post_on = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.name


class Profile(models.Model):
    profile_pic = models.ImageField(upload_to= 'profile_pic/')
    name = models.CharField(max_length=150)
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
    image = models.ForeignKey(Image,related_name='comments',on_delete = models.CASCADE)
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    body = models.TextField()
    post_on = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return '%s - %s' % (self.image.name, self.username)
