from django.contrib import admin

from series.models import Series


class SeasonsAdmin(admin.StackedInline):
    extra = 0
    fk_name = 'parent'
    model = Series


@admin.register(Series)
class SeriesAdmin(admin.ModelAdmin):
    exclude = ('parent',)
    inlines = (SeasonsAdmin,)
    list_display = ('name', 'number', 'year',)
    model = Series

    def get_queryset(self, request):  # noqa
        return self.model.objects.filter(parent__isnull=True)
