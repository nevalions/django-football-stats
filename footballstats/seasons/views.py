from django.shortcuts import render, redirect
from django.views.generic import View, CreateView

from seasons.forms import AddSeasonForm
from seasons.models import Season, _get_current_season, _get_other_seasons
from tournaments.models import Tournament


# Main index page from Seasons List
class MainPage(View):
    def get(self, request):
        return render(request, 'index.html',
                      {
                          'current_season': _get_current_season(),
                          'other_seasons_list': _get_other_seasons(),
                       })


# Seasons list page
class SeasonList(View):
    def get(self, request):
        return render(request, 'seasons/seasons_list.html',
                      {
                          'current_season': _get_current_season(),
                          'other_seasons_list': _get_other_seasons(),
                      })


# Season page
class SeasonDetail(View):
    def get(self, request, year, season_id):
        selected_season = season_id
        selected_season = Season.objects.get(year=year)
        selected_season_tournaments = Tournament.objects.filter(season=selected_season)
        return render(request, 'seasons/season_page.html',
                      {'selected_season': selected_season,
                       'selected_season_tournaments': selected_season_tournaments
                       })


def season_add_view(request):
    error = ''
    template_name = 'seasons/season_add.html'

    if request.method == 'POST':
        form = AddSeasonForm(request.POST)
        if form.is_valid():
            season, created = Season.objects.get_or_create(**form.cleaned_data)
            return redirect('season_list')
        else:
            error = 'Add Error'
    else:
        form = AddSeasonForm()

    return render(request, template_name, {
        'form': form,
        'error: error': error
    })
