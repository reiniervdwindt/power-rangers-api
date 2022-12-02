from django.contrib import admin

from powerrangers.allies.forms import AllyAdminForm
from powerrangers.allies.models import Ally


@admin.register(Ally)
class AllyAdmin(admin.ModelAdmin):
    fields = ('name', 'description', 'series',)
    form = AllyAdminForm
    search_fields = ('name',)
