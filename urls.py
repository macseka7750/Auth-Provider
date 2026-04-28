from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Identity & Auth Endpoints
    path('api/v1/auth/', include('dj_rest_auth.urls')),
    
    # App-Specific Endpoints (Modular)
    path('api/v1/users/', include('apps.users.urls')),
]

# Serve static/media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
