from django.test import TestCase

from allies.models import Ally


class AllyTestCase(TestCase):
    fixtures = [
        'allies.json',
        'series.json'
    ]

    def test_ally(self):
        ally = Ally.objects.get(pk=1)
        self.assertIsInstance(ally, Ally)
        self.assertEqual(ally.name, 'Alpha 5')
        self.assertRegexpMatches(ally.description, '^Alpha 5 \(Alpha for short\) was the robotic assistant')

    def test_ally_to_string(self):
        ally = Ally.objects.get(pk=1)
        self.assertEqual(str(ally), 'Alpha 5')
