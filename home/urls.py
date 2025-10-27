from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import HomeView, HomeRoadmap

app_name = 'home'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('roadmap/', HomeRoadmap, name='roadmap'),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)