from django.views.generic import ListView, TemplateView, DetailView
from django.conf.urls.static import static
from django.urls import path, re_path
from django.conf import settings

from . views import reserved


urlpatterns = [

    path('', reserved, name='reserved'),

#     # path('new/<room>', views.user),
#     # path('', TemplateView.as_view(template_name='web/catalog.html'), name='bookings'),
#     # path('', wizard_book, name='bookings'),
#     # path('/', views.HomePageView.as_view(), name='home'),
#     # path('', views.IndexPageView.as_view(), name='index'),
#     # path('catalog/', views.catalog_view, name='catalog_rooms'),
#     # path('catalog/<int:pk>/', views.ShowRoom.as_view(), name='room_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)