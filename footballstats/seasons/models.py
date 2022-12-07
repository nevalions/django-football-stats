import datetime

from django.db import models
from django.urls import reverse


# Season model
class Season(models.Model):
    year = models.IntegerField(blank=False, default=1900)
    description = models.TextField(max_length=200)

    def __str__(self):
        return f'Season {self.year}'

    class Meta:
        verbose_name = "Season"
        verbose_name_plural = "Seasons"
        ordering = ['-year']

    def get_absolute_url(self):
        return reverse('season_page', kwargs={
            'year': self.year,
            'season_id': self.pk
        })


def _get_current_season_year():
    return Season.objects.filter(year=int(datetime.date.today().year))


def _get_other_seasons_years():
    return Season.objects.exclude(year=int(datetime.date.today().year)).order_by('-year')
