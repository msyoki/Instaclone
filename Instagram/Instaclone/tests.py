from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import Image, Profile
from django.contrib.auth.models import User


class ImageTestClass(TestCase):
    '''
        a class to test the profile instances and its methods
    '''
    
    # Set up method
    def setUp(self):
        self.user = User.objects.create(id=1,username='msyoki')
        self.image= Image(
        image='/static/photos/aphoto.jpeg',
        name='test',
        caption='test caption',
        likes=0,
        username=self.user,
        post_on='Oct. 21, 2020, 8:00 a.m.')

    def test_instance(self):
        '''
        Testing Instance
        '''
        self.assertTrue(isinstance(self.image,Image))

    def test_save_method(self):
        '''
        Testing save Image method
        '''
        self.image.save_image()
        image = Image.objects.all()
        self.assertTrue(len(image)>=1)

 

class ProfileTestClass(TestCase):
    '''
    a class to test the profile instances and its methods
    '''

    # Set up method
    def setUp(self):
        self.user = User.objects.create(id=1,username='msyoki')
        self.profile= Profile(
        profile_pic='/static/profile_pic/aphoto.jpeg',
        name='test',
        username=self.user,
        email='test@gmail.com',
        bio='testbio')
        
    
    def test_instance(self):
        '''
        Testing Instance
        '''
        self.assertTrue(isinstance(self.profile,Profile))

       
    def test_save_method(self):
        '''
        Testing save profile method
        '''
        self.profile.save_profile()
        self.profiles = Profile.objects.all()
        self.assertTrue(len(self.profiles)>=1)

