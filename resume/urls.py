from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from resume import views

urlpatterns = [
    path('', views.view_resume, name='v_resume'),
    path('aboutme/', views.view_resume, name='v_aboutme'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

