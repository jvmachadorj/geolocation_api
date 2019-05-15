from django.test import TestCase, Client
from django.urls import reverse


class ProviderViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.valid_provider = {
            "name": "teste",
            "email": "teste@gmail.com",
            "phone": "+5521985447898",
            "language": "English",
            "currency": "BRL"
        }
        self.content_type = 'application/json'

    def create_provider(self):
        url = reverse('provider-list')
        create_response = self.client.post(url, self.valid_provider, content_type=self.content_type)
        self.assertEquals(create_response.status_code, 201)
