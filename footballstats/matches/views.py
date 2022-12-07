from django.shortcuts import render
from django.views import View

from matches.models import Match, _get_current_tournament_matches, _get_other_tournaments_matches


# Matches list page
class MatchList(View):
    def get(self, request):
        return render(request, 'matches/matches_list.html',
                      {
                          'current_tournament_matches': _get_current_tournament_matches(),
                          'other_season_matches': _get_other_tournaments_matches()
                      })


# Match main page
class MatchDetail(View):
    def get(self, request, match_id, tournament):
        tournament_name = tournament
        current_match = Match.objects.get(id=match_id)
        return render(request, 'matches/match_page.html',
                      {"current_match": current_match})
