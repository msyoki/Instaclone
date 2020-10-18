from .models import Image,Profile
from django import forms

class ImagePostForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['like', 'post_on','user','profile']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['']
  