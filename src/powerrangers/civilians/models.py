from __future__ import unicode_literals

from django.db import models
from django.db.models import Q

from powerrangers.series.models import Series


class Civilian(models.Model):
    name = models.CharField(max_length=64, unique=True)
    nickname = models.CharField(max_length=32, default=None, blank=True, null=True)
    description = models.TextField(default=None, blank=True, null=True)
    series = models.ManyToManyField(
        Series, blank=True, limit_choices_to=Q(series__isnull=True), related_name='civilians'
    )

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
