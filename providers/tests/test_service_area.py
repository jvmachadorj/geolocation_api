from django.test import TestCase, Client
from django.urls import reverse

from providers.models import Providers
from providers.tests.test_provider import create_provider_mock, PROVIDER_MOCK_DICT

SERVICE_AREA_LIST = 'service_areas-list'


class SercviceAreaViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.content_type = 'application/json'
        create_provider_mock(self.client, PROVIDER_MOCK_DICT, self.content_type)
        provider = Providers.objects.first()
        self.service_area = {
            "name": "Teste",
            "price": 40,
            "service_area": {
                "type": "Polygon",
                "coordinates": [
                    [
                        [
                            -43.83544921875,
                            -22.58358253773391
                        ],
                        [
                            -43.7255859375,
                            -23.47332387777116
                        ],
                        [
                            -42.264404296875,
                            -23.17066382710224
                        ],
                        [
                            -42.264404296875,
                            -22.2992614997412
                        ],
                        [
                            -43.83544921875,
                            -22.58358253773391
                        ]
                    ]
                ]
            },
            "provider": provider.id
        }

        self.lat = -43.26416015625
        self.long = -22.88756221517449

        url = reverse(SERVICE_AREA_LIST)
        create_response = self.client.post(url, self.service_area, content_type=self.content_type)
        self.created_service_area = create_response.data

    def test_service_area_creation(self):
        url = reverse(SERVICE_AREA_LIST)
        response = self.client.post(url, self.service_area, content_type=self.content_type)
        self.assertEquals(response.status_code, 201)

    def test_wrong_service_area_creation(self):
        url = reverse(SERVICE_AREA_LIST)
        self.service_area['provider'] = None
        response = self.client.post(url, self.service_area, content_type=self.content_type)
        self.assertEquals(response.status_code, 400)

    def test_search_area_list_view(self):
        url = reverse(SERVICE_AREA_LIST)
        response = self.client.get(url, content_type=self.content_type)
        self.assertEquals(response.status_code, 200)
        self.assertIsNotNone(response.data)

    def test_delete_view(self):
        url = reverse('service_areas-detail', args=(self.created_service_area.get('id'),))
        response = self.client.delete(url, content_type=self.content_type)
        self.assertEquals(response.status_code, 204)
        self.assertIsNone(response.data)

    def test_search_polygon_by_coordinates(self):
        url = reverse('coordinate_search') + '?coordinates={},{}'.format(self.lat, self.long)
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertIsNotNone(response.json())

    def test_wrong_query_sting_search(self):
        url = reverse('coordinate_search') + '?coord={},{}'.format(self.lat, self.long)
        response = self.client.get(url)
        self.assertEquals(response.status_code, 400)
