"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

# Documentation
schema_view = get_schema_view(
    openapi.Info(
        title="crm_service",  # Название API
        default_version='v0',  # Версия API по умолчанию
        description="Description",
        terms_of_service="https://www.google.com/policies/terms/",  # Условия использования API
        contact=openapi.Contact(email="contact@snippets.local"),  # Контактная информация разработчиков API
        license=openapi.License(name="BSD License"),  # Лицензия API
    ),
    public=True,  # Отметка, что схема API публично доступна
    permission_classes=(permissions.AllowAny,),  # Класс разрешений для доступа к схеме API
)

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # Apps
    path('api/products/', include('products.urls', namespace='products')),
    path('api/suppliers/', include('suppliers.urls', namespace='suppliers')),

    # Users
    path('api/users/', include('users.urls', namespace='users')),

    # Documentation
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),  # Swagger JSON | YAML
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),  # Swagger UI
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),  # ReDoc UI
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
