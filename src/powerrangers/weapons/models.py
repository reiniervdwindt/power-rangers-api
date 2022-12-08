from django.db import models

from powerrangers.weapons.choices import Category


class Weapon(models.Model):
    name = models.CharField(max_length=64, unique=True)
    category = models.CharField(max_length=16, choices=Category.choices)
    parts = models.ManyToManyField('Weapon', blank=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
