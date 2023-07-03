import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Load the environment variables from .env file
load_dotenv()

# Get the authentication credentials
client_id = os.getenv('SPOTIPY_CLIENT_ID')
client_secret = os.getenv('SPOTIPY_CLIENT_SECRET')

# Setup the Spotify client
sp = spotipy.Spotify(
  auth_manager=SpotifyOAuth(client_id=client_id,
                            client_secret=client_secret,
                            redirect_uri="http://127.0.0.1:5500/spotify/",
                            scope="user-top-read"))

# Get the top 100 most played tracks
results = sp.current_user_top_tracks(limit=100, time_range="long_term")

# Print the name, artist of each track and the genres of the artist
for i, item in enumerate(results['items']):
  artist_id = item['artists'][0]['id']  # Get the id of the first artist
  artist = sp.artist(artist_id)  # Fetch the artist object
  genres = ', '.join(artist['genres'])  # Convert the genres list to a string
  print(f"{i+1}. {item['name']} - {item['artists'][0]['name']} | Genres: {genres}")
