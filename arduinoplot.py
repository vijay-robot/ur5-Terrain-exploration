import serial
import time
import matplotlib.pyplot as plt
import numpy as np

# Set up serial port and parameters
port = 'COM7'  # Update this to match your system
baud_rate = 9600
ser = serial.Serial(port, baud_rate, timeout=1)
time.sleep(2)  # Wait for Arduino to reset

# Set up the plot
plt.ion()  # Enable interactive mode
fig, ax = plt.subplots()
x_data = []  # List to store timestamps or indices
y_data = []  # List to store sensor values
line, = ax.plot(x_data, y_data, '-o')

plt.xlabel("Time")       # Label for the x-axis
plt.ylabel("Serial Data")       # Label for the y-axis
plt.title("Real Time plot of pressure ")          # Title of the plot

# Start reading and plotting data
try:
    start_time = time.time()
    while True:
        if ser.in_waiting > 0:
            line_data = ser.readline().decode('utf-8').strip()  # Read data
            if line_data.isdigit():  # Check if the data is numeric
                sensor_value = int(line_data)
                current_time = time.time() - start_time  # Calculate elapsed time

                # Append new data to lists
                x_data.append(current_time)
                y_data.append(sensor_value)

                # Limit the number of points on the plot for better visibility
                if len(x_data) > 100:
                    x_data.pop(0)
                    y_data.pop(0)

                # Update plot data
                line.set_xdata(x_data)
                line.set_ydata(y_data)
                ax.relim()  # Recalculate limits
                ax.autoscale_view()  # Rescale view

                # Draw updated plot
                plt.draw()
                plt.pause(0.01)

except KeyboardInterrupt:
    print("Stopped by user.")
finally:
    ser.close()
    plt.ioff()  # Turn off interactive mode
    plt.show()  # Show final plot when done
