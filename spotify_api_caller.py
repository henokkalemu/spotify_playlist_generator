import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv

# API CREDENTIALS
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
REDIRECT_URI = os.getenv('REDIRECT_URI')

scope= 'user-library-read user-read-private playlist-modify-public'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri= REDIRECT_URI,
    scope=scope))

def get_sp():
    return sp

def get_user_id():
    user_info = sp.me()
    return user_info['id']

    # COLLECT TRACKS
def get_saved_tracks():
    results = sp.current_user_saved_tracks()
    tracks = results['items']

    # Collect track IDs
    track_ids = [item['track']['id'] for item in tracks]

    return track_ids

# retrive audio features
def get_audio_features(track_ids):
    audio_features = []
    
    for i in range(0, len(track_ids), 50):
        batch = track_ids[i:i+50]
        audio_features += sp.audio_features(batch)
    
    return audio_features



