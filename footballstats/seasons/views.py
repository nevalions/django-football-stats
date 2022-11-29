import datetime

from django.shortcuts import render
from seasons.models import Season


# Seasons main page

def seasons_index_page(request):

    current_year = int(datetime.date.today().year)
    current_season = Season.objects.filter(year=current_year)
    all_seasons = Season.objects.exclude(year=current_year)

    return render(request, 'seasons/seasons_list.html', {"season_list": all_seasons, "current_season": current_season})

