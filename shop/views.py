from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from shop.models import Product, Order
from shop.serializers import ProductSerilizer, OrderSerilizer


class ProductList(generics.ListAPIView):
    model = Product
    queryset = Product.objects.all()
    serializer_class = ProductSerilizer


class OrderListCreate(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = OrderSerilizer

    def get_queryset(self):
        user = self.request.user
        return Order.objects.filter(user=user)
