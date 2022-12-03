# Generated by Django 4.1.3 on 2022-11-29 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seasons', '0003_alter_season_year'),
        ('matches', '0003_rename_field_legth_matches_field_length'),
    ]

    operations = [
        migrations.AddField(
            model_name='matches',
            name='season',
            field=models.ForeignKey(default=1, on_delete=models.SET(1), to='seasons.season', verbose_name='seasons'),
            preserve_default=False,
        ),
    ]