from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse
from django.db import connection
from datetime import timedelta

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.db import connection

def insert_data(request):
    """Inserts initial data into the database."""
    with connection.cursor() as cursor:
        # Insert Artists
        cursor.execute("INSERT INTO backend_artist (name) VALUES ('Eminem'), ('Drake'), ('Coldplay'), ('Adele');")

        # Insert Albums
        cursor.execute("INSERT INTO backend_album (title, release_date, artist_id) VALUES "
                       "('The Eminem Show', '2002-05-26', 1), "
                       "('Scorpion', '2018-06-29', 2), "
                       "('Parachutes', '2000-07-10', 3), "
                       "('21', '2011-01-24', 4);")

        # Insert Genres
        cursor.execute("INSERT INTO backend_genre (name) VALUES ('Hip-Hop'), ('Pop'), ('Rock'), ('R&B');")

        # Insert Songs
        cursor.execute("INSERT INTO backend_song (title, duration, total_play_time, album_id, artist_id, genre_id) VALUES "
                       "('Lose Yourself', '00:05:26', 0, 1, 1, 1), "
                       "('Gods Plan', '00:03:18', 0, 2, 2, 2), "
                       "('Yellow', '00:04:29', 0, 3, 3, 3), "
                       "('Rolling in the Deep', '00:03:48', 0, 4, 4, 4);")

        # Insert Users
        cursor.execute("INSERT INTO backend_user (name, email, password) VALUES "
                       "('Alice', 'alice@example.com', 'password123'), "
                       "('Bob', 'bob@example.com', 'securepassword'), "
                       "('Charlie', 'charlie@example.com', 'charliepass');")

        # Insert Playback History
        cursor.execute("INSERT INTO backend_playbackhistory (user_id, song_id, timestamp, play_count) VALUES "
                       "(1, 1, NOW(), 5), "
                       "(2, 2, NOW(), 3), "
                       "(3, 3, NOW(), 7);")

        # Insert Favorites
        cursor.execute("INSERT INTO backend_favorites (user_id, song_id) VALUES (1, 2), (2, 3), (3, 1);")

    return HttpResponse("Data inserted successfully!")

def get_artists(request):
    """Fetches all artists from the database."""
    with connection.cursor() as cursor:
        cursor.execute("SELECT id, name FROM backend_artist;")
        artists = cursor.fetchall()
    
    artist_list = [{"id": row[0], "name": row[1]} for row in artists]
    return JsonResponse(artist_list, safe=False)

def get_albums(request):
    """Fetches all albums from the database."""
    with connection.cursor() as cursor:
        cursor.execute("SELECT id, title, release_date, artist_id FROM backend_album;")
        albums = cursor.fetchall()
    
    album_list = [{"id": row[0], "title": row[1], "release_date": row[2], "artist_id": row[3]} for row in albums]
    return JsonResponse(album_list, safe=False)

def get_songs_by_genre(request, genre_id):
    """Fetches all songs of a given genre."""
    with connection.cursor() as cursor:
        cursor.execute("SELECT id, title, duration, album_id, artist_id FROM backend_song WHERE genre_id = %s;", [genre_id])
        songs = cursor.fetchall()
    
    song_list = [{"id": row[0], "title": row[1], "duration": str(row[2]), "album_id": row[3], "artist_id": row[4]} for row in songs]
    return JsonResponse(song_list, safe=False)

def get_user_favorites(request, user_id):
    """Fetches the favorite songs of a given user."""
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT s.id, s.title FROM backend_song s "
            "JOIN backend_favorites f ON s.id = f.song_id WHERE f.user_id = %s;", [user_id]
        )
        favorites = cursor.fetchall()
    
    favorite_list = [{"id": row[0], "title": row[1]} for row in favorites]
    return JsonResponse(favorite_list, safe=False)

def get_playback_history(request, user_id):
    """Fetches the playback history of a given user."""
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT s.id, s.title, ph.timestamp, ph.play_count FROM backend_song s "
            "JOIN backend_playbackhistory ph ON s.id = ph.song_id WHERE ph.user_id = %s;", [user_id]
        )
        history = cursor.fetchall()
    
    history_list = [{"id": row[0], "title": row[1], "timestamp": row[2], "play_count": row[3]} for row in history]
    return JsonResponse(history_list, safe=False)
