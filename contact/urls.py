from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import contact_view

app_name = 'contact'

urlpatterns = [
    path('', contact_view, name='contact'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

