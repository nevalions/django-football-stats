from django.urls import path

from seasons.views import SeasonList, SeasonDetail

urlpatterns = [
    path('', SeasonList.as_view(), name='season_list'),  # seasons list
    path('<str:year>/', SeasonDetail.as_view(), name='season_page')  # seasons page
]
