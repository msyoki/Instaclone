from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .models import Image,Profile,Comment
from django.urls import reverse_lazy,reverse
from .forms import ImagePostForm,ProfileForm,CommentForm


# Create your views here.
@login_required(login_url='/accounts/login/')  
def home(request):
    images = Image.objects.all()
    profiles = Profile.objects.all()
    return render(request,'Instaclone/index.html',{"images":images,"profiles":profiles})

@login_required(login_url='/accounts/login/')
def new_image(request):
    if request.method == 'POST':
        form = ImagePostForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save()
            image.save()
        return redirect('/')

    else:
        form = ImagePostForm()
    return render(request, 'Instaclone/new_image.html', {"form": form})

@login_required(login_url='/accounts/login/')
def new_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save()
            profile.save()
        return redirect('/')

    else:
        form = ProfileForm()
    return render(request, 'Instaclone/new_profile.html', {"form": form})


@login_required(login_url='/accounts/login/')
def search_results(request):
    if 'user' in request.GET and request.GET["user"]:
        search_term = request.GET.get("user")
        searched_users = Profile.search_profile(search_term)
        message=f"{search_term}"

        return render(request,'Instaclone/search.html',{"message":message,"users":searched_users})

    else:
        message="You haven't searched for any term"
        return render(request,'Instaclone/search.html',{"message":message})


@login_required(login_url='/accounts/login/')
def profile(request,profile_id):
    current_user=request.user

    try:
        all_images=Image.objects.all()
        profile = Profile.objects.get(id=profile_id)
        username = profile.username
        images = Image.objects.filter(username=username)
    except:
        raise ObjectDoesNotExist()
    return render(request,"Instaclone/profile.html",{"profile":profile,"images":images})



@login_required(login_url='/accounts/login/')
 # if this is a POST request we need to process the form data
def new_comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save()
            comment.save()
        return redirect('/')
    else:
        form = CommentForm()
    return render(request, 'Instaclone/new_comment.html', {"form": form})
