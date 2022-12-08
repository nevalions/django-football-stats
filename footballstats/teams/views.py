from django.db.models import Q
from django.shortcuts import render, redirect
from django.views import View

from matches.models import Match
from seasons.models import _get_current_season, _get_other_seasons
from stats.models import StatsMatchOnline
from teams.forms import AddTeamForm
from teams.models import Team, _get_current_season_teams, _get_other_seasons_teams


# Teams list index page
class TeamList(View):
    def get(self, request):
        current_season = _get_current_season()
        current_season_teams = Team.objects.filter(tournament__season__in=current_season)
        other_seasons = _get_other_seasons()
        other_seasons_teams = Team.objects.filter(tournament__season__in=current_season)
        print(current_season_teams)
        return render(request, 'teams/teams_list.html',
                      {
                          'current_season_teams': current_season_teams,
                          'other_seasons_teams': other_seasons_teams,
                          'current_season': current_season,
                          'other_seasons': other_seasons
                      })


# Teams list index page
class TeamDetail(View):
    def get(self, request, team_id, name, tournament, tournament_id):
        selected_team = Team.objects.get(id=team_id)
        team_name = name
        team_current_tournament_matches = Match.objects.filter(
            Q(tournament=tournament_id) & Q(team_a=team_id) | Q(team_b=team_id))

        current_matches_stats = StatsMatchOnline.objects.filter(match__id__in=team_current_tournament_matches)

        # ???
        matches_no_stats = team_current_tournament_matches.exclude(id__in=current_matches_stats)

        return render(request, 'teams/team_page.html',
                      {
                          'selected_team': selected_team,
                          'team_current_tournament_matches': team_current_tournament_matches,
                          'current_season': _get_current_season(),
                          'current_matches_stats': current_matches_stats,
                          'matches_no_stats': matches_no_stats,
                      })


def team_add_view(request):
    error = ''
    template_name = 'teams/team_add.html'

    if request.method == 'POST':
        form = AddTeamForm(request.POST)
        if form.is_valid():
            team, created = Team.objects.get_or_create(**form.cleaned_data)
            return redirect('teams_list')
        else:
            error = 'Add Error'
    else:
        form = AddTeamForm()

    return render(request, template_name, {
        'form': form,
        'error: error': error
    })
