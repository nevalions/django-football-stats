from django.urls import path

from tournaments.views import tournaments_list_page, tournament_page

urlpatterns = [
    path('', tournaments_list_page, name='tournaments_list'),  # tournaments list
    path('<int:tournament_id>/<str:name>/<str:season>',
         tournament_page, name='tournament_page'),  # tournament page
]
