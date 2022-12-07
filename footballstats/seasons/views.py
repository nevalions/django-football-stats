from django.shortcuts import render, redirect
from django.views.generic import View, CreateView

from seasons.forms import AddSeasonForm
from seasons.models import Season, _get_current_season_year, _get_other_seasons_years
from tournaments.models import Tournament


# Main index page from Seasons List
class MainPage(View):
    def get(self, request):
        current_season = _get_current_season_year()
        season_list = _get_other_seasons_years
        return render(request, 'index.html',
                      {"season_list": season_list,
                       "current_season": current_season,
                       })


# Seasons list page
class SeasonList(View):
    def get(self, request):
        current_season = _get_current_season_year()
        other_seasons_list = _get_other_seasons_years

        return render(request, 'seasons/season_list.html',
                      {
                          'current_season': current_season,
                          'other_seasons_list': other_seasons_list,
                      })


# Season index page
class SeasonDetail(View):
    def get(self, request, year, season_id):
        current_season = season_id
        current_season = Season.objects.get(year=year)
        current_season_tournaments = Tournament.objects.filter(season=current_season)
        return render(request, 'seasons/season_page.html',
                      {'current_season': current_season,
                       'current_season_tournaments': current_season_tournaments
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
