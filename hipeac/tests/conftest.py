import pytest

from rest_framework.test import APIClient


@pytest.fixture()
def api_client():
    """A Django REST framework test client instance."""
    return APIClient(enforce_csrf_checks=True)
