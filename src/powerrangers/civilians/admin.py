from django.contrib import admin

from powerrangers.civilians.forms import CivilianAdminForm
from powerrangers.civilians.models import Civilian


@admin.register(Civilian)
class CivilianAdmin(admin.ModelAdmin):
    form = CivilianAdminForm
    search_fields = ('name',)
