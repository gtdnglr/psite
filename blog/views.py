from django.shortcuts import render
from .models import Post
from django.views.generic import DetailView

def tesat(request):
    return render(request, 'blog/blog.html', {})

def blog_home(request):
    result = Post.objects.filter(status=1).order_by('-created_on')

    if result.exists():
        context = {'pf': result[0], 'prt': result[1:4], 'prb': result[4:11], }
        return render(request, 'blog/blog.html', context)
    else:
        return render(request, 'blog/blog.html', {'pf' : ''})

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post.html'
