from django.contrib import admin

from powerrangers.monsters.forms import MonsterAdminForm
from powerrangers.monsters.models import Monster


@admin.register(Monster)
class MonsterAdmin(admin.ModelAdmin):
    form = MonsterAdminForm
    search_fields = ('name',)
