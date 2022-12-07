from django.db import models
from django.urls import reverse

from teams.models import Team
from tournaments.models import Tournament, _get_current_season_tournaments, _get_other_years_tournaments


# Match model
class Match(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.SET_NULL, null=True)
    date = models.DateField(blank=False)
    time = models.TimeField(blank=False, default='12:00:00')
    place = models.CharField(max_length=200, default='City and Stadium')
    field_length = models.IntegerField(default=90)
    team_a = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, related_name='team_a')
    team_b = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, related_name='team_b')
    score_a = models.IntegerField(default=0)
    score_b = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.tournament.name} {self.tournament.season.year} ' \
               f'{self.date.day}-{self.date.month} {self.team_a.name} vs. {self.team_b.name}'

    class Meta:
        verbose_name = "Match"
        verbose_name_plural = "Matches"
        ordering = ['-date']

    def get_absolute_url(self):
        return reverse('match_page', kwargs={
            'match_id': self.pk,
            'tournament': self.tournament.name})


def _get_current_tournament_matches():
    return Match.objects.filter(tournament__in=_get_current_season_tournaments())


def _get_other_tournaments_matches():
    return Match.objects.filter(tournament__in=_get_other_years_tournaments())
