from __future__ import unicode_literals

from django.db import models
from django.db.models import Q
from django.utils.encoding import python_2_unicode_compatible

from series.models import Series
from villains import constants


@python_2_unicode_compatible
class Villain(models.Model):
    name = models.CharField(max_length=64, unique=True)
    description = models.TextField(default=None, blank=True, null=True)
    gender = models.CharField(max_length=8, choices=constants.GENDERS, default=None, blank=True, null=True)
    type = models.CharField(max_length=32, choices=constants.VILLAINS_TYPES, default=None, blank=True, null=True)
    homeworld = models.CharField(max_length=32, default=None, blank=True, null=True)
    series = models.ManyToManyField(
        Series, blank=True, limit_choices_to=Q(series__isnull=True), related_name='villains'
    )

    class Meta(object):
        ordering = ('name',)

    def __str__(self):
        return self.name
