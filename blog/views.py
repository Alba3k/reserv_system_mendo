from django.views.generic import ListView, TemplateView, DetailView
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from . models import Post, Cat


class PostList(ListView):
    model = Post
    posts = Post.objects.filter(status='published')
    template_name = 'web/blog/list.html'
    context_object_name = 'posts'


class PostDetail(DetailView):
    model = Post
    template_name = 'web/blog/detail.html'
    context_object_name = 'post'