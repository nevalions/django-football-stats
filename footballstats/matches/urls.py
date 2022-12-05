from django.urls import path

from matches.views import match_page

urlpatterns = [
    path('<int:match_id>/<str:tournament>/', match_page, name='match_page')  # matches page
               ]
