# code to plot in real time while reading from UR5 (not required)
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

# Set up the plot
plt.ion()  # Enable interactive mode
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6))

# Initialize data storage for real-time plotting
x_data = list(range(50))  # Number of points to show on plot
y_data_1 = [[0] * 50 for _ in range(8)]  # For the first 8 signals
y_data_2 = [[0] * 50 for _ in range(8)]  # For the last 8 signals

# Plot lines for each channel
lines_1 = [ax1.plot(x_data, y_data_1[i], label=f'Sensor {i + 1}')[0] for i in range(8)]
lines_2 = [ax2.plot(x_data, y_data_2[i], label=f'Sensor {i + 9}')[0] for i in range(8)]

# Set labels and legends
ax1.set_title('Analog Signals from ADS1115 (Sensors 1-8)')
ax1.set_xlabel('Time')
ax1.set_ylabel('Sensor Value')
ax1.legend()

ax2.set_title('Analog Signals from ADS1115 (Sensors 9-16)')
ax2.set_xlabel('Time')
ax2.set_ylabel('Sensor Value')
ax2.legend()

# Open CSV file to store data
csv_file = open('../../AppData/Roaming/JetBrains/PyCharmCE2024.1/scratches/sensor_data.csv', 'w', newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Timestamp'] + [f'Sensor{i + 1}' for i in range(16)])  # Header row


# Function to update the plot with new data
def update_plot(data):
    for i in range(8):
        y_data_1[i].append(data[i])
        y_data_1[i].pop(0)
        lines_1[i].set_ydata(y_data_1[i])

        y_data_2[i].append(data[i + 8])
        y_data_2[i].pop(0)
        lines_2[i].set_ydata(y_data_2[i])

    ax1.relim()
    ax1.autoscale_view()
    ax2.relim()
    ax2.autoscale_view()
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
