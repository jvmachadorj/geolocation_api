from django.test import TestCase, Client
from django.urls import reverse

PROVIDER_MOCK_DICT = {
    "name": "teste",
    "email": "teste@gmail.com",
    "phone": "+5521985447898",
    "language": "English",
    "currency": "BRL"
}

PROVIDER_LIST_URL = 'providers-list'


def create_provider_mock(client, provider, content_type):
    url = reverse('providers-list')
    request = client.post(url, provider, content_type=content_type)
    return request.data


class ProviderViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.valid_provider = PROVIDER_MOCK_DICT
        self.content_type = 'application/json'
        self.created_provider = create_provider_mock(self.client, self.valid_provider, self.content_type)

    def test_provider_creation(self):
        url = reverse(PROVIDER_LIST_URL)
        create_response = self.client.post(url, self.valid_provider, content_type=self.content_type)
        self.assertEquals(create_response.status_code, 201)

    def test_wrong_provider_creation(self):
        url = reverse(PROVIDER_LIST_URL)
        wrong_provider = self.valid_provider.copy()
        wrong_provider['email'] = 123
        create_response = self.client.post(url, wrong_provider, content_type=self.content_type)
        self.assertEquals(create_response.status_code, 400)

    def test_list_view(self):
        url = reverse(PROVIDER_LIST_URL)
        create_response = self.client.get(url, content_type=self.content_type)
        self.assertEquals(create_response.status_code, 200)
        self.assertIsNotNone(create_response.data)

    def test_delete_view(self):
        url = reverse('providers-detail', args=(self.created_provider.get('id'),))
        create_response = self.client.delete(url, content_type=self.content_type)
        self.assertEquals(create_response.status_code, 204)
        self.assertIsNone(create_response.data)
