# Generated by Django 4.1.3 on 2022-12-08 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seasons', '0005_remove_season_description_season_current_season'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='season',
            name='current_season',
        ),
        migrations.AddField(
            model_name='season',
            name='Season Type',
            field=models.BooleanField(default=False, verbose_name='Is it current year?'),
        ),
    ]
