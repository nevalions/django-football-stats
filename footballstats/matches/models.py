from django.db import models
from django.urls import reverse

from tournaments.models import Tournament


# Match model
class Match(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.SET_NULL, null=True)
    date = models.DateField(blank=False)
    time = models.TimeField(blank=False, default='12:00:00')
    place = models.CharField(max_length=200, default='City and Stadium')
    field_length = models.IntegerField(default=90)
    team_a = models.CharField(max_length=200, default='Team A')
    team_b = models.CharField(max_length=200, default='Team B')

    def __str__(self):
        return f'{self.tournament.name} {self.tournament.season.year} {self.date.day}-{self.date.month} {self.team_a} vs. {self.team_b}'

    class Meta:
        verbose_name = "Match"
        verbose_name_plural = "Matches"
        ordering = ['-tournament', '-date']

    def get_absolute_url(self):
        return reverse('match_page', kwargs={
            'match_id': self.pk,
            'tournament': self.tournament.name})