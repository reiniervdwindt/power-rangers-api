from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Series(models.Model):
    name = models.CharField(max_length=128)
    number = models.PositiveSmallIntegerField()
    year = models.PositiveSmallIntegerField()
    parent = models.ForeignKey('Series', default=None, blank=True, null=True)

    class Meta(object):
        ordering = ('year',)
        verbose_name_plural = 'series'

    def __str__(self):
        return self.name

    @property
    def full_name(self):
        return '{series} ({season})'.format(series=self.parent, season=self.name)

    @property
    def seasons(self):
        return Series.objects.filter(parent=self)
