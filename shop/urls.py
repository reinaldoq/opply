from django.urls import path
from rest_framework.routers import DefaultRouter

from shop.views import ProductList, OrderListCreate

router = DefaultRouter()
router.register(r"products", ProductList)
router.register(r"orders", OrderListCreate, basename='orders')

app_name = "shop"

urlpatterns = [
    path('products/', ProductList.as_view(), name='api_product_list'),
    path('orders/', OrderListCreate.as_view(), name='api_orders_list_create')
]
