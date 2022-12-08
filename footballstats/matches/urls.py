from django.urls import path

from matches.views import MatchList, MatchDetail

urlpatterns = [
    path('<int:match_id>/<str:tournament>/<str:season>', MatchDetail.as_view(), name='match_page'),  # matches page
    path('', MatchList.as_view(), name='match_list')  # matches list
]
