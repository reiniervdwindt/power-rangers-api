from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from rangers import constants
from series.models import Series
from weapons.models import Weapon
from zords.models import Zord


@python_2_unicode_compatible
class Ranger(models.Model):
    name = models.CharField(max_length=64, unique=True)
    color = models.CharField(max_length=16, choices=constants.RANGER_COLORS)
    series = models.ManyToManyField(Series, through='Appearance')

    def __str__(self):
        return self.name

    class Meta(object):
        ordering = ('name',)


@python_2_unicode_compatible
class Appearance(models.Model):
    ranger = models.ForeignKey(Ranger)
    series = models.ForeignKey(Series)
    weapon = models.ForeignKey(Weapon)
    zord = models.ForeignKey(Zord)

    def __str__(self):
        return '{ranger} ({series})'.format(ranger=self.ranger.name, series=self.series)

    class Meta(object):
        ordering = ('series__name',)
