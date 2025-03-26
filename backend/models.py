from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Album(models.Model):
    title = models.CharField(max_length=255)
    release_date = models.DateField()
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Song(models.Model):
    title = models.CharField(max_length=255)
    duration = models.DurationField()
    total_play_time = models.PositiveIntegerField(default=0)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class PlaybackHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    play_count = models.PositiveIntegerField(default=1)

class Favorites(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
