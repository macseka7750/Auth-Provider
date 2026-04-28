from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Django Admin Interface
    path('admin/', admin.site.urls),
    
    # 1. Identity & Authentication Endpoints
    # Handles login, logout, password reset, etc. via dj-rest-auth
    path('api/v1/auth/', include('dj_rest_auth.urls')),
    
    # 2. User Management (Custom App)
    # Handles registration and user profile logic
    path('api/v1/users/', include('apps.users.urls')),
    
    # 3. Blog & Content Management (Custom App)
    # Handles posts and RBAC-protected content creation
    path('api/v1/blog/', include('apps.blog.urls')),
]

# ------------------------------------------------------------------------------
# STATIC & MEDIA FILES
# ------------------------------------------------------------------------------
# These are served by the Django server ONLY during development. 
# In production, WhiteNoise or a CDN (like AWS S3) should handle these.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
