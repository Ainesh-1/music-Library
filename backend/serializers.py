from rest_framework import serializers
from .models import Artist, Album, Song, Genre, PlaybackHistory, Favorites, User

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'

class AlbumSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer()
    
    class Meta:
        model = Album
        fields = '__all__'

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class SongSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer()
    album = AlbumSerializer()
    genre = GenreSerializer()
    
    class Meta:
        model = Song
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email']

class PlaybackHistorySerializer(serializers.ModelSerializer):
    song = SongSerializer()
    
    class Meta:
        model = PlaybackHistory
        fields = '__all__'

class FavoritesSerializer(serializers.ModelSerializer):
    song = SongSerializer()
    
    class Meta:
        model = Favorites
        fields = '__all__'
