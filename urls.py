from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import (
    SpectacularAPIView, 
    SpectacularRedocView, 
    SpectacularSwaggerView
)

urlpatterns = [
    # Django Admin Interface
    path('admin/', admin.site.urls),
    
    # --------------------------------------------------------------------------
    # 1. IDENTITY & AUTHENTICATION (JWT/OAuth2)
    # --------------------------------------------------------------------------
    # Handles login, logout, password reset via dj-rest-auth
    path('api/v1/auth/', include('dj_rest_auth.urls')),
    
    # --------------------------------------------------------------------------
    # 2. MODULAR APPS
    # --------------------------------------------------------------------------
    # User Profile & Registration
    path('api/v1/users/', include('apps.users.urls')),
    
    # Blog & RBAC-protected Content
    path('api/v1/blog/', include('apps.blog.urls')),

    # --------------------------------------------------------------------------
    # 3. SWAGGER / OPENAPI DOCUMENTATION
    # --------------------------------------------------------------------------
    # The raw Schema (YAML/JSON export)
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    
    # Interactive Swagger UI (Best for testing)
    path(
        'api/schema/swagger-ui/', 
        SpectacularSwaggerView.as_view(url_name='schema'), 
        name='swagger-ui'
    ),
    
    # Clean Redoc View (Best for reading)
    path(
        'api/schema/redoc/', 
        SpectacularRedocView.as_view(url_name='schema'), 
        name='redoc'
    ),
]

# ------------------------------------------------------------------------------
# STATIC & MEDIA FILES
# ------------------------------------------------------------------------------
# Served by Django only during development. WhiteNoise handles these in prod.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
