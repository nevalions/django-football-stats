import datetime

from django.db import models
from django.urls import reverse


# Season model
class Season(models.Model):
    year = models.IntegerField(blank=False, default=1900)
    current_season = models.BooleanField(default=False)

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


def _get_current_season():
    return Season.objects.filter(current_season=True)


def _get_other_seasons():
    return Season.objects.filter(current_season=False)
