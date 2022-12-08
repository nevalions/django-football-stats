from django.shortcuts import render
from django.views import View

from matches.models import Match, _get_current_tournament_matches, _get_other_tournaments_matches
from seasons.models import Season


# Matches list page
class MatchList(View):
    def get(self, request):
        current_tournament_matches = Match.objects.filter(season__current_season=True)
        print(current_tournament_matches)
        return render(request, 'matches/matches_list.html',
                      {
                          'current_tournament_matches': current_tournament_matches,
                          'other_seasons_matches': _get_other_tournaments_matches().filter(
                              season__current_season=False)
                      })


# Match main page
class MatchDetail(View):
    def get(self, request, match_id, tournament, season):
        tournament_name = tournament
        season_year = season
        current_match = Match.objects.get(id=match_id)
        return render(request, 'matches/match_page.html',
                      {"current_match": current_match})
