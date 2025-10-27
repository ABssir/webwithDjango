from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import ArticleListView, ArticleDetailView, CategoryListView

app_name = 'blog'

urlpatterns = [
    path('', ArticleListView.as_view(), name='blog'),
    path('page/<int:page>/', ArticleListView.as_view(), name='blog'),
    path('<slug:slug>/', ArticleDetailView.as_view(), name='detail'),
    path('category/<slug:slug>/', CategoryListView.as_view(), name='category'),
    path('category/<slug:slug>/page/<int:page>/', CategoryListView.as_view(), name='category'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)