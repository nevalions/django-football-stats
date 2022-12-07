from django import forms

from seasons.models import Season


class AddSeasonForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Season
        fields = ['year']