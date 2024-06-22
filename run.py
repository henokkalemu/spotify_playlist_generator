import feature_extraction, playlist_generator, spotify_api_caller, random_forests
import pandas as pd



def main():
    
    # get ids
    track_ids = spotify_api_caller.get_saved_tracks()
    
    # get user id 
    user_id = spotify_api_caller.sp.me()["id"]
    # return user_info['id']
    
    print(user_id)
    # use ids and get features
    audio_features = spotify_api_caller.get_audio_features(track_ids)
    
    #get features from tracks
    track_features_df = feature_extraction.extract_features(audio_features)
    
    # Display the DataFrame
    import ace_tools as tools
    tools.display_dataframe_to_user(name="Track Features", dataframe=track_features_df)
    
    # train model
    labels = ['chill', 'party', 'workout', 'focus'] *5
    
    # print("Shape of features:", track_features_df.shape)
    # print("Number of labels:", len(labels))
    
    model = random_forests.train_random_forests(track_features_df, labels)
    # use model to make prediction on tracks
    predictions = random_forests.predict_labels(model, track_features_df)
    
    
    playlist_generator.generate_playlists(user_id, track_ids, predictions)
    
    
    
    
    
    
    
    
if __name__ == "__main__":
    main()


# track_ids, track_feats, sp = spotify_api_caller.spotify_api_caller()

# X, y, df = feature_extraction.feat_extraction(track_feats)

# model, X = random_forests.random_forests(X, y)


# playlist_generator.playlist_generator(X, track_ids, track_feats, sp)
