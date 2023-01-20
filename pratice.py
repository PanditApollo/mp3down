# importing all the necessary libraries
from __future__ import unicode_literals
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from youtubesearchpython import VideosSearch
import time
from pytube import YouTube
import moviepy.editor
import os
import requests
import eyed3
from eyed3.id3.frames import ImageFrame

# start time for the script
start_time = time.time()

# https://open.spotify.com/playlist/4Kjvwm5SLJmD63ahnoGxNf?si=a4853b37b9334673
cwd = os.getcwd()
# gets me the playlist_id, just the id
def get_playlist_id(str):
    playlist_id_0 = str.split("playlist/")
    playlist_id_1 = playlist_id_0[1]
    playlist_id_2 = playlist_id_1.split("?")
    return playlist_id_2[0]

# playlist_id     
playlist_id = get_playlist_id((input("Enter the playlist url: ")))


# authentication codes from spotify API
SPOTIPY_CLIENT_ID = '58db0e7ae228450ab8ba7341dd6c67de'
SPOTIPY_CLIENT_SECRET = 'a72c3ce108664c30904266207dc39c4a'


# authentication process for Spotify Client
auth_manager_alt = SpotifyClientCredentials(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET)

# spotipy library basic documentation
sp = spotipy.Spotify(auth_manager=auth_manager_alt)
set_of_tracks = sp.playlist_tracks(playlist_id)

# no_of songs in the playlists
no_of_songs = len(set_of_tracks['items']) # total number of songs in the playlist, max = 100


# dictionary that contains all the tracks
dict_of_track = (set_of_tracks["items"]) # Has all the tracks needed
print(dict_of_track)