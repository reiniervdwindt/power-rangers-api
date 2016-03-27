from django.test import TestCase

from characters import constants
from characters.models import (Ally, Civilian, Monster, Ranger, Villain,
                               Weapon, Zord, ZordMode)


class CharactersTestCase(TestCase):
    fixtures = ['characters.json']


class AllyTestCase(CharactersTestCase):
    def test_ally(self):
        ally = Ally.objects.get(pk=1)
        self.assertIsInstance(ally, Ally)
        self.assertEqual(ally.name, 'Alpha 5')
        self.assertRegexpMatches(ally.description, '^Alpha 5 \(Alpha for short\) was the robotic assistant')

    def test_ally_to_string(self):
        ally = Ally.objects.get(pk=1)
        self.assertEqual(str(ally), 'Alpha 5')


class CivilianTestCase(CharactersTestCase):
    def test_civilian(self):
        civilian = Civilian.objects.get(pk=1)
        self.assertIsInstance(civilian, Civilian)
        self.assertEqual(civilian.name, 'Farkas Bulkmeier')
        self.assertEqual(civilian.nickname, 'Bulk')

    def test_civilian_to_string(self):
        civilian = Civilian.objects.get(pk=1)
        self.assertEqual(str(civilian), 'Farkas Bulkmeier')


class MonsterTestCase(CharactersTestCase):
    def test_monster(self):
        monster = Monster.objects.get(pk=1)
        self.assertIsInstance(monster, Monster)
        self.assertEqual(monster.name, 'Bones')

    def test_monster_to_string(self):
        monster = Monster.objects.get(pk=1)
        self.assertEqual(str(monster), 'Bones')


class RangerTestCase(CharactersTestCase):
    def test_ranger(self):
        ranger = Ranger.objects.get(pk=1)
        self.assertIsInstance(ranger, Ranger)
        self.assertEqual(ranger.name, 'Red Ranger')
        self.assertEqual(ranger.color, constants.RANGER_COLOR_RED)

    def test_ranger_to_string(self):
        ranger = Ranger.objects.get(pk=1)
        self.assertEqual(str(ranger), 'Red Ranger')


class VillainTestCase(CharactersTestCase):
    def test_villain(self):
        villain = Villain.objects.get(pk=1)
        self.assertIsInstance(villain, Villain)
        self.assertEqual(villain.name, 'Rita Repulsa')

    def test_villain_to_string(self):
        villain = Villain.objects.get(pk=1)
        self.assertEqual(str(villain), 'Rita Repulsa')


class WeaponTestCase(CharactersTestCase):
    def test_weapon(self):
        weapon = Weapon.objects.get(pk=1)
        self.assertIsInstance(weapon, Weapon)
        self.assertEqual(weapon.name, 'Power Sword')
        self.assertEqual(weapon.type, constants.WEAPON_TYPE_SWORD)

    def test_weapon_to_string(self):
        weapon = Weapon.objects.get(pk=1)
        self.assertEqual(str(weapon), 'Power Sword')


class ZordTestCase(CharactersTestCase):
    def test_zord(self):
        zord = Zord.objects.get(pk=18)
        self.assertIsInstance(zord, Zord)
        self.assertEqual(zord.name, 'White Tigerzord')
        self.assertEqual(zord.type, constants.ZORD_TYPE_THUNDERZORD)

        mode = zord.modes.first()
        self.assertEqual(mode.id, 1)
        self.assertEqual(mode.name, 'Tiger Mode')
        self.assertRegexpMatches(mode.description, '^Tiger mode is the primary form')

    def test_zord_to_string(self):
        zord = Zord.objects.get(pk=1)
        self.assertEqual(str(zord), 'Tyrannosaurus Dinozord')

    def test_zord_mode_to_string(self):
        mode = ZordMode.objects.get(pk=1)
        self.assertEqual(str(mode), 'Tiger Mode')
