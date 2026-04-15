from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpRequest
from .models import Post

# Create your views here.

def home_view(request: HttpRequest):
    posts = Post.objects.filter(is_published=True).order_by('-published_at')
    return render(request, 'blog/home.html', {'posts': posts})


def add_post_view(request: HttpRequest):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('image')

        Post.objects.create(
            title=title,
            content=content,
            image=image
        )
        return redirect('blog:home_view')

    return render(request, 'blog/add_post.html')


def detail_post_view(request: HttpRequest, post_id: int):
    post = Post.objects.get(id=post_id)
    return render(request, 'blog/post_details.html', {'post': post})


def update_post_view(request: HttpRequest, post_id: int):
    post = Post.objects.get(id=post_id)

    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        image = request.FILES.get('image')
        if "image" in request.FILES: post.image = request.FILES['image']
        post.save()
        return redirect('blog:home_view')
    
    return render(request, 'blog/update_post.html', {'post': post})


def delete_post_view(request: HttpRequest, post_id: int):
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect('blog:home_view')
