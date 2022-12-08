from django.db import models
from django.utils.translation import gettext_lazy as _


class Color(models.TextChoices):
    BLACK = 'black', _('Black'),
    BLUE = 'blue', _('Blue'),
    GREEN = 'green', _('Green'),
    PINK = 'pink', _('Pink'),
    RED = 'red', _('Red'),
    WHITE = 'white', _('White'),
    YELLOW = 'yellow', _('Yellow'),
