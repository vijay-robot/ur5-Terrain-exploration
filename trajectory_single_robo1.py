import rtde_control
import rtde_receive
import time
rtde_r = rtde_receive.RTDEReceiveInterface("169.254.123.175")
rtde_c = rtde_control.RTDEControlInterface("169.254.123.175")
start_pose = rtde_r.getActualTCPPose()  # Returns [x, y, z, rx, ry, rz] in meters and radians

print('start_pose = ', start_pose)
initial_pose = start_pose

ds = 0.09 #displacement in y and z axis for the coir
ds1 = 0.095
dx = 0.3 #displacement in x axis, distance to move to the next terrain

#Each trajectory is one cycle

# this is the initial trajectory and covers two terrains areas
trajectory1 = [
    start_pose,  # Start at the actual pose
    [start_pose[0], start_pose[1], start_pose[2]- ds, start_pose[3], start_pose[4], start_pose[5]],  # 1 Move -5 cm along the z
    [start_pose[0], start_pose[1], start_pose[2], start_pose[3], start_pose[4], start_pose[5]],  # 1 Move +5 cm on z
    [start_pose[0], start_pose[1] - ds, start_pose[2], start_pose[3], start_pose[4], start_pose[5]],  #1 Move right in y
    [start_pose[0], start_pose[1] - ds, start_pose[2]-ds1, start_pose[3], start_pose[4], start_pose[5]], #1 Move -5 cm along the z
    [start_pose[0], start_pose[1] - ds, start_pose[2], start_pose[3], start_pose[4], start_pose[5]], # 1 Move +5 cm on z
    [start_pose[0], start_pose[1] - 2*ds, start_pose[2], start_pose[3], start_pose[4], start_pose[5]], #1 Move -5 cm on y
    [start_pose[0], start_pose[1] - 2*ds, start_pose[2]-ds1, start_pose[3], start_pose[4], start_pose[5]], #1 Move -5 on z
    [start_pose[0], start_pose[1] - 2*ds, start_pose[2], start_pose[3], start_pose[4], start_pose[5]], #1 move +5 on z
    [start_pose[0], start_pose[1] - 3*ds, start_pose[2], start_pose[3], start_pose[4], start_pose[5]], #1 Move -5 cm on y
    [start_pose[0], start_pose[1] - 3*ds, start_pose[2]-ds1, start_pose[3], start_pose[4], start_pose[5]], #1 Move -5 on z
    [start_pose[0], start_pose[1] - 3*ds, start_pose[2], start_pose[3], start_pose[4], start_pose[5]], #1 move +5 on z	: #2 begins with x position

    [start_pose[0] - dx, start_pose[1] - 3*ds, start_pose[2], start_pose[3], start_pose[4], start_pose[5]], #2 move to X for next cycle
    [start_pose[0] - dx, start_pose[1] - 3*ds, start_pose[2] - ds, start_pose[3], start_pose[4], start_pose[5]], # 2 Move -5 cm along the z
    [start_pose[0] - dx, start_pose[1] - 3*ds, start_pose[2] , start_pose[3], start_pose[4], start_pose[5]], # 2 Move +5 cm along the z
    [start_pose[0] - dx, start_pose[1] - 2*ds, start_pose[2] , start_pose[3], start_pose[4], start_pose[5]], # 2 Move left on y
    [start_pose[0] - dx, start_pose[1] - 2*ds, start_pose[2] - ds, start_pose[3], start_pose[4], start_pose[5]], # 2 Move -5 cm along the z
    [start_pose[0] - dx, start_pose[1] - 2*ds, start_pose[2] , start_pose[3], start_pose[4], start_pose[5]], # 2 Move +5 cm along the z
    [start_pose[0] - dx, start_pose[1] - ds, start_pose[2] , start_pose[3], start_pose[4], start_pose[5]], # 2 Move left on y
    [start_pose[0] - dx, start_pose[1] - ds, start_pose[2] - ds , start_pose[3], start_pose[4], start_pose[5]], # 2 Move -5 cm along the z
    [start_pose[0] - dx, start_pose[1] - ds, start_pose[2] , start_pose[3], start_pose[4], start_pose[5]], # 2 move +5 cm on z
    [start_pose[0] - dx, start_pose[1] , start_pose[2] , start_pose[3], start_pose[4], start_pose[5]], # 2 move left on y
    [start_pose[0] - dx, start_pose[1] , start_pose[2] - ds , start_pose[3], start_pose[4], start_pose[5]], # 2 move -5 cm on z
    [start_pose[0] - dx, start_pose[1] , start_pose[2] , start_pose[3], start_pose[4], start_pose[5]] # 2 move +5 cm on z

]

def move_along_trajectory(trajectory, acceleration=0.07, velocity=0.2): # for the first cycle only
    for pose in trajectory:
        rtde_c.moveL(pose, acceleration, velocity)
        time.sleep(3)  # Wait for 1 second at each pose (optional, for demonstration purposes)
        print(pose)

#this is the second trajectory, without the initial pose and generalized to be called multiple times

def move_along_trajectory_t(x,dx,acceleration=0.07, velocity=0.2): # for subsequent cycles, only one half for this code
    trajectory_t = [
        [start_pose[0] - x * dx, start_pose[1], start_pose[2], start_pose[3], start_pose[4], start_pose[5]],
        # 5 move to X for next cycle
        [start_pose[0] - x * dx, start_pose[1], start_pose[2] - ds1, start_pose[3], start_pose[4], start_pose[5]],
        # 5 Move -5 cm along the z
        [start_pose[0] - x * dx, start_pose[1], start_pose[2], start_pose[3], start_pose[4], start_pose[5]],
        # 5 Move +5 cm on z
        [start_pose[0] - x * dx, start_pose[1] - ds, start_pose[2], start_pose[3], start_pose[4], start_pose[5]],
        # 5 Move right in y
        [start_pose[0] - x * dx, start_pose[1] - ds, start_pose[2] - ds1, start_pose[3], start_pose[4], start_pose[5]],
        # 5 Move -5 cm along the z
        [start_pose[0] - x * dx, start_pose[1] - ds, start_pose[2], start_pose[3], start_pose[4], start_pose[5]],
        # 5 Move +5 cm on z
        [start_pose[0] - x * dx, start_pose[1] - 2 * ds, start_pose[2], start_pose[3], start_pose[4], start_pose[5]],
        # 5 Move -5 cm on y
        [start_pose[0] - x * dx, start_pose[1] - 2 * ds, start_pose[2] - ds1, start_pose[3], start_pose[4],
         start_pose[5]],  # 5 Move -5 on z
        [start_pose[0] - x * dx, start_pose[1] - 2 * ds, start_pose[2], start_pose[3], start_pose[4], start_pose[5]],
        # 5 move +5 on z
        [start_pose[0] - x * dx, start_pose[1] - 3 * ds, start_pose[2], start_pose[3], start_pose[4], start_pose[5]],
        # 5 Move -5 cm on y
        [start_pose[0] - x * dx, start_pose[1] - 3 * ds, start_pose[2] - ds1, start_pose[3], start_pose[4],
         start_pose[5]],  # 5 Move -5 on z
        [start_pose[0] - x * dx, start_pose[1] - 3 * ds, start_pose[2], start_pose[3], start_pose[4], start_pose[5]],
        # 5 move +5 on z	: #6 begins with x position

        [start_pose[0] - (x + 0.6) * dx, start_pose[1] - 3 * ds, start_pose[2], start_pose[3], start_pose[4],
          start_pose[5]],  # 6 move to X for next cycle
        [start_pose[0] - (x + 0.6) * dx, start_pose[1] - 3 * ds, start_pose[2] - ds, start_pose[3], start_pose[4],
         start_pose[5]],  # 6 Move -5 cm along the z
        [start_pose[0] - (x + 0.6) * dx, start_pose[1] - 3 * ds, start_pose[2], start_pose[3], start_pose[4],
        start_pose[5]],  # 6 Move +5 cm along the z
        [start_pose[0] - (x + 0.6) * dx, start_pose[1] - 2 * ds, start_pose[2], start_pose[3], start_pose[4],
        start_pose[5]],  # 6 Move left on y
        [start_pose[0] - (x + 0.6) * dx, start_pose[1] - 2 * ds, start_pose[2] - ds, start_pose[3], start_pose[4],
        start_pose[5]],  # 6 Move -5 cm along the z
        [start_pose[0] - (x + 0.6) * dx, start_pose[1] - 2 * ds, start_pose[2], start_pose[3], start_pose[4],
        start_pose[5]],  # 6 Move +5 cm along the z
        [start_pose[0] - (x + 0.6) * dx, start_pose[1] - ds, start_pose[2], start_pose[3], start_pose[4], start_pose[5]],
        # # 6 Move left on y
        [start_pose[0] - (x + 0.6) * dx, start_pose[1] - ds, start_pose[2] - ds, start_pose[3], start_pose[4],
         start_pose[5]],  # 6 Move -5 cm along the z
        [start_pose[0] - (x + 0.6) * dx, start_pose[1] - ds, start_pose[2], start_pose[3], start_pose[4], start_pose[5]],
        # # 6 move +5 cm on z
        [start_pose[0] - (x + 0.6) * dx, start_pose[1], start_pose[2], start_pose[3], start_pose[4], start_pose[5]],
        # # 6 move left on y
        [start_pose[0] - (x + 0.6) * dx, start_pose[1], start_pose[2] - ds, start_pose[3], start_pose[4], start_pose[5]],
        # # 6 move -5 cm on z
        [start_pose[0] - (x + 0.6) * dx, start_pose[1], start_pose[2], start_pose[3], start_pose[4], start_pose[5]]
        # # 6 move +5 cm on z

    ]
    for pose in trajectory_t:
        rtde_c.moveL(pose, acceleration, velocity)
        time.sleep(3)  # Wait for 1 second at each pose (optional, for demonstration purposes)
        print(pose)

# Move the robot along the defined trajectory
move_along_trajectory(trajectory1)  #first trajectory
time.sleep(1)
count = 1
print ('cycle = ',count,' ,x=', 0)

x=2                             #next trajectory
move_along_trajectory_t(x,dx)
count = count + 1
print ('cycle = ',count,' ,x=', x)
time.sleep(1)


rtde_c.moveL(initial_pose,0.08, 0.8) #return to initial position
print('initial pose =', initial_pose)
# Disconnect from the robot
rtde_c.disconnect()
rtde_r.disconnect()
