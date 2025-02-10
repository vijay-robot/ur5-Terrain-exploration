import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load the data
# Path to your CSV file, 'r' means raw string, important if you use back-slash
base_dir = r"C:\Users\vjc28\OneDrive\Documents\BIRL_UC\Terrain_sensingcode\terraindata\Leg_duty"
output_dir = r"C:\Users\vjc28\OneDrive\Documents\BIRL_UC\Terrain_sensingcode\terraindata\Leg_duty\compare"
# Specify the filename
filename = r"Pebble\Pebble_features_summary.csv"

# Construct the full file path
csv_file_path = os.path.join(base_dir, filename)
data = pd.read_csv(csv_file_path)

# Extract surface type from the filename
surface_type = os.path.basename(filename).split('_')[0]  # Extract the part before _features

# Set sensor dynamically (for example, filter the data for one sensor at a time)
sensor_name = 'Sensor_1'  # Replace with dynamic extraction logic if needed

## Features excluding spectral power
features = ['std', 'skewness', 'kurtosis']

# Create subplots for the features (std, skewness, kurtosis)
fig, axes = plt.subplots(1, len(features), figsize=(16, 6))

# Plot each feature in a separate subplot as a boxplot
for i, feature in enumerate(features):
    sns.boxplot(
        data=data[data['sensor'] == sensor_name],  # Filter data for the specific sensor
        x='duration',
        y=feature,
        ax=axes[i],
        palette='viridis'
    )
    axes[i].set_title(f"Variability of {feature.capitalize()} for {sensor_name} ({surface_type})")
    axes[i].set_xlabel('Duration (s)')
    axes[i].set_ylabel('Value')

# Adjust layout to avoid overlap
plt.tight_layout()

# Save the first plot
output_filename = os.path.join(base_dir, f"{surface_type}_{sensor_name}_variability_other_features.png")
plt.savefig(output_filename)

# Show the first plot
plt.show()

# Plot spectral power separately in a new figure
fig, ax = plt.subplots(figsize=(8, 6))

# Plot the spectral power
sns.boxplot(
    data=data[data['sensor'] == sensor_name],  # Filter data for the specific sensor
    x='duration',
    y='spectral_power',
    ax=ax,
    palette='viridis'
)

# Set title and labels for spectral power plot
ax.set_title(f"Spectral Power Variability for {sensor_name} ({surface_type})")
ax.set_xlabel('Duration (s)')
ax.set_ylabel('Spectral Power')

# Save the spectral power plot
output_filename_spectral = os.path.join(output_dir, f"{surface_type}_{sensor_name}_spectral_power.png")
plt.savefig(output_filename_spectral)

# Show the spectral power plot
plt.show()