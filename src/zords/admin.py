from django import forms
from django.contrib import admin
from django.contrib.admin.widgets import FilteredSelectMultiple

from zords.models import Mode, Zord


class ZordAdminForm(forms.ModelForm):
    parts = forms.ModelMultipleChoiceField(
        queryset=Zord.objects.all(),
        widget=FilteredSelectMultiple('zords', is_stacked=False)
    )

    class Meta:
        model = Zord
        exclude = ('pk',)


class ModeInlineAdmin(admin.StackedInline):
    model = Mode
    extra = 0


@admin.register(Zord)
class ZordAdmin(admin.ModelAdmin):
    form = ZordAdminForm
    inlines = (ModeInlineAdmin,)
    list_display = ('name', 'type',)
    list_filter = ('type',)
