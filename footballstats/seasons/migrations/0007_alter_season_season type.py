# Generated by Django 4.1.3 on 2022-12-08 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seasons', '0006_remove_season_current_season_season_season type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='season',
            name='Season Type',
            field=models.BooleanField(default=False, verbose_name='Current year'),
        ),
    ]