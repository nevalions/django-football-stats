# Generated by Django 4.1.3 on 2022-12-05 19:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0007_alter_match_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='match',
            options={'ordering': ['-date', 'tournament'], 'verbose_name': 'Match', 'verbose_name_plural': 'Matches'},
        ),
    ]
