from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.TextChoices):
    CARRIERZORD = 'carrierzord', _('Carrierzord')
    DINOZORD = 'dinozord', _('Dinozord')
    NINJAZORD = 'ninjazord', _('Ninjazord')
    SHOGUNZORD = 'shogunzord', _('Shogunzord')
    THUNDERZORD = 'thunderzord', _('Thunderzord')
