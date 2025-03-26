from django.contrib import admin
from .models import Artist, Album, Genre, Song, User, PlaybackHistory, Favorites

admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(Genre)
admin.site.register(Song)
admin.site.register(User)
admin.site.register(PlaybackHistory)
admin.site.register(Favorites)
