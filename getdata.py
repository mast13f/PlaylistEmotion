import config # .gitignore
import numpy as np
import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

auth_manager = SpotifyClientCredentials(client_id=config.SPOTIPY_CLIENT_ID, client_secret=config.SPOTIPY_CLIENT_SECRET)
sp = spotipy.Spotify(auth_manager=auth_manager)


features = ['danceability','energy','key','loudness','mode','speechiness','acousticness','instrumentalness','liveness','valence','tempo','time_signature']


def get_attributes(link, features):
    # get attributes of songs in playlist
    # link: list of spotify playlist links or album links
    # features: list of features to get
    old = []

    # for album links
    if link[0].startswith('https://open.spotify.com/album/'):
        for i in link:
            album_link = i
            track_uris = [x[ "external_urls"]["spotify"] for x in sp.album_tracks(album_link)["items"]]
            new = sp.audio_features(track_uris)
            new = [x for x in new if x is not None]
            old = old+new
            df = pd.DataFrame(new)[features]

    # for playlist links
    if link[0].startswith('https://open.spotify.com/playlist/'):
        for i in link:
            playlist_link = i
            playlist_URI = playlist_link.split("/")[-1].split("?")[0]
            track_uris = [x[ "track"]["uri"] for x in sp.playlist_tracks(playlist_URI)["items"]]
            new = sp.audio_features(track_uris)
            new = [x for x in new if x is not None]
            old = old+new
            df = pd.DataFrame(old)[features]
    return df




# get dataset
angry_playlists = ['https://open.spotify.com/playlist/37i9dQZF1EIhuCNl2WSFYd','https://open.spotify.com/playlist/37i9dQZF1EIgNZCaOGb0Mi','https://open.spotify.com/playlist/37i9dQZF1EId0AxZAYqRyP','https://open.spotify.com/playlist/37i9dQZF1EIcQR8GTL6NML','https://open.spotify.com/playlist/37i9dQZF1EIdjHvNyr7jpO']
happy_playlists = ['https://open.spotify.com/playlist/37i9dQZF1EIerWLYY5lG2u','https://open.spotify.com/playlist/37i9dQZF1EIcLfJYjuP7bx','https://open.spotify.com/playlist/37i9dQZF1EVJSvZp5AOML2','https://open.spotify.com/playlist/37i9dQZF1EIgG2NEOhqsD7','https://open.spotify.com/playlist/37i9dQZF1DXdPec7aLTmlC']
sad_playlists = ['https://open.spotify.com/playlist/37i9dQZF1EIdChYeHNDfK5','https://open.spotify.com/playlist/37i9dQZF1DWSqBruwoIXkA','https://open.spotify.com/playlist/37i9dQZF1EIg6gLNLe52Bd','https://open.spotify.com/playlist/37i9dQZF1DWW2hj3ZtMbuO','https://open.spotify.com/playlist/37i9dQZF1DWVV27DiNWxkR']
happy = get_attributes(happy_playlists, features)
sad = get_attributes(sad_playlists, features)
angry = get_attributes(angry_playlists, features)

# label
happy['label'] = '1'
sad['label'] = '0'
angry['label'] = '2'

# prepare training and testing data
merged = pd.concat([happy, sad, angry])
training = merged.sample(frac=0.6, random_state=25)
testing = merged.drop(training.index)
X_train = training.drop('label', axis=1)
Y_train = training['label']
X_test = testing.drop('label', axis=1)
Y_test = testing['label']

# encode labels
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
Y_train = le.fit_transform(Y_train)
Y_test = le.fit_transform(Y_test)