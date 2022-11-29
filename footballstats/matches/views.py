from django.shortcuts import render

from matches.models import Matches


# Match main page

def match_index_page(request):

    current_match = Matches.objects.filter(id=1)

    return render(request, 'matches/match.html', {
        "current_match": current_match
    }
    )
