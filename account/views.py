from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import (
    FieldsMixin, 
    FormValidMixin, 
    AutherAccessMixin,
    SuperUserAccessMixin,
    )
from django.views.generic import (
    ListView, 
    CreateView, 
    UpdateView,
    DeleteView, 
)
from blog.models import Article


# Create your views here.
# @login_required
# def home(request):
#
# 	return render(request, 'registration/home.html',{'user': request.user})


class ArticleListView(LoginRequiredMixin, ListView):
    template_name = "registration/home.html"
    # queryset = Article.objects.published()

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Article.objects.all()
        else:
            return Article.objects.filter(author=self.request.user)


class ArticleCreateView(LoginRequiredMixin, FormValidMixin, FieldsMixin, CreateView):
    model = Article
    template_name = 'registration/blog-create-update.html'


class ArticleUpdateView(AutherAccessMixin, FormValidMixin, FieldsMixin, UpdateView):
    model = Article
    template_name = 'registration/blog-create-update.html'


class ArticleDeleteView(SuperUserAccessMixin, DeleteView):
    model = Article
    success_url = reverse_lazy("account:home")
    template_name = 'registration/blog-delete.html'
