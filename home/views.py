from django.views.generic import ListView
from django.shortcuts import render
from blog.models import Article

class HomeView(ListView):
    template_name = "home/home.html"
    context_object_name = 'latest_articles'

    def get_queryset(self):
        return Article.objects.published()[:3]


def HomeRoadmap(request):
    return render(request, "home/roadmap.html")