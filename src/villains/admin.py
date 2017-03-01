from django import forms
from django.contrib import admin
from django.contrib.admin.widgets import FilteredSelectMultiple

from series.models import Series
from villains.models import Villain


class VillainAdminForm(forms.ModelForm):
    series = forms.ModelMultipleChoiceField(
        queryset=Series.objects.filter(series__isnull=True),
        widget=FilteredSelectMultiple('series', is_stacked=False)
    )

    class Meta(object):
        model = Villain
        exclude = ('pk',)


@admin.register(Villain)
class VillainAdmin(admin.ModelAdmin):
    form = VillainAdminForm
    search_fields = ('name', 'description',)
