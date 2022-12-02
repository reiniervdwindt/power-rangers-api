from django.test import TestCase
from rest_framework.reverse import reverse

from powerrangers.zords import constants
from powerrangers.zords.models import Zord


class ZordTestCase(TestCase):
    fixtures = [
        'rangers.json',
        'series.json',
        'weapons.json',
        'zords.json',
    ]

    def test_zord_list(self):
        resp = self.client.get(reverse('zord-list'))

        self.assertEqual(resp.status_code, 200)
        self.assertIsInstance(resp.data, list)

    def test_zord_detail(self):
        resp = self.client.get(reverse('zord-detail', kwargs=dict(pk=1)))

        self.assertEqual(resp.status_code, 200)
        self.assertIsInstance(resp.data, dict)

        self.assertIn('id', resp.data)
        self.assertEqual(resp.data['id'], 1)

        self.assertIn('name', resp.data)
        self.assertEqual(resp.data['name'], 'Dino Megazord')

        self.assertIn('description', resp.data)
        self.assertRegexpMatches(resp.data['description'], '^The Megazord')

        self.assertIn('type', resp.data)
        self.assertEqual(resp.data['type'], 'dinozord')

    def test_zord_not_found(self):
        resp = self.client.get(reverse('zord-detail', kwargs=dict(pk=9999)))

        self.assertEqual(resp.status_code, 404)

    def test_zord(self):
        zord = Zord.objects.get(pk=18)
        self.assertIsInstance(zord, Zord)
        self.assertEqual(zord.name, 'Unicorn Thunderzord')
        self.assertEqual(zord.type, constants.ZORD_TYPE_THUNDERZORD)

    def test_zord_to_string(self):
        zord = Zord.objects.get(pk=1)
        self.assertEqual(str(zord), 'Dino Megazord')

    def test_zord_mode_to_string(self):
        zord = Zord.objects.get(pk=19)
        self.assertIsInstance(zord, Zord)
        self.assertEqual(zord.name, 'White Tigerzord')
        self.assertEqual(zord.type, constants.ZORD_TYPE_THUNDERZORD)

        mode = zord.modes.first()
        self.assertEqual(mode.id, 1)
        self.assertEqual(str(mode), 'Tiger Mode')
        self.assertRegexpMatches(mode.description, '^Tiger mode is the primary form')
