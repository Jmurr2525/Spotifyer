import json

time_periods = ['short_term', 'medium_term', 'long_term']

for period in time_periods:
    file_path = f'data/spotify_data_{period}.json'
    with open(file_path, 'r') as file:
        songs_data = json.load(file)

    # Initialize dictionaries inside the loop
    min_values = {feature: float('inf') for feature in songs_data[0]["audio_features"]}
    max_values = {feature: float('-inf') for feature in songs_data[0]["audio_features"]}
    min_tracks = {feature: "" for feature in songs_data[0]["audio_features"]}
    max_tracks = {feature: "" for feature in songs_data[0]["audio_features"]}

    # Iterate through songs inside the loop
    for song in songs_data:
        for feature, value in song["audio_features"].items():
            if value < min_values[feature]:
                min_values[feature] = value
                min_tracks[feature] = song["track_name"]
            if value > max_values[feature]:
                max_values[feature] = value
                max_tracks[feature] = song["track_name"]

    # Print results for each time period within the loop
    print(f"Time Period: {period}")
    for feature in min_values:
        print(f"{feature.capitalize()} - Min: {min_values[feature]} (Track: {min_tracks[feature]}), Max: {max_values[feature]} (Track: {max_tracks[feature]})")
    print("\n")  # Add a newline for readability between time periods
