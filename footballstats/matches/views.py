from django.shortcuts import render
from django.views import View

from matches.models import Match
from seasons.models import _get_current_season_year, _get_other_seasons_years
from tournaments.models import Tournament


# Matches list page
class MatchList(View):
    def get(self, request):
        current_season = _get_current_season_year()
        all_seasons = _get_other_seasons_years

        current_tournament = Tournament.objects.filter(season__in=current_season)

        current_season_matches = Match.objects.filter(tournament__in=current_tournament)

        return render(request, 'matches/matches_list.html',
                      {"season_list": all_seasons,
                       "current_season": current_season,
                       "current_tournament": current_tournament,
                       "current_season_matches": current_season_matches
                       })


# Match main page
class MatchDetail(View):
    def get(self, request, match_id, tournament):
        tournament_name = tournament
        current_match = Match.objects.get(id=match_id)
        return render(request, 'matches/match_page.html',
                      {"current_match": current_match})
