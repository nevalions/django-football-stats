from django import forms

from seasons.models import Season
from teams.models import Team


class AddTeamForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Team
        fields = '__all__'
