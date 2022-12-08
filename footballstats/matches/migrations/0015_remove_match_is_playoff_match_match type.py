# Generated by Django 4.1.3 on 2022-12-08 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0014_alter_match_options_match_is_playoff'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='is_playoff',
        ),
        migrations.AddField(
            model_name='match',
            name='Match Type',
            field=models.BooleanField(default=False, verbose_name='Is it playoff?'),
        ),
    ]