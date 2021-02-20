from django.shortcuts import render
from .models import Post
from django.views.generic import DetailView

def view_blog(request):
    blog_posts = Post.objects.filter(status=1).order_by('-created_on')

    if blog_posts.exists():
        context = {'post_newest': blog_posts[0], 'posts_top': blog_posts[1:4], 'posts_bottom': blog_posts[4:10], }
        return render(request, 'blog/blog.html', context)
    else:
        return render(request, 'blog/blog.html', {'error' : ''})

def view_post(request, slug):
    blog_post = Post.objects.get(slug=slug)

    context = {'post': blog_post }
    return render(request, 'blog/post.html', context)
