import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient

pytestmark = pytest.mark.django_db


# TODO: Add test to check if user connects to the api with these token

def test_get_jwt_token():
    api_client = APIClient
    creds = {"username": "myusername", "password": "123456"}
    User.objects.create_user(username=creds['username'], password=creds['password'])
    response = api_client().post('/api/token/', data=creds, format="json")

    assert response.data['access']
    assert response.data['refresh']
