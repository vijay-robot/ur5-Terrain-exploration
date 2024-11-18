# This code initializes the Ur5 to the position where it can begin exploring the terrain

import rtde_control
import rtde_receive
import time
IP_address = "169.254.89.186"
rtde_r = rtde_receive.RTDEReceiveInterface(IP_address)  # change the IP address depending on the robot
rtde_c = rtde_control.RTDEControlInterface(IP_address)
current_pose = rtde_r.getActualTCPPose()
print(current_pose)
#initial_pose = [0.06877919438666473, 0.7263623182556608, 0.3168792784885724, 1.0799130910461223, 2.82050807747802, -0.41275990666217305] # pose obtained after physically moving the robot to the desired position
initial_pose = [0.6393873927707303, -0.0015513064457848196, 0.3384147256744571, -2.7464280054950176, -1.0967293761207968, 0.47677626261045786]
rtde_c.moveL(initial_pose,0.05, 0.2) #return to initial position
print('initial pose =', initial_pose)
# Disconnect from the robot
rtde_c.disconnect()
rtde_r.disconnect()
