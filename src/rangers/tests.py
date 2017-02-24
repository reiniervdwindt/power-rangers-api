from django.test import TestCase

from rangers import constants
from rangers.models import Ranger


class RangerTestCase(TestCase):
    fixtures = [
        'rangers.json',
        'series.json',
        'weapons.json',
        'zords.json',
    ]

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
