# Generated by Django 4.1.3 on 2022-11-29 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('seasons', '0003_alter_season_year'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=200)),
                ('season', models.ForeignKey(on_delete=models.SET(1), to='seasons.season', verbose_name='seasons')),
            ],
            options={
                'verbose_name': 'Tournament',
                'verbose_name_plural': 'Tournament',
            },
        ),
    ]