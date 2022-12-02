from django.contrib import admin

from powerrangers.weapons.forms import WeaponAdminForm
from powerrangers.weapons.models import Weapon


@admin.register(Weapon)
class WeaponAdmin(admin.ModelAdmin):
    form = WeaponAdminForm
    list_display = ('name', 'type',)
    list_filter = ('type',)
