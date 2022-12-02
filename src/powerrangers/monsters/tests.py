from django.test import TestCase
from rest_framework.reverse import reverse

from powerrangers.monsters.models import Monster


class MonsterTestCase(TestCase):
    fixtures = [
        'monsters.json',
        'series.json',
    ]

    def test_monster_list(self):
        resp = self.client.get(reverse('monster-list'))

        self.assertEqual(resp.status_code, 200)
        self.assertIsInstance(resp.data, list)

    def test_monster_detail(self):
        resp = self.client.get(reverse('monster-detail', kwargs=dict(pk=2)))

        self.assertEqual(resp.status_code, 200)
        self.assertIsInstance(resp.data, dict)

        self.assertIn('id', resp.data)
        self.assertEqual(resp.data['id'], 2)

        self.assertIn('name', resp.data)
        self.assertEqual(resp.data['name'], 'Bones')

        self.assertIn('description', resp.data)
        self.assertRegexpMatches(resp.data['description'], '^Bones is a skeleton monster created by Finster')

    def test_monster_not_found(self):
        resp = self.client.get(reverse('monster-detail', kwargs=dict(pk=9999)))

        self.assertEqual(resp.status_code, 404)

    def test_monster(self):
        monster = Monster.objects.get(pk=2)
        self.assertIsInstance(monster, Monster)
        self.assertEqual(monster.name, 'Bones')

    def test_monster_to_string(self):
        monster = Monster.objects.get(pk=2)
        self.assertEqual(str(monster), 'Bones')
