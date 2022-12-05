from django.urls import path

from matches.views import MatchList, MatchDetail

urlpatterns = [
    path('<int:match_id>/<str:tournament>/', MatchDetail.as_view(), name='match_page'),  # matches page
    path('', MatchList.as_view(), name='match_list')  # matches list
]
