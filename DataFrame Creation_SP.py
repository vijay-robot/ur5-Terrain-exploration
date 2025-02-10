#create dataframe and extract the statistical features of each terrain. Already created - not required to be used any more

import os
import pandas as pd
import numpy as np
from scipy.signal import welch  # For spectral features like power spectral density (PSD)

# Define the directory containing your CSV files
data_dir = r"C:/Users/vjc28/OneDrive/Documents/BIRL_UC/Terrain_sensingcode/terraindata/Leg_duty/Coir"


# Function to extract terrain, cycle, and duration from the filename
def extract_metadata(filename):
    parts = filename.split('_')
    terrain = parts[0]
    cycle = int(parts[1][1])  # Extract the number after 'c'
    duration = int(parts[2][1:].replace('.txt', ''))  # Extract the number after 'd'
    #duration = int(parts[2].replace('.txt', ''))  # Extract the number filename without 'd'
    return terrain, cycle, duration


# Function to calculate statistical and spectral features for each signal
def calculate_features(data):
    features = {}
    features['mean'] = np.mean(data)
    features['std'] = np.std(data)
    features['min'] = np.min(data)
    features['max'] = np.max(data)
    features['range'] = np.ptp(data)
    features['skewness'] = pd.Series(data).skew()
    features['kurtosis'] = pd.Series(data).kurtosis()

    # Spectral feature: Power Spectral Density (average power)
    freqs, psd = welch(data, fs=1.0)  # Assumes 1 Hz sampling frequency; update as needed
    features['spectral_power'] = np.sum(psd)  # Total power in the signal
    features['dominant_frequency'] = freqs[np.argmax(psd)]  # Frequency with the highest power

    return features


# Prepare an empty list to store all data
all_data = []

# Loop through all files in the directory
for filename in os.listdir(data_dir):
    if filename.endswith('.txt'):  # Ensure only processing text files
        filepath = os.path.join(data_dir, filename)

        # Read the CSV file (assuming it's whitespace-delimited)
        sensor_data = pd.read_csv(filepath, delimiter=',', header=None)

        # Extract metadata from the filename
        terrain, cycle, duration = extract_metadata(filename)

        # Calculate features for each sensor column
        for sensor_id in sensor_data.columns:
            sensor_signal = sensor_data[sensor_id]
            features = calculate_features(sensor_signal)
            features['terrain'] = terrain
            features['cycle'] = cycle
            features['duration'] = duration
            features['sensor'] = f"Sensor_{sensor_id + 1}"
            all_data.append(features)

# Create a DataFrame from the list of dictionaries
features_df = pd.DataFrame(all_data)

# Display the DataFrame
print(features_df)

# Save to a CSV file
output_file = "Coir_features_summary.csv"

# Combine directory and file name
output_path = os.path.join(data_dir, output_file)

# Save the DataFrame to the specified path
features_df.to_csv(output_path, index=False)

#features_df.to_csv("features_summary.csv", index=False) test file name not to be used
