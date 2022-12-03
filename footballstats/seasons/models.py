from django.db import models
from django.urls import reverse


# Seasons model
class Season(models.Model):
    year = models.IntegerField(blank=False, default=1900)
    description = models.TextField(max_length=200)

    def __str__(self):
        return f'Season {self.year}'

    class Meta:
        verbose_name = "Season"
        verbose_name_plural = "Seasons"

    def get_absolute_url(self):
        return reverse('season_page', kwargs={
            'year': self.year})
