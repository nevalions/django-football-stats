# Generated by Django 4.1.3 on 2022-12-07 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seasons', '0005_remove_season_description_season_current_season'),
        ('tournaments', '0007_alter_tournament_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tournament',
            options={'verbose_name': 'Tournament', 'verbose_name_plural': 'Tournament'},
        ),
        migrations.RemoveField(
            model_name='tournament',
            name='season',
        ),
        migrations.AddField(
            model_name='tournament',
            name='season',
            field=models.ManyToManyField(to='seasons.season'),
        ),
    ]
