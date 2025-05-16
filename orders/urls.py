from django.urls import path

from .views import MyOrderView, CreatOrderProductView

app_name = 'orders'

urlpatterns = [
    path('my_order/', MyOrderView.as_view(), name='my_order'),
    path('add_product/', CreatOrderProductView.as_view(), name='add_product')
]
