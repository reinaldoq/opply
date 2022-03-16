import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken


# TODO: Create function to generate products
@pytest.fixture
def products():
    return [{
        "name": "Pencil",
        "price": 2.50,
        "quantity_in_stock": 10,
    },
        {
            "name": "Pen",
            "price": 3.75,
            "quantity_in_stock": 7,
        },
        {
            "name": "Paper",
            "price": 6,
            "quantity_in_stock": 5,
        },
    ]


@pytest.fixture
def order():
    return {"products": {
        "id": 1,
        "name": "Pen",
        "price": 3.75,
        "quantity_in_stock": 7,
    },
        "date": "2022-03-17T20:22:07.487Z",
        "user": 1, }


@pytest.fixture
def api_client():
    user = User.objects.create_user(username='testuser', password='testpwd')
    client = APIClient()
    refresh = RefreshToken.for_user(user)
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')

    return client, user
