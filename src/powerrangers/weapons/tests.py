from django.test import TestCase
from rest_framework.reverse import reverse

from powerrangers.weapons import constants
from powerrangers.weapons.models import Weapon


class WeaponTestCase(TestCase):
    fixtures = ['weapons.json']

    def test_weapon_list(self):
        resp = self.client.get(reverse('weapon-list'))

        self.assertEqual(resp.status_code, 200)
        self.assertIsInstance(resp.data, list)

    def test_weapon_detail(self):
        resp = self.client.get(reverse('weapon-detail', kwargs=dict(pk=1)))

        self.assertEqual(resp.status_code, 200)
        self.assertIsInstance(resp.data, dict)

        self.assertIn('id', resp.data)
        self.assertEqual(resp.data['id'], 1)

        self.assertIn('name', resp.data)
        self.assertEqual(resp.data['name'], 'Dragon Dagger')

        self.assertIn('type', resp.data)
        self.assertEqual(resp.data['type'], constants.WEAPON_TYPE_DAGGER)

    def test_weapon_not_found(self):
        resp = self.client.get(reverse('weapon-detail', kwargs=dict(pk=9999)))

        self.assertEqual(resp.status_code, 404)

    def test_weapon(self):
        weapon = Weapon.objects.get(pk=1)
        self.assertIsInstance(weapon, Weapon)
        self.assertEqual(weapon.name, 'Dragon Dagger')
        self.assertEqual(weapon.type, constants.WEAPON_TYPE_DAGGER)

    def test_weapon_to_string(self):
        weapon = Weapon.objects.get(pk=1)
        self.assertEqual(str(weapon), 'Dragon Dagger')
