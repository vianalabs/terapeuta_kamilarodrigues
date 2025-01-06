import pytest
from django.test import TestCase
from django.urls import reverse

@pytest.mark.unit
def test_acess_index_true(client):
    """
    Test if the index view returns a 200 status code when accessed.
    """
    url = reverse('index')
    response = client.get(url)
    assert response.status_code == 200
