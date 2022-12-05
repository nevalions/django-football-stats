from django.shortcuts import render

from matches.models import Match


# Match main page

def match_page(request, match_id):
    current_match = Match.objects.get(id=match_id)
    return render(request, 'matches/matches.html', {"current_match": current_match})
