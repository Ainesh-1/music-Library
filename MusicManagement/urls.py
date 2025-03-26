"""
URL configuration for MusicManagement project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.urls import path
from backend.views import insert_data


from django.urls import path
from backend.views import get_artists, get_albums, get_songs_by_genre, get_user_favorites, get_playback_history

urlpatterns = [
    path("admin/", admin.site.urls), path("insert_data/", insert_data, name="insert_data"),
    path("artists/", get_artists, name="get_artists"),
    path("albums/", get_albums, name="get_albums"),
    path("songs/genre/<int:genre_id>/", get_songs_by_genre, name="get_songs_by_genre"),
    path("favorites/<int:user_id>/", get_user_favorites, name="get_user_favorites"),
    path("history/<int:user_id>/", get_playback_history, name="get_playback_history"),
]
