from .models import Image
from django import forms

class ImagePostForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['like', 'post_on','user','profile']
  