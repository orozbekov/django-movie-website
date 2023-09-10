# Generated by Django 4.2.5 on 2023-09-05 10:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Actors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('dateOfBirth', models.DateField()),
                ('biography', models.TextField()),
                ('photoURL', models.ImageField(upload_to='photos/')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('runtime', models.IntegerField()),
                ('release_date', models.DateField()),
                ('posterURL', models.ImageField(upload_to='posters/')),
                ('video', models.FileField(upload_to='videos/')),
                ('trailer', models.FileField(upload_to='trailers/')),
            ],
        ),
        migrations.CreateModel(
            name='Producer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('dateOfBirth', models.DateField()),
                ('biography', models.TextField()),
                ('photoURL', models.ImageField(upload_to='photos/')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('rating', models.IntegerField()),
                ('timestamp', models.DateTimeField()),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movie')),
            ],
        ),
        migrations.CreateModel(
            name='MovieActors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_main_actor', models.BooleanField(default=False)),
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.actors')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movie')),
            ],
            options={
                'unique_together': {('movie', 'actor')},
            },
        ),
        migrations.AddField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(through='movies.MovieActors', to='movies.actors'),
        ),
        migrations.AddField(
            model_name='movie',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.category'),
        ),
        migrations.AddField(
            model_name='movie',
            name='producer',
            field=models.ManyToManyField(to='movies.producer'),
        ),
        migrations.CreateModel(
            name='GenreMovie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.genre')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movie')),
            ],
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movie')),
            ],
        ),
    ]