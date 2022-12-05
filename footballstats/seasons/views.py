from django.shortcuts import render
from django.views.generic import View

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
        season_list = _get_other_seasons_years

        return render(request, 'seasons/season_list.html',
                      {"season_list": season_list,
                       "current_season": current_season,
                       })


# Season index page
class SeasonDetail(View):
    def get(self, request, year):
        current_season = Season.objects.get(year=year)
        current_season_tournaments = Tournament.objects.filter(season=current_season)
        return render(request, 'seasons/season_page.html',
                      {"current_season": current_season,
                       "current_season_tournaments": current_season_tournaments
                       })
