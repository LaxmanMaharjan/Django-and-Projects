from django.urls import path
from .views import ArticleDeleteView, ArticleUpdateView, CommentDeleteView, CommentUpdateView, HomeView, ArticleDetailView, CreateArticleView, DashboardView

urlpatterns = [
        path("", HomeView.as_view(), name='home'),
        path("dashboard", DashboardView.as_view(), name='dashboard'),
        path("create-blog", CreateArticleView.as_view(), name='create-blog'),
        path("blog-detail/<int:pk>", ArticleDetailView.as_view(), name='blog-detail'),
        path("blog-update/<int:pk>", ArticleUpdateView.as_view(), name='blog-update'),
        path("blog-delete/<int:pk>", ArticleDeleteView.as_view(), name='blog-delete'),

        path("comment-update/<int:pk>", CommentUpdateView.as_view(), name='comment-update'),
        path("comment-delete/<int:pk>", CommentDeleteView.as_view(), name='comment-delete'),

        
        ]
