from django.test import TestCase
from rest_framework.reverse import reverse

from powerrangers.allies.models import Ally


class AllyTestCase(TestCase):
    fixtures = [
        'allies.json',
        'series.json'
    ]

    def test_ally_list(self):
        resp = self.client.get(reverse('ally-list'))

        self.assertEqual(resp.status_code, 200)
        self.assertIsInstance(resp.data, list)

    def test_ally_detail(self):
        resp = self.client.get(reverse('ally-detail', kwargs=dict(pk=1)))

        self.assertEqual(resp.status_code, 200)
        self.assertIsInstance(resp.data, dict)

        self.assertIn('id', resp.data)
        self.assertEqual(resp.data['id'], 1)

        self.assertIn('name', resp.data)
        self.assertEqual(resp.data['name'], 'Alpha 5')

        self.assertIn('description', resp.data)
        self.assertRegexpMatches(resp.data['description'], r'^Alpha 5 \(Alpha for short\) was the robotic assistant')

    def test_ally_not_found(self):
        resp = self.client.get(reverse('ally-detail', kwargs=dict(pk=9999)))

        self.assertEqual(resp.status_code, 404)

    def test_ally(self):
        ally = Ally.objects.get(pk=1)
        self.assertIsInstance(ally, Ally)
        self.assertEqual(ally.name, 'Alpha 5')
        self.assertRegexpMatches(ally.description, r'^Alpha 5 \(Alpha for short\) was the robotic assistant')

    def test_ally_to_string(self):
        ally = Ally.objects.get(pk=1)
        self.assertEqual(str(ally), 'Alpha 5')
