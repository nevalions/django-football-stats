from django.urls import path

from teams.views import TeamList, TeamDetail

urlpatterns = [
    path('', TeamList.as_view(), name='team_list'),  # teams list
    path('<int:team_id>/<str:name>/<str:tournament>',
         TeamDetail.as_view(), name='team_page')  # team page
]
