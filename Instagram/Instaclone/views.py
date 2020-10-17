from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Image,Profile,Comment
from .forms import ImagePostForm
from django.http import HttpResponseRedirect

# Create your views here.
@login_required(login_url='/accounts/login/')  
def home(request):
    images = Image.get_all_images()
    profiles = Profile.get_all_profiles()
    comments = Comment.get_all_comments()
    return render(request,'Instaclone/index.html',{"images":images,"profiles":profiles,"comments":comments})


def new_image(request):
    current_user = request.user
    if request.method == 'POST':
        form = ImagePostForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
        return HttpResponseRedirect('post')

    else:
        form = ImagePostForm()
    return render(request, 'Instaclone/new_image.html', {"form": form})