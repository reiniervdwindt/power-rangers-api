from django.test import TestCase

from civilians.models import Civilian


class CivilianTestCase(TestCase):
    fixtures = [
        'civilians.json',
        'series.json',
    ]

    def test_civilian(self):
        civilian = Civilian.objects.get(pk=4)
        self.assertIsInstance(civilian, Civilian)
        self.assertEqual(civilian.name, 'Farkas Bulkmeier')
        self.assertEqual(civilian.nickname, 'Bulk')

    def test_civilian_to_string(self):
        civilian = Civilian.objects.get(pk=4)
        self.assertEqual(str(civilian), 'Farkas Bulkmeier')
