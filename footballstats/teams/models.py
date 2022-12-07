from django.db import models
from django.urls import reverse

from tournaments.models import Tournament


# Team model

class Team(models.Model):
    name = models.CharField(max_length=250, blank=False)
    tournament = models.ForeignKey(Tournament, null=True, on_delete=models.SET_NULL)
    description = models.TextField(max_length=200, blank=True)

    def __str__(self):
        return f'{self.name} - {self.tournament.name} {self.tournament.season.year}'

    class Meta:
        verbose_name = "Team"
        verbose_name_plural = "Teams"
        ordering = ['-tournament']

    def get_absolute_url(self):
        return reverse('team_page', kwargs={
            'team_id': self.pk,
            'name': self.name,
            'tournament': self.tournament,
            'tournament_id': self.tournament.pk
        })
