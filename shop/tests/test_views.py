import pytest
from rest_framework.test import APIClient

from shop.models import Product, Order

pytestmark = pytest.mark.django_db


class TestProduct:
    endpoint = '/api/v1/products/'
    api_client = APIClient

    def create_products(self, products_to_create):
        for product in products_to_create:
            Product.objects.create(name=product['name'], price=product['price'],
                                   quantity_in_stock=product['quantity_in_stock'])

    def test_get_products(self, products):
        self.create_products(products)
        response = self.api_client().get(self.endpoint)
        assert response.status_code == 200
        assert response.data['count'] == len(products)


class TestOrder:
    endpoint = '/api/v1/orders/'

    def test_get_orders(self, api_client):
        product = Product.objects.create(name='pen', price=5, quantity_in_stock=7)
        order = Order.objects.create(user_id=api_client[1].pk, date="2022-03-17T20:22:07.487Z")
        order.products.add(product)
        response = api_client[0].get(self.endpoint)
        assert response.status_code == 200

    def test_create_order(self, api_client):
        Product.objects.create(name='pen', price=5, quantity_in_stock=7)
        product = Product.objects.first()
        order = {"products": [{'id': product.pk}],
                 "date": "2022-03-17T20:22:07.487Z",
                 "user": api_client[1].pk, }

        response = api_client[0].post(self.endpoint, data=order, format='json')
        assert response.status_code == 201

    def test_decrease_stock(self, api_client):
        Product.objects.create(name='pen', price=5, quantity_in_stock=7)
        product = Product.objects.first()
        order = {"products": [{'id': product.pk}],
                 "date": "2022-03-17T20:22:07.487Z",
                 "user": api_client[1].pk, }

        response = api_client[0].post(self.endpoint, data=order, format='json')
        assert response.status_code == 201
        updated_product = Product.objects.first()
        assert updated_product.quantity_in_stock == product.quantity_in_stock - 1
