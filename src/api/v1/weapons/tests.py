from rest_framework.reverse import reverse

from characters.tests import CharactersTestCase


class WeaponsTestCase(CharactersTestCase):
    def test_weapon_list(self):
        resp = self.client.get(reverse('api:v1:weapon-list'))

        self.assertEqual(resp.status_code, 200)
        self.assertIsInstance(resp.data, list)

    def test_weapon_detail(self):
        resp = self.client.get(reverse('api:v1:weapon-detail', kwargs=dict(pk=1)))

        self.assertEqual(resp.status_code, 200)
        self.assertIsInstance(resp.data, dict)

        self.assertIn('id', resp.data)
        self.assertEqual(resp.data['id'], 1)

        self.assertIn('name', resp.data)
        self.assertEqual(resp.data['name'], 'Power Sword')

        self.assertIn('type', resp.data)
        self.assertEqual(resp.data['type'], 'sword')

    def test_weapon_not_found(self):
        resp = self.client.get(reverse('api:v1:weapon-detail', kwargs=dict(pk=9999)))

        self.assertEqual(resp.status_code, 404)
