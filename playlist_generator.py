import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotify_api_caller import sp

# helper method to create and populate playlist
def create_playlist(user_id, playlist_name, track_ids):

    new_playlist = sp.user_playlist_create(user_id, playlist_name)

    #
    sp.user_playlist_add_tracks(user_id, new_playlist['id'], track_ids)
    


def generate_playlists(user_id, track_ids, predictions):
    
    unique_labels = set(predictions)
    
    for label in unique_labels:
        playlist_name = f"{label} Playlist"
        tracks_for_label = [track_ids[i] for i in range(len(predictions)) if predictions[i] == label]
        create_playlist(user_id, playlist_name, tracks_for_label)