#this program notrmaiizes the features and creates plot for each sensor to compare the difference of each feature between different terrains.

import pandas as pd
import matplotlib.pyplot as plt
import os
import matplotlib.colors as mcolors
import seaborn as sns

from sklearn.preprocessing import MinMaxScaler

# Normalize the feature data before plotting
scaler = MinMaxScaler()

# Directory containing your surface directories
base_dir = r"C:\Users\vjc28\OneDrive\Documents\BIRL_UC\Terrain_sensingcode\terraindata\Leg_duty"
output_dir = r"C:\Users\vjc28\OneDrive\Documents\BIRL_UC\Terrain_sensingcode\terraindata\Leg_duty\compare\normalized data"

# List of surface directories
surface_dirs = ['Coir', 'Al', 'SP', 'Pebble']

# Features to extract (modified to include skewness and kurtosis)
features_to_plot = ['mean', 'skewness', 'spectral_power']

# Prepare an empty list to store data for the boxplot
data_for_boxplot = []

# Prepare the labels for each surface
labels = []

# Loop through each surface directory
for surface_dir in surface_dirs:
    # Construct the file path for the surface summary CSV
    surface_file = f"{surface_dir}_features_summary.csv"
    surface_file_path = os.path.join(base_dir, surface_dir, surface_file)

    # Read the CSV file
    surface_data = pd.read_csv(surface_file_path)

    # Filter data for Sensor 1 and Cycle 1
    filtered_data = surface_data[(surface_data['sensor'] == 'Sensor_15') & (surface_data['cycle'] == 1)]

    # Extract the relevant features and add them to the list for plotting
    feature_data = []
    for feature in features_to_plot:
        filtered_data[feature] = scaler.fit_transform(filtered_data[[feature]])
        feature_data.append(filtered_data[feature].values)


    # Append the data for each surface
    data_for_boxplot.append(feature_data)

    # Append the label for the current surface
    labels.append(surface_dir)

# Define a list of colors for the surfaces
#colors = list(mcolors.TABLEAU_COLORS.values())
pastel_colors = sns.color_palette("pastel", n_colors=6)

# Create the boxplot
fig, ax = plt.subplots(figsize=(10, 6))

# Plot boxplots for each surface with different colors
positions = range(len(features_to_plot))  # Position of each feature on the x-axis
for i, feature_data in enumerate(data_for_boxplot):
    bp = ax.boxplot(
        feature_data,
        positions=[pos + i * 0.2 for pos in positions],
        widths=0.15,
        patch_artist=True,  # This enables coloring
    )
    # Shade the boxes with the corresponding color
    for box in bp['boxes']:
        box.set_facecolor(pastel_colors[i % len(pastel_colors)])


# Set x-ticks and labels
ax.set_xticks([pos + 0.3 for pos in positions])
ax.set_xticklabels(features_to_plot,fontsize=14)

# Set y-axis label
ax.set_ylabel('Feature Value (Normalized)',fontsize=14)

# Set plot title
ax.set_title('Comparison of Features for Sensor 15 Across Surfaces',fontsize = 16)

# Add legend with surface labels and colors
handles = [plt.Line2D([0], [0], color=pastel_colors[i % len(pastel_colors)], lw=4) for i in range(len(surface_dirs))]
#plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

# Adjust layout to prevent clipping

ax.legend(handles, labels, title="Surface Type", bbox_to_anchor=(1, 1),loc='upper right') #position legend using bbox

# Generate a variable filename based on the surface comparison
filename = f"normalized_sensor_15_cycle_1_comparison_{'_'.join(surface_dirs)}.png"
plt.tight_layout()
# Save the plot with the generated filename in the base directory
output_filename = os.path.join(output_dir, filename)
plt.savefig(output_filename)

# Show the plot
plt.show()
