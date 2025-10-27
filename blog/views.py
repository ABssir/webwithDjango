from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404
from .models import Article, Category
from django.http import Http404
from django.core.paginator import Paginator
from account.models import User


class ArticleListView(ListView):
    # model = Article
    template_name = 'article_list.html'
    # context_object_name = "articles"
    queryset = Article.objects.published()
    paginate_by = 2



class CategoryListView(ListView):
    paginate_by = 4
    template_name = 'category_list.html'
   
    def get_queryset(self):
        slug = self.kwargs.get('slug')
        self.category = get_object_or_404(Category.objects.active(), slug=slug)
        return self.category.articles.published()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context



class ArticleDetailView(DetailView):
    template_name = 'blog/article_detail.html'

    def get_object(self):
        slug = self.kwargs.get('slug')
        return get_object_or_404(Article.objects.published(), slug=slug)
  
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article = self.get_object()
        context['categories_article'] = article.category.active()
        context['categories'] = Category.objects.active()  
        return context
