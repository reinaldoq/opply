from decimal import Decimal

from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models

User = get_user_model()


class Product(models.Model):
    name = models.TextField(blank=True)
    # This would break if we sell products more expensive than 999999.99
    price = models.DecimalField(decimal_places=2, max_digits=8, blank=True)
    quantity_in_stock = models.DecimalField(decimal_places=2, max_digits=8, blank=True,
                                            validators=[MinValueValidator(Decimal('0.00'))])


# TODO: Include qantity and other variants in a third entity OrderProduct.
# I am keeping this simple for this exercise
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='user')
    date = models.DateTimeField()
    products = models.ManyToManyField(Product)
