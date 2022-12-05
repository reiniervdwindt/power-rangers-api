from django.db import models


class SeriesQuerySet(models.QuerySet):
    def series(self):
        return self.filter(parent__isnull=True)

    def seasons(self):
        return self.filter(parent__isnull=False)
