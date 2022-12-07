from django.shortcuts import render
from django.views import View

from matches.models import Match
from teams.models import Team
from tournaments.models import Tournament, _get_current_season_tournaments, _get_other_years_tournaments


# Tournaments list index page
class TournamentList(View):
    def get(self, request):
        current_season_tournaments = _get_current_season_tournaments()
        other_years_season_tournaments = _get_other_years_tournaments()

        current_season_matches = Match.objects.filter(tournament__in=current_season_tournaments)
        return render(request, 'tournaments/tournaments_list.html',
                      {'current_season_tournaments': current_season_tournaments,
                       'other_years_season_tournaments': other_years_season_tournaments,
                       'current_season_matches': current_season_matches
                       })


# Tournament index page
class TournamentDetail(View):
    def get(self, request, tournament_id, name, season):
        # current_tournament_name = name
        # current_season = season
        selected_tournament = Tournament.objects.get(id=tournament_id)
        selected_tournament_matches = Match.objects.filter(tournament=selected_tournament)
        selected_tournament_teams = Team.objects.filter(tournament=selected_tournament)
        return render(request, 'tournaments/tournament_page.html',
                      {'selected_tournament': selected_tournament,
                       'selected_tournament_matches': selected_tournament_matches,
                       'selected_tournament_teams': selected_tournament_teams
                       })
