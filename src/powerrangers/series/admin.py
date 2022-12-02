from django.contrib import admin

from powerrangers.series.models import Series


class SeasonsInline(admin.StackedInline):
    extra = 0
    fk_name = 'parent'
    model = Series


@admin.register(Series)
class SeriesAdmin(admin.ModelAdmin):
    exclude = ('parent',)
    inlines = (SeasonsInline,)
    list_display = ('name', 'number', 'year',)
    model = Series

    def get_queryset(self, request):  # noqa
        return super().get_queryset(request).filter(parent__isnull=True)
