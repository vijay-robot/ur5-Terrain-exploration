import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pandas as pd

# Load data from CSV file
data = pd.read_csv(r"C:\Users\vjc28\OneDrive\Documents\BIRL_UC\Terrain_sensingcode\terraindata\Leg_duty\SP\SP_c3_d1.txt")  # Update with the path to your CSV file
num_sensors = 16  # Assuming 16 sensors
sensor_data = [data.iloc[:, i].values for i in range(num_sensors)]  # Separate each column's data

# Set up the figure and the subplots (4x4 grid for 16 sensors)
fig, axes = plt.subplots(4, 4, figsize=(12, 12))
axes = axes.flatten()  # Flatten axes array for easy indexing

# Initialize the plot lines for each sensor
lines = []
for i in range(num_sensors):
    line, = axes[i].plot([], [], lw=2, label=f'Sensor {i+1}')
    lines.append(line)
    axes[i].set_xlim(0, len(sensor_data[0]))  # Adjust x-axis limits for each plot
    axes[i].set_ylim(np.min(sensor_data[i]), np.max(sensor_data[i]))  # Adjust y-axis limits per sensor
    axes[i].set_title(f'Sensor {i+1}')
    axes[i].legend(loc="upper right")

# Initialize function for animation
def init():
    for line in lines:
        line.set_data([], [])
    return lines

# Update function for animation
def update(frame):
    x = np.arange(frame)  # X-axis data up to the current frame
    for i in range(num_sensors):
        y = sensor_data[i][:frame]  # Y-axis data up to the current frame
        lines[i].set_data(x, y)
    return lines

# Animate with FuncAnimation
ani = animation.FuncAnimation(fig, update, frames=len(sensor_data[0]), init_func=init, blit=True, interval=100)

plt.tight_layout()
plt.show()
