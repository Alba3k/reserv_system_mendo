from django.views.generic import TemplateView, ListView
from django.contrib.auth import views as auth_views
from django.urls import path, re_path, include
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings

from profiles import views as user_views
from profiles.views import pageNotFound


urlpatterns = [
    path('', include('rooms.urls')),
    path('blog/', include('blog.urls')),
    path('reservation/', include('bookings.urls')),
    path('contacts/', TemplateView.as_view(template_name='web/contacts.html'), name='contacts'),

    path('admin/', admin.site.urls),

    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]

handler404 = pageNotFound

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
