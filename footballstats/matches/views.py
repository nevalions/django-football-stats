from django.shortcuts import render
from django.views import View

from matches.models import Match, _get_current_tournament_matches, _get_other_tournaments_matches
from seasons.models import Season
from stats.models import StatsMatchOnline


# Matches list page
class MatchList(View):
    def get(self, request):
        current_tournament_matches = Match.objects.filter(season__current_season=True)

        # if exists stats???
        matches_stats = StatsMatchOnline.objects.filter(match__id__in=current_tournament_matches)

        # ???
        matches_no_stats = current_tournament_matches.exclude(id__in=matches_stats)

        return render(request, 'matches/matches_list.html',
                      {
                          'current_tournament_matches': current_tournament_matches,
                          'other_seasons_matches': _get_other_tournaments_matches().filter(
                              season__current_season=False),
                          'matches_stats': matches_stats,
                          'matches_no_stats': matches_no_stats,
                      })


# Match main page
class MatchDetail(View):
    def get(self, request, match_id, tournament, season):
        tournament_name = tournament
        season_year = season
        current_match = Match.objects.get(id=match_id)
        current_match_stats = StatsMatchOnline.objects.filter(match__id=match_id).first()
        return render(request, 'matches/match_page.html',
                      {
                          'current_match': current_match,
                          'current_match_stats': current_match_stats
                      })
