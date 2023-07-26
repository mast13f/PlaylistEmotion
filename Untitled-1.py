import config


import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

auth_manager = SpotifyClientCredentials(client_id=config.SPOTIPY_CLIENT_ID, client_secret=config.SPOTIPY_CLIENT_SECRET)
sp = spotipy.Spotify(auth_manager=auth_manager)

playlist_link = 'https://open.spotify.com/playlist/37i9dQZF1DZ06evNZZcxVu'
playlist_URI = playlist_link.split("/")[-1].split("?")[0] 
track_uris = [x[ "track"]["uri"] for x in sp.playlist_tracks(playlist_URI)["items"]]

print(track_uris)

sp.audio_features(track_uris)