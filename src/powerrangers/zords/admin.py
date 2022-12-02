from django.contrib import admin

from powerrangers.zords.forms import ZordAdminForm
from powerrangers.zords.models import Mode, Zord


class ModeInlineAdmin(admin.StackedInline):
    model = Mode
    extra = 0


@admin.register(Zord)
class ZordAdmin(admin.ModelAdmin):
    form = ZordAdminForm
    inlines = (ModeInlineAdmin,)
    list_display = ('name', 'type',)
    list_filter = ('type',)
