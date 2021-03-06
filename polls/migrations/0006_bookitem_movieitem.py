# Generated by Django 2.1.1 on 2018-11-25 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_gameitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookid', models.IntegerField()),
                ('book_name', models.CharField(max_length=50)),
                ('book_type', models.CharField(max_length=50)),
                ('book_description', models.CharField(max_length=200)),
                ('book_rating', models.DecimalField(decimal_places=1, max_digits=2)),
                ('book_author', models.CharField(max_length=50)),
                ('book_year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='MovieItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movieid', models.IntegerField()),
                ('movie_name', models.CharField(max_length=50)),
                ('movie_type', models.CharField(max_length=50)),
                ('movie_description', models.CharField(max_length=200)),
                ('movie_rating', models.DecimalField(decimal_places=1, max_digits=2)),
                ('movie_director', models.CharField(max_length=50)),
                ('movie_year', models.IntegerField()),
            ],
        ),
    ]
