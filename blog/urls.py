from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from blog import views

urlpatterns = [
    path('', views.view_blog, name='v_blog'),
    path("<slug:slug>/", views.view_post, name="v_post"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

