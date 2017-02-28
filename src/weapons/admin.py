from django import forms
from django.contrib import admin
from django.contrib.admin.widgets import FilteredSelectMultiple

from weapons.models import Weapon


class WeaponAdminForm(forms.ModelForm):
    parts = forms.ModelMultipleChoiceField(
        queryset=Weapon.objects.all(),
        widget=FilteredSelectMultiple('weapons', is_stacked=False)
    )

    class Meta:
        model = Weapon
        exclude = ('pk',)


@admin.register(Weapon)
class WeaponAdmin(admin.ModelAdmin):
    form = WeaponAdminForm
    list_display = ('name', 'type',)
    list_filter = ('type',)
