from django.db import models
from django.urls import reverse

from seasons.models import _get_current_season, Season
from teams.models import Team
from tournaments.models import Tournament, _get_current_season_tournaments, _get_other_years_tournaments


# Match model
class Match(models.Model):
    season = models.ForeignKey(Season, on_delete=models.SET_NULL, null=True)
    tournament = models.ForeignKey(Tournament, on_delete=models.SET_NULL, null=True)
    is_playoff = models.BooleanField(name='Match Type', verbose_name='Playoff Match', default=False)
    date = models.DateField(blank=False)
    time = models.TimeField(blank=False, default='12:00:00')
    place = models.CharField(max_length=200, default='City and Stadium')
    field_length = models.IntegerField(default=90)
    team_a = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, related_name='team_a')
    team_b = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, related_name='team_b')

    def __str__(self):
        return f'{self.tournament.name} {self.season.year} ' \
               f'{self.date.day}-{self.date.month} {self.team_a.name} vs. {self.team_b.name}'

    class Meta:
        verbose_name = "Match"
        verbose_name_plural = "Matches"
        ordering = ['season', '-date']

    def get_absolute_url(self):
        return reverse('match_page', kwargs={
            'match_id': self.pk,
            'tournament': self.tournament.name,
            'season': self.season.year
        })

    # def save(self, *args, **kwargs):
    #     self.score_a = StatsMatchOnline.score_team_a
    #     self.score_b = StatsMatchOnline.score_team_b
    #     super(Match, self).save(*args, **kwargs)


def _get_current_season_matches():
    return Match.objects.filter(tournament__season__in=_get_current_season())

def _get_current_tournament_matches():
    return Match.objects.filter(tournament__in=_get_current_season_tournaments())


def _get_other_tournaments_matches():
    return Match.objects.filter(tournament__in=_get_other_years_tournaments())
