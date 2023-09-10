from django.db import models

from apps.account.models import User

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Producer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    dateOfBirth = models.DateField()
    biography = models.TextField()
    photoURL = models.ImageField(upload_to='photos/')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Actors(models.Model):
    name = models.CharField(max_length=255)
    dateOfBirth = models.DateField()
    biography = models.TextField()
    photoURL = models.ImageField(upload_to='photos/')

    def __str__(self):
        return self.name
    

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    runtime = models.IntegerField()
    release_date = models.DateField()
    posterURL = models.ImageField(upload_to='posters/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    producer = models.ManyToManyField(Producer)
    video = models.FileField(upload_to='videos/')
    trailer = models.FileField(upload_to='trailers/')
    actors = models.ManyToManyField(Actors, through='MovieActors')

    def __str__(self):
        return self.title
    

class Review(models.Model):
    comment = models.TextField()
    rating = models.IntegerField()
    timestamp = models.DateTimeField()
    account = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

class Favorite(models.Model):
    account = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

class GenreMovie(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

class MovieActors(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    actor = models.ForeignKey(Actors, on_delete=models.CASCADE)
    is_main_actor = models.BooleanField(default=False)

    class Meta:
        unique_together = ('movie', 'actor')