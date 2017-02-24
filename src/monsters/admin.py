from django import forms
from django.contrib import admin
from django.contrib.admin.widgets import FilteredSelectMultiple

from monsters.models import Monster
from series.models import Series


class MonsterAdminForm(forms.ModelForm):
    series = forms.ModelMultipleChoiceField(
        queryset=Series.objects.filter(series__isnull=True),
        widget=FilteredSelectMultiple('series', is_stacked=False)
    )

    class Meta:
        model = Monster
        exclude = ('pk',)


@admin.register(Monster)
class MonsterAdmin(admin.ModelAdmin):
    form = MonsterAdminForm
    search_fields = ('name',)
