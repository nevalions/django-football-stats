from django.db import models
from django.db.models import Max, Count
from django.urls import reverse

from seasons.models import Season, _get_current_season, _get_other_seasons


# Tournament model
class Tournament(models.Model):
    season = models.ManyToManyField(Season)
    name = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=200, blank=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = "Tournament"
        verbose_name_plural = "Tournament"
        ordering = ['-name']

    def get_absolute_url(self):
        return reverse('tournament_page', kwargs={
            'tournament_id': self.pk,
            'name': self.name,
})


def _get_current_season_tournaments():
    return Tournament.objects.filter(season__in=_get_current_season())


def _get_other_years_tournaments():
    return Tournament.objects.filter(season__in=_get_other_seasons())
