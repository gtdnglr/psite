from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from blog import views

urlpatterns = [
    path('', views.blog_home, name='view_blog_home'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
