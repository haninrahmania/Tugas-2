# Generated by Django 4.1 on 2022-09-21 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywatchlist', '0003_alter_watchlistmovie_movie_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchlistmovie',
            name='movie_rating',
            field=models.IntegerField(default=0),
        ),
    ]
