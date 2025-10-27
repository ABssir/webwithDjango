from django.db import models
from django.urls import reverse
from django.utils import timezone
from django_jalali.db import models as jmodels
from account.models import User
from django_ckeditor_5.fields import CKEditor5Field

# my manager
class ArticleManager(models.Manager):
    def published(self):
        return self.filter(status="p")


class CategoryManager(models.Manager):
    def active(self):
        return self.filter(status=True)


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, unique=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title
        
    def article_count(self):
        return self.articles.published().count()

    objects = CategoryManager()


class Article(models.Model):
    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Published')
    )
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name="articles")
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, unique=True)
    category = models.ManyToManyField(Category, related_name="articles")
    description = CKEditor5Field('Text', config_name='extends')
    thumbnail = models.ImageField(upload_to="")
    publish = jmodels.jDateTimeField(default=timezone.now)
    created = jmodels.jDateTimeField(auto_now_add=True)
    update = jmodels.jDateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='d')
    reading_time_minutes = models.IntegerField()

    def __str__(self):
        return self.title

    



    def category_to_str(self):
        return ", ".join([category.title for category in self.category.active()])

    objects = ArticleManager()

    class Meta:
        ordering = ["-publish"]
