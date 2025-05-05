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

# URLs sin prefijo de idioma (como el cambio de idioma y login)
urlpatterns = [
    path('i18n/setlang/', set_language, name='set_language'),
    path('usuarios/', include('users.urls')),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
    path('pedidos/', include('orders.urls')),
]

# URLs con prefijo de idioma
urlpatterns += i18n_patterns(
    path('', include('products.urls')),
    prefix_default_language=False,
)

# Para servir archivos media y static en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
