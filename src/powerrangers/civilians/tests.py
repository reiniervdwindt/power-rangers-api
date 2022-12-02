from django.test import TestCase
from rest_framework.reverse import reverse

from powerrangers.civilians.models import Civilian


class CivilianTestCase(TestCase):
    fixtures = [
        'civilians.json',
        'series.json',
    ]

    def test_civilian_list(self):
        resp = self.client.get(reverse('civilian-list'))

        self.assertEqual(resp.status_code, 200)
        self.assertIsInstance(resp.data, list)

    def test_civilian_detail(self):
        resp = self.client.get(reverse('civilian-detail', kwargs=dict(pk=4)))

        self.assertEqual(resp.status_code, 200)
        self.assertIsInstance(resp.data, dict)

        self.assertIn('id', resp.data)
        self.assertEqual(resp.data['id'], 4)

        self.assertIn('name', resp.data)
        self.assertEqual(resp.data['name'], 'Farkas Bulkmeier')

        self.assertIn('description', resp.data)
        self.assertRegexpMatches(resp.data['description'], '^Farkas "Bulk" Bulkmeier is a fictional character')

    def test_civilian_not_found(self):
        resp = self.client.get(reverse('civilian-detail', kwargs=dict(pk=9999)))

        self.assertEqual(resp.status_code, 404)

    def test_civilian(self):
        civilian = Civilian.objects.get(pk=4)
        self.assertIsInstance(civilian, Civilian)
        self.assertEqual(civilian.name, 'Farkas Bulkmeier')
        self.assertEqual(civilian.nickname, 'Bulk')

    def test_civilian_to_string(self):
        civilian = Civilian.objects.get(pk=4)
        self.assertEqual(str(civilian), 'Farkas Bulkmeier')
