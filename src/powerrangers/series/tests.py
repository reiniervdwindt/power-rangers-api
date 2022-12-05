from django.contrib.admin.sites import AdminSite
from django.db.models import QuerySet
from django.test import TestCase
from rest_framework.reverse import reverse

from powerrangers.series.admin import SeriesAdmin
from powerrangers.series.models import Episode, Series


class SeriesTestCase(TestCase):
    fixtures = ['series.json']

    def test_series_list(self):
        resp = self.client.get(reverse('series-list'))

        self.assertEqual(resp.status_code, 200)
        self.assertIsInstance(resp.data, list)

    def test_series_detail(self):
        resp = self.client.get(reverse('series-detail', kwargs=dict(pk=1)))

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
        resp = self.client.get(reverse('series-detail', kwargs=dict(pk=9999)))
        self.assertEqual(resp.status_code, 404)

    def test_series_seasons_list(self):
        resp = self.client.get(reverse('series-seasons', args=(1, )))
        self.assertEqual(resp.status_code, 200)

    def test_series_episodes_list(self):
        resp = self.client.get(reverse('series-episodes', args=(1, )))
        self.assertEqual(resp.status_code, 200)

    def test_seasons_list(self):
        resp = self.client.get(reverse('seasons-list'))
        self.assertEqual(resp.status_code, 200)

    def test_seasons_detail(self):
        resp = self.client.get(reverse('seasons-detail', args=(2, )))
        self.assertEqual(resp.status_code, 200)

    def test_seasons_episodes_list(self):
        resp = self.client.get(reverse('seasons-episodes', args=(2, )))
        self.assertEqual(resp.status_code, 200)

    def test_series(self):
        series = Series.objects.get(pk=1)
        self.assertIsInstance(series, Series)
        self.assertEqual(series.name, 'Mighty Morphin Power Rangers')
        self.assertEqual(series.year, 1993)

    def test_series_to_string(self):
        series = Series.objects.get(pk=1)
        self.assertEqual(str(series), 'Mighty Morphin Power Rangers')

    def test_season(self):
        season = Series.objects.get(pk=2)
        self.assertIsInstance(season, Series)
        self.assertIsInstance(season.parent, Series)
        self.assertEqual(season.number, 1)
        self.assertEqual(season.number, 1)
        self.assertEqual(season.year, 1993)

    def test_season_to_string(self):
        season = Series.objects.get(pk=2)
        self.assertEqual(str(season), 'Mighty Morphin Power Rangers (Season 1)')

    def test_episode_to_string(self):
        episode = Episode.objects.get(pk=1)
        self.assertEqual(str(episode), 'Day of the Dumpster')

    def test_admin(self):
        ma = SeriesAdmin(Series, AdminSite())
        queryset = ma.get_queryset(request=object)
        self.assertIsInstance(queryset, QuerySet)
        self.assertEqual(len(queryset), 22)
