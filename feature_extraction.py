import pandas as pd
# from spotify_api_caller import track_feats



def extract_features(audio_features):

    df = pd.DataFrame(audio_features)

    features = ['danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness','acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo']

    track_features_df = df[features]

    return track_features_df