from django.test import TestCase

from zords import constants
from zords.models import Zord


class ZordTestCase(TestCase):
    fixtures = ['zords.json']

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
