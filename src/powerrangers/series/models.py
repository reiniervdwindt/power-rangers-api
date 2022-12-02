from django.db import models


class Series(models.Model):
    name = models.CharField(max_length=128)
    number = models.PositiveSmallIntegerField()
    year = models.PositiveSmallIntegerField()
    parent = models.ForeignKey(
        to='Series',
        default=None,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='seasons'
    )

    imdb_id = models.CharField(max_length=9, unique=True, default=None, blank=True, null=True)
    trakt_id = models.IntegerField(unique=True, default=None, blank=True, null=True)

    class Meta:
        ordering = ('year',)
        verbose_name_plural = 'series'

    def __str__(self):
        if self.parent:
            return '{series} ({season})'.format(series=self.parent.name, season=self.name)
        return '{name}'.format(name=self.name)


class Episode(models.Model):
    series = models.ForeignKey(Series, related_name='episodes', on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    number = models.PositiveSmallIntegerField()

    imdb_id = models.CharField(max_length=9, unique=True, default=None, blank=True, null=True)
    trakt_id = models.IntegerField(unique=True, default=None, blank=True, null=True)

    def __str__(self):
        return self.name
