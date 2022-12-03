from django.db import models
from django.urls import reverse

from seasons.models import Season


# Tournament model
class Tournament(models.Model):
    season = models.ForeignKey(Season, on_delete=models.SET(1), verbose_name='seasons', blank=False)
    name = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=200)

    def __str__(self):
        return f' {self.name} {self.season}'

    class Meta:
        verbose_name = "Tournament"
        verbose_name_plural = "Tournament"

    def get_absolute_url(self):
        return reverse('tournament_page', kwargs={
            'tournament_id': self.pk,
            'name': self.name,
            'season': self.season})