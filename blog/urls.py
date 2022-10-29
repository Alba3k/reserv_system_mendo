from django.views.generic import ListView, TemplateView, DetailView
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path

from . views import PostList, PostDetail


urlpatterns = [
    path('', PostList.as_view(), name='blog_list'),
    path('<slug:slug>/', PostDetail.as_view(), name='blog_detail'),
]