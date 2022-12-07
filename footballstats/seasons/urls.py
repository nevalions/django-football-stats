from django.urls import path

from seasons.views import SeasonList, SeasonDetail, season_add_view

urlpatterns = [
    path('', SeasonList.as_view(), name='season_list'),  # seasons list
    path('<int:season_id>/<str:year>/', SeasonDetail.as_view(), name='season_page'),  # seasons page
    path('add/', season_add_view, name='season_add')  # season add page
]
