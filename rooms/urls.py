from django.views.generic import ListView, TemplateView, DetailView
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path

from . views import HomePage, CatalogPage, search, show_room
from . models import Room, Type

urlpatterns = [

    path('', HomePage.as_view(), name='index'),

    path('catalog/', CatalogPage.as_view(), name='catalog'),
    path('catalog/<slug:room_slug>/', show_room, name='room_detail'),

    path('search/', search, name='search_room'),
    path('search/<slug:room_slug>/', show_room, name='room_detail'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)