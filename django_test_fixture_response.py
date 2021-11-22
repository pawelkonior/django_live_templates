import pytest
from django.urls import reverse

@pytest.fixture
def get_$endpoint$_response(client):
    url = reverse('$endpoint_name$')
    return client.get(url)