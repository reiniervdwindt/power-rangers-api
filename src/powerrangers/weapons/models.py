from django.db import models

from powerrangers.weapons import constants


class Weapon(models.Model):
    name = models.CharField(max_length=64, unique=True)
    type = models.CharField(max_length=16, choices=constants.WEAPONS)
    parts = models.ManyToManyField('Weapon', blank=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
