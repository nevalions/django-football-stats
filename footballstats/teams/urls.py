from django.urls import path

from teams.views import TeamList, TeamDetail, team_add_view

urlpatterns = [
    path('', TeamList.as_view(), name='teams_list'),  # teams list
    path('<int:team_id>/<str:name>/<str:tournament>/<int:tournament_id>',
         TeamDetail.as_view(), name='team_page'),  # team page
    path('add/', team_add_view, name='team_add'),  # team add page

]
