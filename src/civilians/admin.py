from django import forms
from django.contrib import admin
from django.contrib.admin.widgets import FilteredSelectMultiple

from civilians.models import Civilian
from series.models import Series


class CivilianAdminForm(forms.ModelForm):
    series = forms.ModelMultipleChoiceField(
        queryset=Series.objects.filter(series__isnull=True),
        widget=FilteredSelectMultiple('series', is_stacked=False)
    )

    class Meta(object):
        model = Civilian
        exclude = ('pk',)


@admin.register(Civilian)
class CivilianAdmin(admin.ModelAdmin):
    form = CivilianAdminForm
    search_fields = ('name',)
