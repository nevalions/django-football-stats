from django.shortcuts import render, redirect
from django.views import View

from matches.models import Match
from stats.forms import AddStatsMatchOnline, EditStatsMatchOnline
from stats.models import StatsMatchOnline


# Match Stats List View
class StatsMatchOnlineListView(View):

    def get(self, request):

        template_name = 'stats/stats_match_online_list.html'
        form = AddStatsMatchOnline()

        current_season_matches = Match.objects.filter(season__current_season=True)
        print(current_season_matches)

        all_online_stats_match = StatsMatchOnline.objects.filter(match__in=current_season_matches)
        print(all_online_stats_match)

        return render(request, template_name,
                      {
                          'form': form,
                          'all_online_stats_match': all_online_stats_match,

                      })

    def post(self, request):
        error = ''
        if request.method == 'POST':
            form = AddStatsMatchOnline(request.POST)
            if form.is_valid():
                stats_match_online, created = StatsMatchOnline.objects.get_or_create(**form.cleaned_data)
                return redirect('stats_match_online_list')
            else:
                error = 'Add Error'
        else:
            form = AddStatsMatchOnline()

        return render(request)


# Match Stats Page View
class StatsMatchOnlineView(View):

    def get(self, request,
            stats_match_online_id,
            match_id,
            match_team_a,
            match_team_b):
        template_name = 'stats/stats_match_online_page.html'

        online_id = stats_match_online_id
        m_id = match_id
        team_a = match_team_a
        team_b = match_team_b
        selected_online_stats_match = StatsMatchOnline.objects.filter(pk=online_id)
        print(selected_online_stats_match)
        selected_match = Match.objects.filter(pk=m_id)

        return render(request, template_name,
                      {
                          'selected_online_stats_match': selected_online_stats_match,
                          'selected_match': selected_match,
                      })


# Match Stats Add View
def stats_online_match_add(request):
    error = ''
    if request.method == 'POST':
        form = AddStatsMatchOnline(request.POST)
        if form.is_valid():
            stats_match_online, created = StatsMatchOnline.objects.get_or_create(**form.cleaned_data)
            return redirect('stats_match_online_list')
        else:
            error = 'Add Error'
    else:
        form = AddStatsMatchOnline()

    return render(request)


class StatsMatchOnlineAddView(View):

    def get(self, request):
        template_name = 'stats/stats_match_online_add_page.html'
        form = AddStatsMatchOnline()

        return render(request, template_name,
                      {
                          'form': form,
                      })


# Match Stats Edit View
def stats_online_match_edit(request, stats_match_online_id):
    error = ''
    selected_online_stats_match = StatsMatchOnline.objects.filter(pk=stats_match_online_id)
    template_name = 'stats/stats_match_online_edit_page.html'

    form = EditStatsMatchOnline(request.POST or None, instance=selected_online_stats_match.first())
    if form.is_valid():
        form.save()
        return redirect('stats_match_online_list')
    else:
        error = 'Add Error'

    return render(request, template_name,
                  {
                      'form': form,
                      'selected_online_stats_match': selected_online_stats_match
                  })