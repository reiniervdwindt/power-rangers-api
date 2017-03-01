from django import forms
from django.contrib import admin
from django.contrib.admin.widgets import FilteredSelectMultiple

from allies.models import Ally
from series.models import Series


class AllyAdminForm(forms.ModelForm):
    series = forms.ModelMultipleChoiceField(
        queryset=Series.objects.filter(series__isnull=True),
        widget=FilteredSelectMultiple('series', is_stacked=False),
        required=False
    )

    class Meta:
        model = Ally
        exclude = ('pk',)


@admin.register(Ally)
class AllyAdmin(admin.ModelAdmin):
    fields = ('name', 'description', 'series',)
    form = AllyAdminForm
    search_fields = ('name',)
