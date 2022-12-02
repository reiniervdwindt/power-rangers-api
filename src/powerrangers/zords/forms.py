from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple

from powerrangers.zords.models import Zord


class ZordAdminForm(forms.ModelForm):
    parts = forms.ModelMultipleChoiceField(
        queryset=Zord.objects.all(),
        widget=FilteredSelectMultiple('zords', is_stacked=False),
        required=False
    )

    class Meta:
        model = Zord
        exclude = ('pk',)
