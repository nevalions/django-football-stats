from django.shortcuts import render
from django.views import View

from matches.models import Match
from seasons.models import _get_current_season_year, _get_other_seasons_years
from tournaments.models import Tournament


# Matches list page
class MatchList(View):
    def get(self, request):
        current_tournament = Tournament.objects.filter(season__in=_get_current_season_year())
        other_seasons_tournaments = Tournament.objects.filter(season__in=_get_other_seasons_years())

        current_tournament_matches = Match.objects.filter(tournament__in=current_tournament)
        other_tournaments_matches = Match.objects.filter(tournament__in=other_seasons_tournaments)

        return render(request, 'matches/matches_list.html',
                      {
                       'current_tournament': current_tournament,
                       'current_tournament_matches': current_tournament_matches,
                       'other_season_matches': other_tournaments_matches
                       })


# Match main page
class MatchDetail(View):
    def get(self, request, match_id, tournament):
        tournament_name = tournament
        current_match = Match.objects.get(id=match_id)
        return render(request, 'matches/match_page.html',
                      {"current_match": current_match})
