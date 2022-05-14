from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import View
from django.views.generic.edit import DeleteView, FormView, UpdateView

from django.views.generic.base import TemplateView, View
from django.views.generic import DetailView
from django.views.generic.list import ListView

from article.forms import ArticleForm
from article.models import Article

# Create your views here.
class HomeView(ListView):
    template_name = 'article/index.html'
    model = Article
    context_object_name = 'articles'


class DashboardView(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user
        context = {
                'articles':user.article.all(),
                'username':user.username,
                }
        print("username")
        print(user.username)
        print(context)
        return render(request,'article/dashboard.html', context=context)

class CreateArticleView(LoginRequiredMixin, FormView):
    template_name = 'form.html' 
    success_url = '/'
    form_class = ArticleForm

    def form_valid(self, form):
        user = self.request.user
        title = form.cleaned_data['title']
        content = form.cleaned_data['content']
        image = form.cleaned_data['image']
        

        article = Article(author=user, title=title, content=content, image=image, slug=title)
        article.save()

        return super().form_valid(form)

class ArticleDetailView(DetailView):
    template_name = 'article/detail.html'
    model = Article
    context_object_name = 'article'
    
class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'form.html' 
    form_class = ArticleForm
    model = Article

    def post(self, request, *args, **kwargs):
        pk = kwargs.get(self.pk_url_kwarg)
        self.success_url = f'/blog-detail/{pk}'
        return super().post(request, *args, **kwargs)

class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Article
    template_name = 'article/delete.html'
    success_url = '/dashboard'
    context_object_name = 'article'
