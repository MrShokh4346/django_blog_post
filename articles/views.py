from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView ,CreateView
from .models import Post
from django.urls import reverse_lazy
# Create your views here.

class ArticleListView(ListView):
    model = Post
    template_name = 'articlelist.html'

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_detail.html'

class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'article_edit.html'
    fields = ['title', 'summary', 'body', 'photo']
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
    
class ArticleDeleteView(LoginRequiredMixin,  DeleteView):
    model = Post
    template_name = 'article_delete.html'
    success_url = reverse_lazy('articlelist')
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class ArticleCreateView(LoginRequiredMixin,  CreateView):
    model = Post
    fields = ['title', 'summary','body', 'photo', ]
    template_name = 'article_new.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def test_func(self):
        return self.request.user.is_superuser


