from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from zords import constants


@python_2_unicode_compatible
class Zord(models.Model):
    name = models.CharField(max_length=64, unique=True)
    description = models.TextField()
    type = models.CharField(max_length=32, choices=constants.ZORD_TYPES)
    parts = models.ManyToManyField('Zord', blank=True)

    class Meta(object):
        ordering = ('name',)

    def __str__(self):
        return self.name

    @property
    def pilots(self):
        if self.appearance_set.count():
            return [appearance.ranger for appearance in self.appearance_set.all()]

        pilots = []
        for part in self.parts.all():
            pilots += part.pilots

        return pilots


@python_2_unicode_compatible
class Mode(models.Model):
    name = models.CharField(max_length=32, unique=True)
    zord = models.ForeignKey(Zord, related_name='modes')
    description = models.TextField()

    class Meta(object):
        ordering = ('name',)

    def __str__(self):
        return self.name
