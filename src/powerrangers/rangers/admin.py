from django.contrib import admin

from powerrangers.rangers.models import Appearance, Ranger


class AppearanceInlineAdmin(admin.StackedInline):
    model = Appearance
    extra = 0


@admin.register(Ranger)
class RangerAdmin(admin.ModelAdmin):
    inlines = (AppearanceInlineAdmin,)
