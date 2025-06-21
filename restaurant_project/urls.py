from django.contrib import admin
from django.urls import path, include
from django.conf import settings # Ensure settings is imported to access MEDIA_URL and MEDIA_ROOT
from django.conf.urls.static import static # Import static to serve media files in development


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
