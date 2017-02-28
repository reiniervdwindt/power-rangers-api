from django.test import TestCase

from weapons import constants
from weapons.models import Weapon


class WeaponTestCase(TestCase):
    fixtures = ['weapons.json']

    def test_weapon(self):
        weapon = Weapon.objects.get(pk=1)
        self.assertIsInstance(weapon, Weapon)
        self.assertEqual(weapon.name, 'Dragon Dagger')
        self.assertEqual(weapon.type, constants.WEAPON_TYPE_DAGGER)

    def test_weapon_to_string(self):
        weapon = Weapon.objects.get(pk=1)
        self.assertEqual(str(weapon), 'Dragon Dagger')
