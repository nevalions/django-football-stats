from django.db.models import Q
from django.shortcuts import render, redirect
from django.views import View

from matches.models import Match
from teams.forms import AddTeamForm
from teams.models import Team, _get_current_season_teams, _get_other_seasons_teams


# Teams list index page
class TeamList(View):
    def get(self, request):

        return render(request, 'teams/teams_list.html',
                      {
                          'current_season_teams': _get_current_season_teams(),
                          'other_seasons_teams': _get_other_seasons_teams(),
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
