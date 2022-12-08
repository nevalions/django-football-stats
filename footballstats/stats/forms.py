from django import forms

from stats.models import StatsMatchOnline


class AddStatsMatchOnline(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = StatsMatchOnline
        fields = '__all__'


class EditStatsMatchOnline(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = StatsMatchOnline
        fields = '__all__'
