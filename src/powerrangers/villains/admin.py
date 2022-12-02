from django.contrib import admin

from powerrangers.villains.forms import VillainAdminForm
from powerrangers.villains.models import Villain


@admin.register(Villain)
class VillainAdmin(admin.ModelAdmin):
    form = VillainAdminForm
    search_fields = ('name', 'description',)
