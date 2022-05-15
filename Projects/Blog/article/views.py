from django.shortcuts import get_object_or_404, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import View
from django.views.generic.edit import DeleteView, FormView, UpdateView

from django.views.generic.base import TemplateView, View
from django.views.generic import DetailView
from django.views.generic.list import ListView

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from article.forms import ArticleForm, CommentForm
from article.models import Article, Comment
from django.shortcuts import redirect

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

class ArticleDetailView(View):

    def get(self, request, *args, **kwargs):
        context = {}
        context['form'] = CommentForm()
        pk = kwargs.get('pk')
        article = Article.objects.get(pk=pk)

        context['article'] = article
        context['comments'] = Comment.objects.filter(article = article)

        return render(request, template_name='article/detail.html', context=context)

    @method_decorator(login_required())
    def post(self, request, *args, **kwargs):
        author = request.user.username
        pk = kwargs.get('pk')
        article = Article.objects.get(pk=pk)

        form = CommentForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
            comment = Comment(author=author,content=content, article=article)
            comment.save()
            return redirect(request.path_info)
        else:
            return render(request, 'article/message.html',{'login_message':'You must login to comment.'})
        
    
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

class CommentCreateView(LoginRequiredMixin, FormView):
    template_name = 'form.html'
    form_class = CommentForm
    
    def get(self, request, *args, **kwargs):
        print(self.request.user.article)
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        user = self.request.user

        self.success_url = self.request.path_info
        content = form.cleaned_data['content']

        comment = Comment(author=user, content=content)

        return super().form_valid(form)

class CommentUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'article/detail.html' 
    form_class = CommentForm
    queryset = Comment.objects.all()

    def get_context_data(self, **kwargs):
        pk = self.kwargs['pk']
        context =super().get_context_data(**kwargs)
        comment = Comment.objects.get(pk=pk)
        
        article = comment.article
        context['article'] =article
        #context['form'] = CommentForm()
        context['comments'] = Comment.objects.filter(article = article)
        return context

    def get(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        comment = Comment.objects.get(pk=pk)
        
        user = request.user
        author = comment.author
        if user.username == author:
            return super().get(request, *args, **kwargs)
        else:
            message = "You can only update the comment you have written."
            return render(request,'article/message.html',{"comment_update":message})


    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        comment = get_object_or_404(Comment,pk=pk)
        article_pk = comment.article.pk
        self.success_url = f'/blog-detail/{article_pk}'
        return super().post(request, *args, **kwargs)

class CommentDeleteView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        user =request.user
        pk = kwargs.get('pk')
        comment = get_object_or_404(Comment,pk=pk)
        author = comment.author
        article_pk = comment.article.pk
        comment.delete()
        if user.username == author:
            return redirect(f'/blog-detail/{article_pk}')
        else:
            message = "You can only delete the comment you have written."
            return render(request,'article/message.html',{"comment_update":message})

