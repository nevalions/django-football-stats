"""footballstats URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from matches.views import match_page
from seasons.views import seasons_list_page, index_page, season_page
from tournaments.views import tournaments_list_page, tournament_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_page, name='main'),  # seasons list MAIN INDEX
    path('seasons/', seasons_list_page, name='seasons_list'),  # seasons list
    path('seasons/<str:year>', season_page, name='season_page'),  # seasons page
    path('tournaments/', tournaments_list_page, name='tournaments_list'),  # tournaments list
    path('tournaments/<int:tournament_id>/<str:name>/<str:season>', tournament_page, name='tournament_page'),  # tournament page
    path('matches/<int:match_id>', match_page, name='match_page')  # matches page
]
