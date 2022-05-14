from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.

class Article(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name='article')
    title = models.CharField(max_length = 50)
    content = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to = 'article_images', null=True, blank=True)
    slug = models.SlugField(unique=True, max_length=100)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super(Article, self).save(*args, **kwargs)        

    class Meta:
        ordering = ['-created_date']

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete = models.CASCADE, related_name="comment")
    author = models.CharField(max_length = 50)
    content = models.CharField(max_length = 200)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author}:{self.content}"

    class Meta:
        ordering = ['-created_date']


