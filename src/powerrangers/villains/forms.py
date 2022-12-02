from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple

from powerrangers.series.models import Series
from powerrangers.villains.models import Villain


class VillainAdminForm(forms.ModelForm):
    series = forms.ModelMultipleChoiceField(
        queryset=Series.objects.filter(seasons__isnull=True),
        widget=FilteredSelectMultiple('series', is_stacked=False),
        required=False
    )

    class Meta:
        model = Villain
        exclude = ('pk',)
