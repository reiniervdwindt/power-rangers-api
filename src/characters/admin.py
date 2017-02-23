from django.contrib import admin

from characters.models import (Ally, Civilian, Monster, Ranger, Villain,
                               Weapon, Zord, ZordMode)


@admin.register(Ally)
class AllyAdmin(admin.ModelAdmin):
    search_fields = ('name',)


@admin.register(Civilian)
class CivilianAdmin(admin.ModelAdmin):
    search_fields = ('name',)


@admin.register(Monster)
class MonsterAdmin(admin.ModelAdmin):
    search_fields = ('name',)


@admin.register(Ranger)
class RangerAdmin(admin.ModelAdmin):
    search_fields = ('name',)


@admin.register(Villain)
class VillainAdmin(admin.ModelAdmin):
    search_fields = ('name', 'description',)


@admin.register(Weapon)
class WeaponAdmin(admin.ModelAdmin):
    list_display = ('name', 'type',)
    list_filter = ('type',)


class ZordModesInline(admin.StackedInline):
    extra = 0
    model = ZordMode


@admin.register(Zord)
class ZordAdmin(admin.ModelAdmin):
    inlines = (ZordModesInline,)
    list_display = ('name', 'type',)
    list_filter = ('type',)
    search_fields = ('name', 'description',)
