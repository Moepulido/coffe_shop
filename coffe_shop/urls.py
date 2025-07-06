"""
URL configuration for coffe_shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.views.i18n import set_language
from django.contrib.auth.views import LogoutView
from products.views import (
    ProductFormView,
    index,
    product_list,
    product_detail,
    ProductListAPI,
)
from .views import serve_media

# URLs sin prefijo de idioma (servicios básicos)
urlpatterns = [
    path("i18n/setlang/", set_language, name="set_language"),
    path("admin/", admin.site.urls),
    # API endpoints
    path("api/products/", ProductListAPI.as_view(), name="api_product_list"),
    path("api-auth/", include("rest_framework.urls")),
]

# URLs con prefijo de idioma (todo el contenido principal)
urlpatterns += i18n_patterns(
    path("", index, name="index"),  # Ruta raíz con i18n
    path("usuarios/", include("users.urls")),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("pedidos/", include("orders.urls")),
    path("productos/agregar/", ProductFormView.as_view(), name="add_product"),
    path("products/", product_list, name="product_list"),
    path("products/<int:product_id>/", product_detail, name="product_detail"),
    path("", include("products.urls")),
    prefix_default_language=False,  # No agregar prefijo para el idioma por defecto
)

# Para servir archivos media
if settings.DEBUG:
    # En desarrollo, usar el servidor de desarrollo de Django
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    # En producción, usar nuestra vista personalizada
    urlpatterns += [
        path('media/<path:path>', serve_media, name='serve_media'),
    ]

# Para servir archivos static solo en desarrollo (WhiteNoise maneja esto en producción)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
