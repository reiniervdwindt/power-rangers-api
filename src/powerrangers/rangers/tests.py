from django.test import TestCase
from rest_framework.reverse import reverse

from powerrangers.rangers import constants
from powerrangers.rangers.models import Ranger


class RangerTestCase(TestCase):
    fixtures = [
        'rangers.json',
        'series.json',
        'weapons.json',
        'zords.json',
    ]

    def test_ranger_list(self):
        resp = self.client.get(reverse('rangers-list'))

        self.assertEqual(resp.status_code, 200)
        self.assertIsInstance(resp.data, list)

    def test_ranger_detail(self):
        resp = self.client.get(reverse('rangers-detail', kwargs=dict(pk=1)))

        self.assertEqual(resp.status_code, 200)
        self.assertIsInstance(resp.data, dict)

        self.assertIn('id', resp.data)
        self.assertEqual(resp.data['id'], 1)

        self.assertIn('name', resp.data)
        self.assertEqual(resp.data['name'], 'Red Ranger')

        self.assertIn('color', resp.data)
        self.assertEqual(resp.data['color'], 'red')

        self.assertIn('series', resp.data)
        self.assertIsInstance(resp.data['series'], list)

    def test_ranger_not_found(self):
        resp = self.client.get(reverse('rangers-detail', kwargs=dict(pk=9999)))

        self.assertEqual(resp.status_code, 404)

    def test_ranger(self):
        ranger = Ranger.objects.get(pk=1)
        self.assertIsInstance(ranger, Ranger)
        self.assertEqual(ranger.name, 'Red Ranger')
        self.assertEqual(ranger.color, constants.RANGER_COLOR_RED)

        series = ranger.appearance_set.all()[0]
        self.assertEqual(str(series), 'Red Ranger (Mighty Morphin Power Rangers (Season 1))')

    def test_ranger_to_string(self):
        ranger = Ranger.objects.get(pk=1)
        self.assertEqual(str(ranger), 'Red Ranger')
