from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from PIL import Image

class Category(models.Model):
    title = models.CharField(max_length=25, verbose_name='Category Title')
    created_on = models.DateTimeField(auto_now_add=True, verbose_name='Created On')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['-created_on',]

class Post(models.Model):
    STATUS_CHOICES = (
        (0, 'Draft'),
        (1, 'Published'),
    )
    category = models.ForeignKey(Category, verbose_name='Category', on_delete=models.SET('category'))
    author = models.ForeignKey(User, verbose_name='Author', on_delete=models.SET('author'))
    status = models.IntegerField(choices=STATUS_CHOICES, default='draft')
    title = models.CharField(max_length=58, null=False, default='', unique=True, verbose_name='Post Title')
    description = models.CharField(max_length=120, null=False, default='', verbose_name='Post Description')
    slug = models.SlugField(max_length=120, null=False, unique=True, verbose_name='Post URL Slug')
    content = models.TextField(verbose_name='Post Content')
    featured_image = models.ImageField(upload_to='image/', verbose_name='Featured Image (800x570)')
    created_on = models.DateTimeField(auto_now_add=True, verbose_name='Created On')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-created_on',]

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.CharField(max_length=80, default='', null=False)
    email = models.EmailField(default='', null=False)
    content = models.TextField(default='', null=False)
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=True)
    test = models.TextField(default='')

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        ordering = ['-created_on',]

    def __str__(self):
        return f'{self.author} commented on {self.post}'
