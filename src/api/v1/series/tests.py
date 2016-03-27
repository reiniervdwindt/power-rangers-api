from django.test import TestCase
from rest_framework.reverse import reverse


class SeriesTestCase(TestCase):
    fixtures = ['series.json']

    def test_series_list(self):
        resp = self.client.get(reverse('api:v1:series-list'))

        self.assertEqual(resp.status_code, 200)
        self.assertIsInstance(resp.data, list)

    def test_series_detail(self):
        resp = self.client.get(reverse('api:v1:series-detail', kwargs=dict(pk=1)))

        self.assertEqual(resp.status_code, 200)
        self.assertIsInstance(resp.data, dict)

        self.assertIn('id', resp.data)
        self.assertEqual(resp.data['id'], 1)

        self.assertIn('name', resp.data)
        self.assertEqual(resp.data['name'], 'Mighty Morphin Power Rangers')

        self.assertIn('seasons', resp.data)
        self.assertIsInstance(resp.data['seasons'], list)
        self.assertGreaterEqual(len(resp.data['seasons']), 1)

        season = resp.data['seasons'][0]
        self.assertIn('id', season)
        self.assertEqual(season['id'], 2)

        self.assertIn('number', season)
        self.assertEqual(season['number'], 1)

        self.assertIn('year', season)
        self.assertEqual(season['year'], 1993)

    def test_series_not_found(self):
        resp = self.client.get(reverse('api:v1:series-detail', kwargs=dict(pk=9999)))

        self.assertEqual(resp.status_code, 404)
