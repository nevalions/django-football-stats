import datetime

from django.shortcuts import render
from seasons.models import Season, _get_current_season_year, _get_other_seasons_years
from tournaments.models import Tournament


# Main index page from Seasons List
def index_page(request):
    current_season = _get_current_season_year()
    all_seasons = _get_other_seasons_years

    return render(request, 'index.html', {"season_list": all_seasons, "current_season": current_season})


# Seasons list page

def seasons_list_page(request):
    current_season = _get_current_season_year()
    all_seasons = _get_other_seasons_years

    return render(request, 'seasons/seasons_list.html', {"season_list": all_seasons, "current_season": current_season})


# Season index page
def season_page(request, year):
    current_season = Season.objects.get(year=year)
    current_season_tournaments = Tournament.objects.filter(season=current_season)
    return render(request, 'seasons/season_page.html', {
        "current_season": current_season,
        "current_season_tournaments": current_season_tournaments})
