import rtde_control
import rtde_receive
import time
IP_address = "169.254.89.186"
rtde_r = rtde_receive.RTDEReceiveInterface(IP_address)
rtde_c = rtde_control.RTDEControlInterface(IP_address)
current_pose = rtde_r.getActualTCPPose()  # Returns [x, y, z, rx, ry, rz] in meters and radians
#actual_q = rtde_r.getActualQ()
#print(actual_q)
print("current_pose = ", current_pose)
initial_pose = current_pose

# Define incremental movement for joints (in radians)
dq = [0.00, 0.0, -0.130, 0, 0, 0]  # Example increments for each joint

# Calculate the new joint positions by adding the increments
#new_q = [actual_q[i] + dq[i] for i in range(len(actual_q))]
new_pose = [current_pose[i] + dq[i] for i in range(len(current_pose))]
#rint(new_q)
print(new_pose)
# Move to the new joint position using movej
rtde_c.moveL(new_pose,0.05, 0.2)  # Use appropriate acceleration (a=0.5) and speed (v=0.2)

# Wait for the movement to complete
time.sleep(6)
rtde_c.moveL(initial_pose,0.05, 0.2)


