from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Series(models.Model):
    name = models.CharField(max_length=128)
    number = models.PositiveSmallIntegerField()
    year = models.PositiveSmallIntegerField()
    parent = models.ForeignKey('Series', default=None, blank=True, null=True)

    imdb_id = models.CharField(max_length=9, unique=True, default=None, blank=True, null=True)
    trakt_id = models.IntegerField(unique=True, default=None, blank=True, null=True)

    class Meta(object):
        ordering = ('year',)
        verbose_name_plural = 'series'

    def __str__(self):
        if self.parent:
            return '{series} ({season})'.format(series=self.parent.name, season=self.name)
        return '{name}'.format(name=self.name)

    @property
    def seasons(self):
        return Series.objects.filter(parent=self)


@python_2_unicode_compatible
class Episode(models.Model):
    series = models.ForeignKey(Series, related_name='episodes')
    name = models.CharField(max_length=128)
    number = models.PositiveSmallIntegerField()

    imdb_id = models.CharField(max_length=9, unique=True, default=None, blank=True, null=True)
    trakt_id = models.IntegerField(unique=True, default=None, blank=True, null=True)

    def __str__(self):
        return self.name
