import os
from googleapiclient.discovery import build
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from pytube import YouTube
import ffmpeg

SPOTIFY_CLIENT_ID = ""
SPOTIFY_CLIENT_SECRET = ""
YOUTUBE_API_KEY = ""

def get_spotify_playlist_tracks(playlist_id):
    '''
    This function checks our playlist then proceeds to create an empty list and then adds all the songs in format to the new list made
    '''
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=SPOTIFY_CLIENT_ID, client_secret=SPOTIFY_CLIENT_SECRET,))
    results = sp.playlist_tracks(playlist_id)
    tracks = []
    for track in results['items']:
        tracks.append((track['track']['name'], track['track']['artists'][0]['name']))
    return tracks

    # return [(track['track']['name'], track['track']['artists'][0]['name']) for track in results['items']]

def seach_yt_musicvideos(query):
    youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)
    search_response = youtube.search().list(q=query, part='id,snippet', type='video').execute()
    videos = []
    for search_result in search_response.get('items', []):
        if search_result['id']['kind'] == 'youtube#video':
            videos.append(search_result['id']['videoId'])
    return videos

def download_convert_mp3(video_id):
    youtube_url = f'https://www.youtube.com/watch?v={video_id}'
    yt = YouTube(youtube_url)
    stream = yt.streams.filter(only_audio=True).first()
    stream.download()
    original_filename = stream.default_filename
    mp3_filename = f"{os.path.splitext(original_filename)[0]}.mp3"
    ffmpeg.input(original_filename).output(mp3_filename).run()
    os.remove(original_filename)
    return mp3_filename

