from django.shortcuts import render, get_object_or_404, Http404
from blog.models import Article


class FieldsMixin():
    """Verify that the current user is authenticated."""

    def __init__(self):
        self.fields = None

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            self.fields = [
                'title', 'thumbnail', 'slug', 'author', 'category', 'description', 'publish', 'reading_time_minutes',
                'status'
            ]
        elif request.user.is_author:
            self.fields = [
                'title', 'thumbnail', 'slug', 'category', 'description', 'publish', 'reading_time_minutes',
            ]
        else:
            raise Http404('You cant see')
        return super().dispatch(request, *args, **kwargs)


class FormValidMixin():
    def form_valid(self, form):
        # if self.request.user.is_superuser:
        #     from.save()

        if self.request.user.is_author:
            self.obj = form.save(commit=False)
            self.obj.author = self.request.user
            self.obj.status = 'd'
        return super().form_valid(form)


class AutherAccessMixin():
    def dispatch(self, request,pk,  *args, **kwargs):
        article = get_object_or_404(Article,pk=pk)
        if article.author == request.user and article.status == 'd' or request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404('You cant see')


class SuperUserAccessMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404('You cant see')
