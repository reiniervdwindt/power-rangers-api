from django.contrib.admin.sites import AdminSite
from django.db.models import QuerySet
from django.test import TestCase

from series.admin import SeriesAdmin
from series.models import Episode, Series


class SeriesTestCase(TestCase):
    fixtures = ['series.json']

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
        self.assertEqual(str(season), 'Season 1')

    def test_season_full_name(self):
        season = Series.objects.get(pk=2)
        self.assertEqual(season.full_name, 'Mighty Morphin Power Rangers (Season 1)')

    def test_episode_to_string(self):
        episode = Episode.objects.get(pk=1)
        self.assertEqual(str(episode), 'Day of the Dumpster')

    def test_admin(self):
        ma = SeriesAdmin(Series, AdminSite())
        queryset = ma.get_queryset(request=object)
        self.assertIsInstance(queryset, QuerySet)
        self.assertEqual(len(queryset), 1)
