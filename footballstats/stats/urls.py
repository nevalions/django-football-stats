from django.urls import path

from stats.views import StatsMatchOnlineAddView, StatsMatchOnlineListView, StatsMatchOnlineView, \
    stats_online_match_edit

urlpatterns = [
    path('<int:stats_match_online_id>/<int:match_id>/<str:match_team_a>/<str:match_team_b>', StatsMatchOnlineView.as_view(),
         name='stats_match_online_page'),  # Online Match Stats page
    path('', StatsMatchOnlineListView.as_view(), name='stats_match_online_list'),  # Online Match Stats list
    path('add/', StatsMatchOnlineAddView.as_view(), name='stats_match_online_add_page'),  # Online Match Stats page
    path('edit/<int:stats_match_online_id>/', stats_online_match_edit,
         name='stats_match_online_edit'),  # Online Match Stats edit page
]
