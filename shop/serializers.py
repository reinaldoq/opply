from rest_framework import serializers

from shop.models import Order, Product


class ProductSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class OrderSerilizer(serializers.ModelSerializer):
    products = ProductSerilizer(many=True)

    class Meta:
        model = Order
        fields = "__all__"

    def create(self, validated_data):
        validated_data.pop("products")

        product_ids = []
        for product in self.initial_data['products']:
            product_ids.append(product['id'])

        order = Order.objects.create(
            **validated_data,
        )
        for product_id in product_ids:
            order.products.add(product_id)
        order.save()

        products = Product.objects.filter(pk__in=product_ids)

        for i in products:
            i.quantity_in_stock = i.quantity_in_stock - 1
        Product.objects.bulk_update(products, ['quantity_in_stock'])
        return order
