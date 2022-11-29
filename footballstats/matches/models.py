from django.db import models

# Match model
class Matches(models.Model):
    date = models.DateField(blank=False)
    time = models.TimeField(blank=False)
    place = models.CharField(max_length=200, default='City and Stadium')
    field_length = models.IntegerField(default=90)
    team_a = models.CharField(max_length=200, default='Team A')
    team_b = models.CharField(max_length=200, default='Team B')

    def __str__(self):
        return f'{self.date} {self.team_a} vs. {self.team_b}'

    class Meta:
        verbose_name = "Match"
        verbose_name_plural = "Matches"

