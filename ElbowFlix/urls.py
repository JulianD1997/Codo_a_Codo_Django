from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from django.urls import include, path

from .views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('',include('API_TMDB.urls')),
    path('',include('users.urls')),
    path('',include('cinema.urls')),
    path('',include('administration.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)