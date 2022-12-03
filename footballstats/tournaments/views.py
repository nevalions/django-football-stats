import datetime

from django.shortcuts import render

from seasons.models import Season
from tournaments.models import Tournament


# Tournaments list index page
def tournaments_list_page(request):
    current_year = int(datetime.date.today().year)

    current_season = Season.objects.filter(year=current_year)
    all_seasons = Season.objects.exclude(year=current_year)

    current_season_tournament = Tournament.objects.filter(season__in=current_season)
    other_years_season_tournaments = Tournament.objects.exclude(season__in=current_season)

    return render(request, 'tournaments/tournaments_list.html', {
        'current_season': current_season,
        'season_list': all_seasons,
        'current_season_tournament': current_season_tournament,
        'other_years_season_tournaments': other_years_season_tournaments,

    }
                  )


# Tournament index page
def tournament_page(request, tournament_id, name, season):
    current_tournament_name = name
    current_season = season
    current_tournament = Tournament.objects.get(id=tournament_id)
    return render(request, 'tournaments/tournament.html', {"current_tournament": current_tournament})
