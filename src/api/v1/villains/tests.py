from django.test import TestCase
from rest_framework.reverse import reverse


class VillainsTestCase(TestCase):
    fixtures = ['villains.json']

    def test_villain_list(self):
        resp = self.client.get(reverse('api:v1:villain-list'))

        self.assertEqual(resp.status_code, 200)
        self.assertIsInstance(resp.data, list)

    def test_villain_detail(self):
        resp = self.client.get(reverse('api:v1:villain-detail', kwargs=dict(pk=1)))

        self.assertEqual(resp.status_code, 200)
        self.assertIsInstance(resp.data, dict)

        self.assertIn('id', resp.data)
        self.assertEqual(resp.data['id'], 1)

        self.assertIn('name', resp.data)
        self.assertEqual(resp.data['name'], 'Baboo')

        self.assertIn('description', resp.data)
        self.assertRegexpMatches(resp.data['description'], '^Baboo is the more intelligent of a dimwitted duo')

    def test_villain_not_found(self):
        resp = self.client.get(reverse('api:v1:villain-detail', kwargs=dict(pk=9999)))

        self.assertEqual(resp.status_code, 404)
