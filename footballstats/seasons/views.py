import datetime

from django.shortcuts import render
from seasons.models import Season
from tournaments.models import Tournament


# Main index page from Seasons List
def index_page(request):
    current_year = int(datetime.date.today().year)
    current_season = Season.objects.filter(year=current_year)
    all_seasons = Season.objects.exclude(year=current_year)

    return render(request, 'index.html', {"season_list": all_seasons, "current_season": current_season})


# Seasons list page

def seasons_list(request):
    current_year = int(datetime.date.today().year)
    current_season = Season.objects.filter(year=current_year)
    all_seasons = Season.objects.exclude(year=current_year)

    return render(request, 'seasons/seasons_list.html', {"season_list": all_seasons, "current_season": current_season})


# Season index page
def season_page(request, year):
    current_season = Season.objects.get(year=year)
    current_season_tournaments = Tournament.objects.filter(season=current_season)
    return render(request, 'seasons/season_page.html', {
        "current_season": current_season,
        "current_season_tournaments": current_season_tournaments})
