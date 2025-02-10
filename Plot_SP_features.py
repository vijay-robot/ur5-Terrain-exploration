import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the features file
features_csv = "C:/Users/vjc28/OneDrive/Documents/BIRL_UC/Terrain_sensingcode/terraindata/Leg_duty/SP/features_summary.csv"
features_df = pd.read_csv(features_csv)

# Specify the duration for which you want the plots (e.g., 1 second)
selected_duration = 1

# Filter the data for the selected duration
duration_data = features_df[features_df['duration'] == selected_duration]

# List of sensors
sensors = sorted(duration_data['sensor'].unique())

# Features to plot
statistics = ['std','skewness', 'kurtosis']

# Create a plot for each sensor
for sensor in sensors:
    # Filter data for the specific sensor
    sensor_data = duration_data[duration_data['sensor'] == sensor]

    # Prepare data for bar plot
    stats_data = {stat: sensor_data[stat].values for stat in statistics}

    # Create a bar chart
    fig, ax = plt.subplots(figsize=(10, 6))

    bar_width = 0.2
    for cycle_idx in range(len(sensor_data['cycle'])):
        cycle_values = [stats_data[stat][cycle_idx] for stat in statistics]
        x_positions = [i + cycle_idx * bar_width for i in range(len(statistics))]
        ax.bar(x_positions, cycle_values, width=bar_width, label=f"Cycle {cycle_idx + 1}")

    # Customize the plot
    x_ticks_positions = [i + bar_width for i in range(len(statistics))]
    ax.set_xticks(x_ticks_positions)
    ax.set_xticklabels(statistics)
    ax.set_title(f"Statistics for {sensor} (Duration: {selected_duration} sec)")
    ax.set_xlabel("Statistics")
    ax.set_ylabel("Value")
    ax.legend(title="Cycle")
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Show or save the plot
    plt.tight_layout()
    plt.savefig(f"sensor_{sensor}_duration_{selected_duration}_stats.png")
    plt.show()
