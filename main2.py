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
from bs4 import BeautifulSoup
import eyed3
from eyed3.id3.frames import ImageFrame
import json

# start time for the script
start_time = time.time()


cwd = os.getcwd()

def get_new_token():
    r = requests.request("GET", "https://open.spotify.com/")
    r_text = BeautifulSoup(r.content, "html.parser").find("script", {"id": "session"}).get_text()
    return json.loads(r_text)['accessToken']

def get_track1234(playlist_id, offset, limit, token):
    url = "https://api.spotify.com/v1/playlists/" + str(playlist_id) + "/tracks?offset=" + str(offset) + "&limit=" + str(limit) + "&market=GB"
    payload={}
    headers = {
      'authorization': 'Bearer ' + str(token),
      'Sec-Fetch-Dest': 'empty',
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    return json.loads(response.text)

a = get_track1234("4Kjvwm5SLJmD63ahnoGxNf", 0, 100, get_new_token())
print(a)
# dict_tracks = a['items']
# # b is a list
# c = 1
# song_name = dict_tracks[0]['track']['name']
# artist_name = dict_tracks[0]['track']['artists'][0]['name']
# album_name = dict_tracks[0]['track']['album']['name']
# cover_url = dict_tracks[0]['track']['album']['images'][0]['url']
# print(song_name)
# print(artist_name)
# print(album_name)
# print(cover_url)

