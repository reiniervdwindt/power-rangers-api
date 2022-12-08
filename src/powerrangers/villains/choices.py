from django.db import models
from django.utils.translation import gettext_lazy as _


class Gender(models.TextChoices):
    FEMALE = 'female', _('Female')
    MALE = 'male', _('Male')


class Category(models.TextChoices):
    ALCHEMIST = 'alchemist', _('Alchemist')
    BOSS = 'boss', _('Boss')
    GENERAL = 'general', _('General')
    HENCHMAN = 'henchman', _('Henchman')
    MINION = 'minion', _('Minion')
    SCIENTIST = 'scientist', _('Scientist')
