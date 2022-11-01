from django.views.generic import ListView, TemplateView, DetailView
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from . models import Post, Cat


class PostList(ListView):
    queryset = Post.objects.filter(status='published')
    paginate_by=6
    template_name = 'web/blog/list.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        cat = Cat.objects.all()
        context = super().get_context_data(**kwargs)
        context['cat'] = cat
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'web/blog/detail.html'
    context_object_name = 'post'