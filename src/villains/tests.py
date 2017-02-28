from django.test import TestCase

from villains.models import Villain


class VillainTestCase(TestCase):
    fixtures = [
        'villains.json',
        'series.json'
    ]

    def test_villain(self):
        villain = Villain.objects.get(pk=1)
        self.assertIsInstance(villain, Villain)
        self.assertEqual(villain.name, 'Baboo')

    def test_villain_to_string(self):
        villain = Villain.objects.get(pk=1)
        self.assertEqual(str(villain), 'Baboo')
