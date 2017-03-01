from django.test import TestCase
from rest_framework import status
from rest_framework.reverse import reverse


class APIRootViewTestCase(TestCase):
    def test_api_root_view(self):
        response = self.client.get(reverse('api:v1:api-root'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
