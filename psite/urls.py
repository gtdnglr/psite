from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from resume import views

urlpatterns = [
    path('', RedirectView.as_view(url='resume/')),
    path('admin/', admin.site.urls),
    path('resume/', views.view_resume, name='v_resume'),
    path('aboutme/', views.view_aboutme, name='v_aboutme'),
    path('blog/', include('blog.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
