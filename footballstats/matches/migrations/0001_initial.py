# Generated by Django 4.1.3 on 2022-12-05 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tournaments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('place', models.CharField(default='City and Stadium', max_length=200)),
                ('field_length', models.IntegerField(default=90)),
                ('team_a', models.CharField(default='Team A', max_length=200)),
                ('team_b', models.CharField(default='Team B', max_length=200)),
                ('tournament', models.ForeignKey(on_delete=models.SET(1), to='tournaments.tournament', verbose_name='seasons')),
            ],
            options={
                'verbose_name': 'Match',
                'verbose_name_plural': 'Matches',
            },
        ),
    ]
