from .models import Post
from .forms import CreatePost
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'posts/index.html', {
        'posts': Post.objects.all().order_by('-date')
    })

def page(request, slug):
    return render(request, 'posts/page.html', {
        'post': Post.objects.get(slug=slug)
    })
    
@login_required(login_url='/users/login/')
def create(request):
    form = CreatePost()
    if request.method == "POST":
        form = CreatePost(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('posts:index')
            
    return render(request, 'posts/create.html', {'form': form})
