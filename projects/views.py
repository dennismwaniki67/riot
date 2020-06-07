from django.shortcuts import render, redirect,get_object_or_404
from django.views.generic import ListView, DetailView
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse_lazy
from .forms import PostForm,ProfileForm,UserRegisterForm
from django.views import generic
from .models import *
from django.db.models import Avg


# Create your views here.


class PostListView(ListView):
    model = Post
    template_name = 'projects/index.html'


class PostDetailView(DetailView): 
    model = Post
    template_name = 'post_detail.html'

    
class SignUpView(generic.CreateView):
    form_class = UserRegisterForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

def profile(request):
    current_user = request.user
    profile = Profile.objects.filter(user=current_user).first()
    posts = request.user.post_set.all()

    return render(request, 'projects/profile.html', locals())

def updateprofile(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            add = form.save(commit=False)
            add.user = current_user
            add.save()
            return redirect('profile')
    else:
        form = ProfileForm()
    return render(request, 'projects/profile_update.html',{"form":form })


def post_new(request):
    current_user = request.user
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
        return redirect('home')
    else:
        form = PostForm()
    return render(request, 'projects/post_new.html', {"form": form})

def search_results(request):

    if 'post' in request.GET and request.GET["post"]:
        search_term = request.GET.get("post")
        searched_posts = Post.search(search_term)
        message = f"{search_term}"

        return render(request, 'projects/search.html',{"message":message,"posts": searched_posts})

    else:
        message = "You haven't searched for any term"
        return render(request, 'projects/search.html',{"message":message})

def vote(request,post_id):
    try:
        post = Post.objects.get(id = post_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"projects/vote.html", {"post":post})