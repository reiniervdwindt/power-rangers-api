from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from characters import constants
from series.models import Series


class Character(models.Model):
    name = models.CharField(max_length=64, unique=True)

    class Meta(object):
        abstract = True
        ordering = ('name',)


@python_2_unicode_compatible
class Ally(Character):
    description = models.TextField(default=None, blank=True, null=True)

    class Meta(object):
        verbose_name_plural = 'allies'

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Civilian(Character):
    nickname = models.CharField(max_length=32, default=None, blank=True, null=True)
    description = models.TextField(default=None, blank=True, null=True)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Monster(Character):
    description = models.TextField()

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Ranger(Character):
    color = models.CharField(max_length=16, choices=constants.RANGER_COLORS)
    weapon = models.OneToOneField('Weapon', related_name='ranger', blank=True, null=True)
    zords = models.ManyToManyField('Zord', related_name='piloted_by')

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Villain(Character):
    description = models.TextField(default=None, blank=True, null=True)
    gender = models.CharField(max_length=8, choices=constants.GENDERS, default=None, blank=True, null=True)
    type = models.CharField(max_length=32, choices=constants.VILLAINS_TYPES, default=None, blank=True, null=True)
    homeworld = models.CharField(max_length=32, default=None, blank=True, null=True)
    series = models.ManyToManyField(Series, blank=True)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Weapon(Character):
    type = models.CharField(max_length=16, choices=constants.WEAPONS)
    parts = models.ManyToManyField('Weapon', blank=True)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Zord(Character):
    description = models.TextField()
    type = models.CharField(max_length=32, choices=constants.ZORD_TYPES)
    parts = models.ManyToManyField('Zord', blank=True)

    def __str__(self):
        return self.name

    @property
    def pilots(self):
        if self.piloted_by.count():
            return self.piloted_by.all()

        pilots = []
        for part in self.parts.all():
            pilots += part.pilots

        return pilots


@python_2_unicode_compatible
class ZordMode(models.Model):
    name = models.CharField(max_length=32, unique=True)
    zord = models.ForeignKey(Zord, related_name='modes')
    description = models.TextField()

    class Meta(object):
        ordering = ('name',)

    def __str__(self):
        return self.name
