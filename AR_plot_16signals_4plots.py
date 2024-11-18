import serial
import time
import matplotlib.pyplot as plt
import csv
from datetime import datetime

# Initialize serial connection
port = 'COM5'  # Update this with your correct port
baud_rate = 9600
ser = serial.Serial(port, baud_rate, timeout=1)
time.sleep(2)  # Allow time for the connection
#csv_file_path = r"C:\Users\vjc28\OneDrive\Documents\BIRL_UC\Terrain_sensingcode\terraindata\Leg_duty\sensor_data.csv" #file path

# Set up the plot
plt.ion()  # Enable interactive mode
fig, axs = plt.subplots(4, 1, figsize=(10, 12))  # Create 4 subplots, each with 4 signals

# Initialize data storage for real-time plotting
x_data = list(range(50))  # Number of points to show on plot
y_data = [[0] * 50 for _ in range(16)]  # For the 16 signals
#axs.set_title('Analog Signals from ADS1115 Sensors 1 to 16')

# Plot lines for each sensor (16 total)
lines = []
for i in range(16):
    ax = axs[i // 4]  # Select the correct subplot
    line, = ax.plot(x_data, y_data[i], label=f'Sensor {i + 1}')
    lines.append(line)
    #ax.set_title('Analog Signals from ADS1115 Sensors 1 to 16')
# Set labels, titles, and legends for each subplot
for i, ax in enumerate(axs):
    ax.set_xlabel('Time')
    ax.set_ylabel('Sensor Value')
    ax.legend()
    #ax.set_title(f'Analog Signals from ADS1115 (Sensors {i * 4 + 1} to {min((i + 1) * 4, 16)})')
ax=axs[0] #set title only at the top, hence ax value is forced to the first plot
ax.set_title('Analog Signals from ADS1115 Sensors 1 to 16')
# Open CSV file to store data
csv_file = open('../../AppData/Roaming/JetBrains/PyCharmCE2024.1/scratches/sensor_data.csv', 'w', newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Timestamp'] + [f'Sensor{i + 1}' for i in range(16)])  # Header row


# Function to update the plot with new data
def update_plot(data):
    for i in range(16):
        y_data[i].append(data[i])
        y_data[i].pop(0)
        lines[i].set_ydata(y_data[i])

    for ax in axs:
        ax.relim()
        ax.autoscale_view()

    plt.draw()
    plt.pause(0.01)


# Main loop to read data from serial, update plot, and save to CSV
try:
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').strip()
            values = line.split(',')
            if len(values) == 16:  # Ensure we have 16 values
                try:
                    data = [int(val) for val in values]

                    # Update the plot with the new data
                    update_plot(data)

                    # Write to CSV with a timestamp
                    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    csv_writer.writerow([timestamp] + data)

                except ValueError:
                    print("Error parsing data.")
except KeyboardInterrupt:
    print("Exiting...")
finally:
    csv_file.close()  # Close the CSV file
    ser.close()  # Close the serial port
