from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from weapons import constants


@python_2_unicode_compatible
class Weapon(models.Model):
    name = models.CharField(max_length=64, unique=True)
    type = models.CharField(max_length=16, choices=constants.WEAPONS)
    parts = models.ManyToManyField('Weapon', blank=True)

    class Meta(object):
        ordering = ('name',)

    def __str__(self):
        return self.name
