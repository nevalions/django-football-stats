# Generated by Django 4.1.3 on 2022-11-29 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seasons', '0002_alter_season_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='season',
            name='year',
            field=models.IntegerField(default=1900),
        ),
    ]
