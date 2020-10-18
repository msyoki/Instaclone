from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Image,Profile
from .forms import ImagePostForm,ProfileForm


# Create your views here.
@login_required(login_url='/accounts/login/')  
def home(request):
    images = Image.objects.all()
    profiles = Profile.objects.all()
    return render(request,'Instaclone/index.html',{"images":images,"profiles":profiles})


def new_image(request):
    current_user = request.user
    if request.method == 'POST':
        form = ImagePostForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
        return redirect('/')

    else:
        form = ImagePostForm()
    return render(request, 'Instaclone/new_image.html', {"form": form})

def new_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return redirect('/')

    else:
        form = ProfileForm()
    return render(request, 'Instaclone/new_profile.html', {"form": form})