from django.contrib import admin
from .models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_on', )
    search_fields = ['title', ]

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on', )
    list_filter = ('status', 'author', )
    search_fields = ['title', 'author', ]
    prepopulated_fields = {'slug': ('title',)}

class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'approved', 'created_on', 'author','content', )
    list_filter = ('approved', )
    search_fields = ['post','author','content', ]

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
