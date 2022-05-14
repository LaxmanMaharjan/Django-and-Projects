from django.contrib import admin
from .models import Article, Comment

# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['author','title','content','created_date','slug']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['article','author','content','created_date']
