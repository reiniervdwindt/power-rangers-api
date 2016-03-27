from django.contrib import admin
from nested_inline.admin import NestedModelAdmin, NestedStackedInline

from series.models import Series


class SeasonsAdmin(NestedStackedInline):
    extra = 0
    fk_name = 'parent'
    model = Series


class SeriesAdmin(NestedModelAdmin):
    inlines = (SeasonsAdmin,)
    model = Series

    def get_queryset(self, request):  # noqa
        return self.model.objects.filter(parent__isnull=True)


admin.site.register(Series, SeriesAdmin)
