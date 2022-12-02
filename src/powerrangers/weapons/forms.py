from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple

from powerrangers.weapons.models import Weapon


class WeaponAdminForm(forms.ModelForm):
    parts = forms.ModelMultipleChoiceField(
        queryset=Weapon.objects.all(),
        widget=FilteredSelectMultiple('weapons', is_stacked=False),
        required=False
    )

    class Meta:
        model = Weapon
        exclude = ('pk',)
