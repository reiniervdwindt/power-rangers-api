from django.test import TestCase

from monsters.models import Monster


class MonsterTestCase(TestCase):
    fixtures = [
        'monsters.json',
        'series.json',
    ]

    def test_monster(self):
        monster = Monster.objects.get(pk=2)
        self.assertIsInstance(monster, Monster)
        self.assertEqual(monster.name, 'Bones')

    def test_monster_to_string(self):
        monster = Monster.objects.get(pk=2)
        self.assertEqual(str(monster), 'Bones')
