from django.contrib import admin
from .models import Article, Category


# Register your models here.
def make_published(modeladmin, request, queryset):
    rows_updated = queryset.update(status="p")
    if rows_updated == 1:
        massage_bit = 'make_published'
    else:
        massage_bit = "makes_published"
    modeladmin.message_user(request, "{} *articles* {}".format(rows_updated, massage_bit))


def make_draft(modeladmin, request, queryset):
    queryset.update(status="d")


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status')
    list_filter = (['status'])
    search_fields = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['status']


admin.site.register(Category, CategoryAdmin)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'publish', 'author', 'status', 'category_to_str')
    list_filter = ('publish', 'status', 'author')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['-status', '-publish']
    actions = [make_published, make_draft]


admin.site.register(Article, ArticleAdmin)
