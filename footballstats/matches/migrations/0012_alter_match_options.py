# Generated by Django 4.1.3 on 2022-12-07 08:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0011_match_score_a_match_score_b_alter_match_team_a_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='match',
            options={'ordering': ['-date'], 'verbose_name': 'Match', 'verbose_name_plural': 'Matches'},
        ),
    ]