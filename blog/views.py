from django.shortcuts import render
from .models import Post
from django.views.generic import DetailView

def tesat(request):
    return render(request, 'blog/blog.html', {})

def blog_home(request):
    posts = Post.objects.filter(status=1).order_by('-created_on')

    if posts.exists():
        context = {'pf': posts[0], 'prt': posts[1:4], 'prb': posts[4:11], }
        return render(request, 'blog/blog.html', context)
    else:
        return render(request, 'blog/post.html', {'error' : ''})

class BlogPost(DetailView):
    model = Post
    template_name = 'blog/post.html'
    slug_url_kwarg = 'post_slug'
    slug_field = 'slug'
