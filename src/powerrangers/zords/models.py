from __future__ import unicode_literals

from django.db import models

from powerrangers.zords.choices import Category


class Zord(models.Model):
    name = models.CharField(max_length=64, unique=True)
    description = models.TextField()
    category = models.CharField(max_length=32, choices=Category.choices)
    parts = models.ManyToManyField('Zord', blank=True)

    class Meta:
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


class Mode(models.Model):
    name = models.CharField(max_length=32, unique=True)
    zord = models.ForeignKey(Zord, related_name='modes', on_delete=models.CASCADE)
    description = models.TextField()

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
