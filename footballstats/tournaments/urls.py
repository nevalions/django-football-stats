from django.urls import path

from tournaments.views import TournamentList, TournamentDetail

urlpatterns = [
    path('', TournamentList.as_view(), name='tournaments_list'),  # tournaments list
    path('<int:tournament_id>/<str:name>/<str:season>',
         TournamentDetail.as_view(), name='tournament_page')  # tournament page
]
