import pandas as pd
import matplotlib.pyplot as plt

# Path to your CSV file
csv_file_path = r"C:\Users\vjc28\OneDrive\Documents\BIRL_UC\Terrain_sensingcode\terraindata\Leg_duty\SP\SP_c3_d1.txt"

# Load data from the CSV file
data = pd.read_csv(csv_file_path)
df = pd.read_csv(csv_file_path)

# Get the number of rows and columns
num_rows, num_columns = df.shape
print(f"Number of rows: {num_rows}")
print(f"Number of columns: {num_columns}")
#plot(data.iloc[:, 2], label=f'Sensor {2}')
# Initialize a figure with 16 subplots (4 rows, 4 columns)
fig, axes = plt.subplots(4, 4, figsize=(15, 10), sharex=True)
fig.suptitle('Sensor Data Plots')

# Plot each sensor's data in its own subplot
for i in range(16):
    row = i // 4
    col = i % 4
    axes[row, col].plot(data.iloc[:, i], label=f'Sensor {i+1}')
    axes[row, col].set_title(f'Sensor {i+1}')
    axes[row, col].set_xlabel('Sample')
    axes[row, col].set_ylabel('Value')
    axes[row, col].legend()
len(data)
# Adjust layout to prevent overlap
plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()
