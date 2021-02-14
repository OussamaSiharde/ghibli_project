import pytest
from django.conf import settings
from django.contrib.auth.models import AnonymousUser
from django.test import Client
from faker import Faker
from rest_framework.test import APIClient


@pytest.fixture
def faker():
    return Faker()


@pytest.fixture
def client():
    return Client()


@pytest.fixture
def api_client():
    return APIClient()
