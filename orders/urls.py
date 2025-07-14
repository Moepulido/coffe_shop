from django.urls import path
from . import views

app_name = "orders"

urlpatterns = [
    path("my_order/", views.MyOrderView.as_view(), name="my_order"),
    path("add_product/", views.add_product, name="add_product"),
]
