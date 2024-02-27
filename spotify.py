import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json

# Load the environment variables from .env file
load_dotenv()

# Get the authentication credentials
client_id = os.getenv('SPOTIPY_CLIENT_ID')
client_secret = os.getenv('SPOTIPY_CLIENT_SECRET')

# Setup the Spotify client
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                            client_secret=client_secret,
                            redirect_uri="http://127.0.0.1:5500/spotify/",
                            scope="user-top-read"))

def fetch_and_save_top_tracks(time_range):
    results = sp.current_user_top_tracks(limit=50, time_range=time_range)
    all_tracks_data = []

    for item in results['items']:
        track_id = item['id']
        track_name = item['name']
        artist_id = item['artists'][0]['id']
        artist_name = item['artists'][0]['name']
        
        audio_features = sp.audio_features(track_id)[0]
        artist_info = sp.artist(artist_id)
        genres = artist_info['genres']
        
        track_data = {
            "track_id": track_id,
            "track_name": track_name,
            "artist_name": artist_name,
            "genres": genres,
            "audio_features": {key: audio_features[key] for key in audio_features if key not in ['type', 'id', 'uri', 'track_href', 'analysis_url', 'duration_ms', 'time_signature']}
        }
        
        all_tracks_data.append(track_data)
    
    # File name based on time range
    file_name = f'spotify_data_{time_range}.json'
    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(all_tracks_data, f, indent=4)
    
    print(f"Data saved to {file_name}")

# Fetch and save data for each time range
for time_range in ['short_term', 'medium_term', 'long_term']:
    fetch_and_save_top_tracks(time_range)
