from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple

from powerrangers.allies.models import Ally
from powerrangers.series.models import Series


class AllyAdminForm(forms.ModelForm):
    series = forms.ModelMultipleChoiceField(
        queryset=Series.objects.filter(seasons__isnull=True),
        widget=FilteredSelectMultiple('series', is_stacked=False),
        required=False
    )

    class Meta:
        model = Ally
        exclude = ('pk',)
