from django.shortcuts import render

from matches.models import Matches


# Match main page

def match_index_page(request, match_id):
    current_match = Matches.objects.get(id=match_id)
    return render(request, 'matches/match.html', {"current_match": current_match})
