# Generated by Django 4.1.3 on 2022-12-07 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0006_alter_tournament_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournament',
            name='description',
            field=models.TextField(blank=True, max_length=200),
        ),
    ]