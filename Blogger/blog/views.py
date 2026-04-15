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

        Post.objects.create(
            title=title,
            content=content
        )
        return redirect('blog:home_view')

    return render(request, 'blog/add_post.html')