# Generated by Django 4.1.3 on 2022-12-08 18:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0017_alter_match_match type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='score_a',
        ),
        migrations.RemoveField(
            model_name='match',
            name='score_b',
        ),
    ]
