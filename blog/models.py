from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify
from django.contrib.auth.models import User
from PIL import Image

status_post = (
    (0,'Draft'),
    (1,'Publish')
)

class Category(models.Model):
    title = models.CharField(max_length=25, verbose_name='Category Title')
    created_on = models.DateTimeField(auto_now_add=True, verbose_name='Created On')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['title',]

class Post(models.Model):
    category = models.ForeignKey('Category', verbose_name='Category', on_delete=models.SET(''))
    author = models.ForeignKey(User, verbose_name='Author', on_delete=models.SET('deleted user'))
    status = models.IntegerField(choices=status_post, default=0)
    title = models.CharField(max_length=59, null=False, default='Post Title', unique=True, verbose_name='Post Title')
    snippet = models.CharField(max_length=120, null=False, default='Post Snippet', verbose_name='Post Snippet')
    slug = models.SlugField(max_length=65, null=False, unique=True, verbose_name='Post URL Slug')
    content = RichTextUploadingField(verbose_name='Post Content')
    featured_image = models.ImageField(upload_to='image/', verbose_name='Featured Image (800x570)')
    created_on = models.DateTimeField(auto_now_add=True, verbose_name='Created On')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-created_on',]

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        if self.slug.endswith('/'):
            self.slug = self.slug[:-1]
        super(Post, self).save(*args, **kwargs)

        Image.open(self.featured_image.path)\
            .resize((800, 570), Image.ANTIALIAS)\
            .save(self.featured_image.path, format='JPEG', dpi=[72, 72])
