import pandas as pd
import matplotlib.pyplot as plt

# Load data from CSV file
csv_file_path = r"C:\Users\vjc28\OneDrive\Documents\BIRL_UC\Terrain_sensingcode\terraindata\Leg_duty\Coir\Coir_c3_d8.txt"
data = pd.read_csv(csv_file_path)
df = pd.read_csv(csv_file_path)

# Get the number of rows and columns
num_rows, num_columns = df.shape
# Plot data from column 2 (assuming column index 1 corresponds to column 2 in zero-indexing)
plt.figure(figsize=(10, 5))
plt.plot(data.iloc[:, 0], label='Sensor 2', color='b')  # Assuming the second column is desired
plt.title('Sensor 2 Data')
plt.xlabel('Sample Index')
plt.ylabel('Sensor Value')
plt.legend()
plt.show()



print(f"Number of rows: {num_rows}")
print(f"Number of columns: {num_columns}")