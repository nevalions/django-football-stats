from django.db import models
from django.urls import reverse

from matches.models import Match


# Match Online Stats

class StatsMatchOnline(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE, blank=False)
    score_team_a = models.IntegerField(default=0)
    score_team_b = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.match.pk} {self.match.season.year} {self.match.tournament.name} ' \
               f'{self.match.team_a.name}-{self.match.team_b.name}'

    class Meta:
        verbose_name = "Match Stats Online"

    def get_absolute_url(self):
        return reverse('stats_match_online_page', kwargs={
            'stats_match_online_id': self.pk,
            'match_id': self.match.pk,
            'match_team_a': self.match.team_a.name,
            'match_team_b': self.match.team_b.name,
        })
