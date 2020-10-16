from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Image

# Create your views here.
@login_required(login_url='/accounts/login/')  
def home(request):
    images = Image.get_all_images()
    return render(request,'Instaclone/index.html',{"images":images})
