# This code initializes the Ur5 to the position where it can begin exploring the terrain

import rtde_control
import rtde_receive
import time
rtde_r = rtde_receive.RTDEReceiveInterface("169.254.123.175")  # change the IP address depending on the robot
rtde_c = rtde_control.RTDEControlInterface("169.254.123.175")
initial_pose = [0.32135769966012545, 0.7695054026691359, 0.14026731814759869, 0.15315932371809668, -3.1127215686389444, -0.13182324039677407]  # pose obtained after physically moving the robot to the desired position
rtde_c.moveL(initial_pose,0.05, 0.2) #return to initial position
print('initial pose =', initial_pose)
# Disconnect from the robot
rtde_c.disconnect()
rtde_r.disconnect()
