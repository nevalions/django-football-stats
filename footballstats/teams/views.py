from django.db.models import Q
from django.shortcuts import render
from django.views import View

from matches.models import Match
from seasons.models import _get_current_season_year, _get_other_seasons_years
from teams.models import Team
from tournaments.models import Tournament


# Teams list index page
class TeamList(View):
    def get(self, request):
        current_season_tournament = Tournament.objects.filter(season__in=_get_current_season_year())
        other_years_season_tournaments = Tournament.objects.filter(season__in=_get_other_seasons_years())

        current_season_teams = Team.objects.filter(tournament__in=current_season_tournament)
        other_seasons_teams = Team.objects.filter(tournament__in=other_years_season_tournaments)
        return render(request, 'teams/teams_list.html',
                      {'current_season_tournament': current_season_tournament,
                       'other_years_season_tournaments': other_years_season_tournaments,
                       'current_season_teams': current_season_teams,
                       'other_seasons_teams': other_seasons_teams,
                       })


# Teams list index page
class TeamDetail(View):
    def get(self, request, team_id, name, tournament, tournament_id):
        selected_team = Team.objects.get(id=team_id)
        team_name = name
        team_tournament = tournament
        team_current_tournament_matches = Match.objects.filter(
            Q(tournament=tournament_id) & Q(team_a=team_id) | Q(team_b=team_id)
        )
        print(team_current_tournament_matches)

        return render(request, 'teams/team_page.html',
                      {
                          'selected_team': selected_team,
                          'team_current_tournament_matches': team_current_tournament_matches,
                      })
