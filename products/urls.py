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
from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.product_list, name='product_list'),
    path('products/<int:product_id>/', views.product_detail, name='product_detail'),
    path('productos/agregar/', views.ProductFormView.as_view(), name='add_product'),
    path('productos/editar/<int:product_id>/', views.edit_product, name='edit_product'),
    # Si prefieres usar la vista basada en clase, comenta la línea anterior y descomenta esta:
    # path('products/', views.ProductListView.as_view(), name='product_list'),
]