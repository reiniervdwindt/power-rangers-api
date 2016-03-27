from collections import OrderedDict

from rest_framework.reverse import reverse

from characters.tests import CharactersTestCase


class RangersTestCase(CharactersTestCase):
    def test_ranger_list(self):
        resp = self.client.get(reverse('api:v1:ranger-list'))

        self.assertEqual(resp.status_code, 200)
        self.assertIsInstance(resp.data, list)

    def test_ranger_detail(self):
        resp = self.client.get(reverse('api:v1:ranger-detail', kwargs=dict(pk=1)))

        self.assertEqual(resp.status_code, 200)
        self.assertIsInstance(resp.data, dict)

        self.assertIn('id', resp.data)
        self.assertEqual(resp.data['id'], 1)

        self.assertIn('name', resp.data)
        self.assertEqual(resp.data['name'], 'Red Ranger')

        self.assertIn('color', resp.data)
        self.assertEqual(resp.data['color'], 'red')

        self.assertIn('weapon', resp.data)
        self.assertIsInstance(resp.data['weapon'], OrderedDict)

    def test_ranger_not_found(self):
        resp = self.client.get(reverse('api:v1:ranger-detail', kwargs=dict(pk=9999)))

        self.assertEqual(resp.status_code, 404)
