from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.TextChoices):
    AXE = 'axe', _('Axe')
    BLASTER = 'blaster', _('Blaster')
    BOW = 'bow', _('Bow')
    DAGGER = 'dagger', _('Dagger')
    LANCE = 'lance', _('Lance')
    SWORD = 'sword', _('Sword')
