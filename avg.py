import os
import json

def calculate_average_features(json_file_path):
    """
    Calculates the average of each audio feature from a JSON file containing Spotify tracks data.
    """
    with open(json_file_path, 'r', encoding='utf-8') as f:
        tracks_data = json.load(f)

    # Initialize a dictionary to accumulate the sums of each feature
    features_sum = {}
    # Initialize the count of tracks
    tracks_count = len(tracks_data)

    # Sum up all the features' values
    for track in tracks_data:
        for feature, value in track['audio_features'].items():
            if feature in features_sum:
                features_sum[feature] += value
            else:
                features_sum[feature] = value

    # Calculate the average of each feature
    features_avg = {feature: value / tracks_count for feature, value in features_sum.items()}

    return features_avg

def format_for_d3_radar(json_file_path, output_file_path):
    """
    Formats averaged data from a JSON file to the D3 radar chart format and writes to a .txt file.
    """
    with open(json_file_path, 'r', encoding='utf-8') as f:
        averaged_data = json.load(f)

    # Transform the data into the required format
    formatted_data = []
    for time_range, features in averaged_data.items():
        formatted_time_range_data = []
        for feature, value in features.items():
            formatted_time_range_data.append({
                "axis": feature.capitalize(),
                "value": round(value, 2)  # Ensuring the value is rounded to two decimal places
            })
        formatted_data.append(formatted_time_range_data)

    # Write the formatted data to a .txt file
    with open(output_file_path, 'w', encoding='utf-8') as f:
        f.write('var data = ' + json.dumps(formatted_data, indent=2) + ';')

def prepare_data_for_radar_chart(averaged_data):
    """
    Prepares the data for the radar chart visualization.
    This function assumes `averaged_data` is a dictionary with keys as time ranges
    and values as dictionaries of the averaged audio features.
    """
    radar_chart_data = []

    for time_range, features in averaged_data.items():
        # Convert each set of features into the format expected by the radar chart
        feature_list = [{"axis": feature, "value": value} for feature, value in features.items()]
        radar_chart_data.append(feature_list)

    return radar_chart_data

def write_data_to_js_file(data, filename="averaged_data.js"):
    """
    Writes the prepared radar chart data to a JavaScript file.
    """
    with open(filename, 'w') as f:
        f.write("var data = " + json.dumps(data, indent=2) + ";")

# Example usage
if __name__ == "__main__":
    # Load your averaged data from the JSON file
    averaged_data_filename = os.path.join("data", "averaged_data.json")
    with open(averaged_data_filename, 'r') as f:
        averaged_data = json.load(f)
    
    # Prepare the data for the radar chart
    radar_chart_data = prepare_data_for_radar_chart(averaged_data)
    
    # Write the data to a JS file
    write_data_to_js_file(radar_chart_data)

