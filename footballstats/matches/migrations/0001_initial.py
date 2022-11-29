# Generated by Django 4.1.3 on 2022-11-29 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Matches',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('place', models.CharField(default='City and Stadium', max_length=200)),
                ('field_legth', models.IntegerField(default=90, max_length=3)),
                ('team_a', models.CharField(default='Team A', max_length=200)),
                ('team_b', models.CharField(default='Team B', max_length=200)),
            ],
            options={
                'verbose_name': 'Match',
                'verbose_name_plural': 'Matches',
            },
        ),
    ]