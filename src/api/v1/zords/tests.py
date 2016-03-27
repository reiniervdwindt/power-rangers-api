from rest_framework.reverse import reverse

from characters.tests import CharactersTestCase


class ZordsTestCase(CharactersTestCase):
    def test_zord_list(self):
        resp = self.client.get(reverse('api:v1:zord-list'))

        self.assertEqual(resp.status_code, 200)
        self.assertIsInstance(resp.data, list)

    def test_zord_detail(self):
        resp = self.client.get(reverse('api:v1:zord-detail', kwargs=dict(pk=1)))

        self.assertEqual(resp.status_code, 200)
        self.assertIsInstance(resp.data, dict)

        self.assertIn('id', resp.data)
        self.assertEqual(resp.data['id'], 1)

        self.assertIn('name', resp.data)
        self.assertEqual(resp.data['name'], 'Tyrannosaurus Dinozord')

        self.assertIn('description', resp.data)
        self.assertRegexpMatches(resp.data['description'], '^Forming the head and torso')

        self.assertIn('type', resp.data)
        self.assertEqual(resp.data['type'], 'dinozord')

    def test_zord_not_found(self):
        resp = self.client.get(reverse('api:v1:zord-detail', kwargs=dict(pk=9999)))

        self.assertEqual(resp.status_code, 404)
