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
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static

# URLs que no necesitan prefijo de idioma (admin, login, etc.)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    path('users/', include('users.urls')),
]

# URLs que sí se traducirán y tendrán prefijo de idioma (/en/, /es/, etc.)
urlpatterns += i18n_patterns(
    path('', include('products.urls')),
    path('orders/', include('orders.urls')),
    # La raíz de cada idioma mostrará la lista de productos.
    # El health checker de AWS usará la raíz sin prefijo y será manejado por la app de productos.
    prefix_default_language=True,
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
