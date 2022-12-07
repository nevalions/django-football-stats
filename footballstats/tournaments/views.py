from django.shortcuts import render
from django.views import View

from matches.models import Match
from seasons.models import _get_current_season_year, _get_other_seasons_years
from teams.models import Team
from tournaments.models import Tournament


# Tournaments list index page
class TournamentList(View):
    def get(self, request):
        current_season = _get_current_season_year()
        all_seasons = _get_other_seasons_years

        current_season_tournament = Tournament.objects.filter(season__in=current_season)
        other_years_season_tournaments = Tournament.objects.exclude(season__in=current_season)

        current_season_matches = Match.objects.filter(tournament__in=current_season_tournament)
        return render(request, 'tournaments/tournaments_list.html',
                      {'current_season': current_season,
                       'season_list': all_seasons,
                       'current_season_tournament': current_season_tournament,
                       'other_years_season_tournaments': other_years_season_tournaments,
                       'current_season_matches': current_season_matches
                       })


# Tournament index page
class TournamentDetail(View):
    def get(self, request, tournament_id, name, season):
        # current_tournament_name = name
        # current_season = season
        current_tournament = Tournament.objects.get(id=tournament_id)
        current_tournament_matches = Match.objects.filter(tournament=current_tournament)
        current_tournament_teams = Team.objects.filter(tournament=current_tournament)
        return render(request, 'tournaments/tournament_page.html',
                      {'current_tournament': current_tournament,
                       'current_tournament_matches': current_tournament_matches,
                       'current_tournament_teams': current_tournament_teams
                       })
