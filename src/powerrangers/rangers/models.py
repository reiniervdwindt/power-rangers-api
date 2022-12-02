from __future__ import unicode_literals

from django.db import models

from powerrangers.rangers import constants
from powerrangers.series.models import Series
from powerrangers.weapons.models import Weapon
from powerrangers.zords.models import Zord


class Ranger(models.Model):
    name = models.CharField(max_length=64, unique=True)
    color = models.CharField(max_length=16, choices=constants.RANGER_COLORS)
    series = models.ManyToManyField(Series, through='Appearance')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Appearance(models.Model):
    ranger = models.ForeignKey(Ranger, on_delete=models.CASCADE)
    series = models.ForeignKey(Series, on_delete=models.CASCADE)
    weapon = models.ForeignKey(Weapon, on_delete=models.CASCADE)
    zord = models.ForeignKey(Zord, on_delete=models.CASCADE)

    def __str__(self):
        return '{ranger} ({series})'.format(ranger=self.ranger.name, series=self.series)

    class Meta:
        ordering = ('series__name',)
