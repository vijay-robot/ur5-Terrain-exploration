#program to run plotting and Ur5 program in one thread, not required
#not used
import threading
import serial
import time
import matplotlib.pyplot as plt
import random  # Replace with actual UR5 control library

# Serial Port Settings for Arduino
port = 'COM7'  # Update as needed
baud_rate = 9600

# Initialize serial connection
ser = serial.Serial(port, baud_rate, timeout=1)
time.sleep(2)  # Allow Arduino to reset after connection

# Initialize plot
plt.ion()  # Interactive mode on for real-time updating
fig, ax = plt.subplots()
x_data, y_data = [], []
line, = ax.plot(x_data, y_data)

plt.xlabel("Time")       # Label for the x-axis
plt.ylabel("Serial Data")       # Label for the y-axis
plt.title("Real Time plot of pressure ")          # Title of the plot

# Function to read and plot sensor data
def read_and_plot_sensor_data():
    while True:
        if ser.in_waiting > 0:
            line_data = ser.readline().decode('utf-8').strip()
            if line_data:
                try:
                    sensor_value = float(line_data)
                    print("Sensor Value:", sensor_value)

                    # Update plot data
                    x_data.append(time.time())  # Use timestamp as x-axis
                    y_data.append(sensor_value)
                    line.set_xdata(x_data)
                    line.set_ydata(y_data)
                    ax.relim()
                    ax.autoscale_view()
                    plt.draw()
                    plt.pause(0.01)

                except ValueError:
                    print("Error parsing sensor value")

# Function to control UR5
def control_ur5():
    while True:
        # Dummy command for UR5 control
        print("Controlling UR5")  # Replace with actual UR5 commands
        time.sleep(0.5)  # Adjust to match control rate

# Thread setup
#thread_sensor = threading.Thread(target=read_and_plot_sensor_data) #NOT to setup plotting as thread
thread_ur5 = threading.Thread(target=control_ur5) #set up ur5 thread

# Start both threads
#thread_sensor.start()
thread_ur5.start() # ur5 is the thread

# Keep main program running until threads are finished
#thread_sensor.join()
#thread_ur5.join()
read_and_plot_sensor_data()  #keep as main program else you get an error that matplotlib outside of main
# Close serial connection when done
ser.close()
