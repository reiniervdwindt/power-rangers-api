from django.test import TestCase
from rest_framework.reverse import reverse


class MonstersTestCase(TestCase):
    fixtures = [
        'monsters.json',
        'series.json',
    ]

    def test_monster_list(self):
        resp = self.client.get(reverse('api:v1:monster-list'))

        self.assertEqual(resp.status_code, 200)
        self.assertIsInstance(resp.data, list)

    def test_monster_detail(self):
        resp = self.client.get(reverse('api:v1:monster-detail', kwargs=dict(pk=2)))

        self.assertEqual(resp.status_code, 200)
        self.assertIsInstance(resp.data, dict)

        self.assertIn('id', resp.data)
        self.assertEqual(resp.data['id'], 2)

        self.assertIn('name', resp.data)
        self.assertEqual(resp.data['name'], 'Bones')

        self.assertIn('description', resp.data)
        self.assertRegexpMatches(resp.data['description'], '^Bones is a skeleton monster created by Finster')

    def test_monster_not_found(self):
        resp = self.client.get(reverse('api:v1:monster-detail', kwargs=dict(pk=9999)))

        self.assertEqual(resp.status_code, 404)
