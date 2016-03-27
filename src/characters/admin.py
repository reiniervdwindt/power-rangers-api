from django.contrib import admin
from nested_inline.admin import NestedModelAdmin, NestedStackedInline

from .models import (Ally, Civilian, Monster, Ranger, Villain, Weapon, Zord,
                     ZordMode)


class AllyAdmin(admin.ModelAdmin):
    search_fields = ('name',)


class CivilianAdmin(admin.ModelAdmin):
    search_fields = ('name',)


class MonsterAdmin(admin.ModelAdmin):
    search_fields = ('name',)


class RangerAdmin(admin.ModelAdmin):
    search_fields = ('name',)


class VillainAdmin(admin.ModelAdmin):
    search_fields = ('name', 'description',)


class WeaponAdmin(admin.ModelAdmin):
    list_display = ('name', 'type',)
    list_filter = ('type',)


class ZordModesAdmin(NestedStackedInline):
    extra = 0
    model = ZordMode


class ZordAdmin(NestedModelAdmin):
    list_display = ('name', 'type',)
    list_filter = ('type',)
    search_fields = ('name', 'description',)


admin.site.register(Ally, AllyAdmin)
admin.site.register(Civilian, CivilianAdmin)
admin.site.register(Monster, MonsterAdmin)
admin.site.register(Ranger, RangerAdmin)
admin.site.register(Villain, VillainAdmin)
admin.site.register(Weapon, WeaponAdmin)
admin.site.register(Zord, ZordAdmin)
