from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('data/', include('data.urls')),
    path('admin/', admin.site.urls),
]

# for serving static files
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# for serving media files (files that were uploaded through your project application)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
