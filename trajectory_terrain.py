import rtde_control
import rtde_receive
import time
rtde_r = rtde_receive.RTDEReceiveInterface("169.254.123.175")
rtde_c = rtde_control.RTDEControlInterface("169.254.123.175")
start_pose = rtde_r.getActualTCPPose()  # Returns [x, y, z, rx, ry, rz] in meters and radians
#actual_q = rtde_r.getActualQ()
#print(actual_q)
print('start_pose = ', start_pose)
initial_pose = start_pose

ds = 0.05 #displacement in each direction

#Each trajectory is one cycle
trajectory1 = [
    start_pose,  # Start at the actual pose
    [start_pose[0], start_pose[1], start_pose[2]- ds, start_pose[3], start_pose[4], start_pose[5]],  # 1 Move -5 cm along the z
    [start_pose[0], start_pose[1], start_pose[2], start_pose[3], start_pose[4], start_pose[5]],  # 1 Move +5 cm on z
    [start_pose[0], start_pose[1] - ds, start_pose[2], start_pose[3], start_pose[4], start_pose[5]],  #1 Move right in y
    [start_pose[0], start_pose[1] - ds, start_pose[2]-ds, start_pose[3], start_pose[4], start_pose[5]], #1 Move -5 cm along the z
    [start_pose[0], start_pose[1] - ds, start_pose[2], start_pose[3], start_pose[4], start_pose[5]], # 1 Move +5 cm on z
    [start_pose[0], start_pose[1] - 2*ds, start_pose[2], start_pose[3], start_pose[4], start_pose[5]], #1 Move -5 cm on y
    [start_pose[0], start_pose[1] - 2*ds, start_pose[2]-ds, start_pose[3], start_pose[4], start_pose[5]], #1 Move -5 on z
    [start_pose[0], start_pose[1] - 2*ds, start_pose[2], start_pose[3], start_pose[4], start_pose[5]], #1 move +5 on z
    [start_pose[0], start_pose[1] - 3*ds, start_pose[2], start_pose[3], start_pose[4], start_pose[5]], #1 Move -5 cm on y
    [start_pose[0], start_pose[1] - 3*ds, start_pose[2]-ds, start_pose[3], start_pose[4], start_pose[5]], #1 Move -5 on z
    [start_pose[0], start_pose[1] - 3*ds, start_pose[2], start_pose[3], start_pose[4], start_pose[5]], #1 move +5 on z	: #2 begins with x position

    [start_pose[0] - ds, start_pose[1] - 3*ds, start_pose[2], start_pose[3], start_pose[4], start_pose[5]], #2 move to X for next cycle
    [start_pose[0] - ds, start_pose[1] - 3*ds, start_pose[2] - ds, start_pose[3], start_pose[4], start_pose[5]], # 2 Move -5 cm along the z
    [start_pose[0] - ds, start_pose[1] - 3*ds, start_pose[2] , start_pose[3], start_pose[4], start_pose[5]], # 2 Move +5 cm along the z
    [start_pose[0] - ds, start_pose[1] - 2*ds, start_pose[2] , start_pose[3], start_pose[4], start_pose[5]], # 2 Move left on y
    [start_pose[0] - ds, start_pose[1] - 2*ds, start_pose[2] - ds, start_pose[3], start_pose[4], start_pose[5]], # 2 Move -5 cm along the z
    [start_pose[0] - ds, start_pose[1] - 2*ds, start_pose[2] , start_pose[3], start_pose[4], start_pose[5]], # 2 Move +5 cm along the z
    [start_pose[0] - ds, start_pose[1] - ds, start_pose[2] , start_pose[3], start_pose[4], start_pose[5]], # 2 Move left on y
    [start_pose[0] - ds, start_pose[1] - ds, start_pose[2] - ds , start_pose[3], start_pose[4], start_pose[5]], # 2 Move -5 cm along the z
    [start_pose[0] - ds, start_pose[1] - ds, start_pose[2] , start_pose[3], start_pose[4], start_pose[5]], # 2 move +5 cm on z
    [start_pose[0] - ds, start_pose[1] , start_pose[2] , start_pose[3], start_pose[4], start_pose[5]], # 2 move left on y
    [start_pose[0] - ds, start_pose[1] , start_pose[2] - ds , start_pose[3], start_pose[4], start_pose[5]], # 2 move -5 cm on z
    [start_pose[0] - ds, start_pose[1] , start_pose[2] , start_pose[3], start_pose[4], start_pose[5]] # 2 move +5 cm on z

]
# cycles 3 and 4
trajectory2 = [
    [start_pose[0] - 2*ds, start_pose[1], start_pose[2], start_pose[3], start_pose[4], start_pose[5]], #3 move to X for next cycle
    [start_pose[0] - 2*ds, start_pose[1], start_pose[2]- ds, start_pose[3], start_pose[4], start_pose[5]],  #3 Move -5 cm along the z
    [start_pose[0] - 2*ds, start_pose[1], start_pose[2], start_pose[3], start_pose[4], start_pose[5]],  #3 Move +5 cm on z
    [start_pose[0] - 2*ds, start_pose[1] - ds, start_pose[2], start_pose[3], start_pose[4], start_pose[5]],  #3 Move right in y
    [start_pose[0] - 2*ds, start_pose[1] - ds, start_pose[2]-ds, start_pose[3], start_pose[4], start_pose[5]], #3 Move -5 cm along the z
    [start_pose[0] - 2*ds, start_pose[1] - ds, start_pose[2], start_pose[3], start_pose[4], start_pose[5]], #3 Move +5 cm on z
    [start_pose[0] - 2*ds, start_pose[1] - 2*ds, start_pose[2], start_pose[3], start_pose[4], start_pose[5]], #3 Move -5 cm on y
    [start_pose[0] - 2*ds, start_pose[1] - 2*ds, start_pose[2]-ds, start_pose[3], start_pose[4], start_pose[5]], #3 Move -5 on z
    [start_pose[0] - 2*ds, start_pose[1] - 2*ds, start_pose[2], start_pose[3], start_pose[4], start_pose[5]], #3 move +5 on z
    [start_pose[0] - 2*ds, start_pose[1] - 3*ds, start_pose[2], start_pose[3], start_pose[4], start_pose[5]], #3 Move -5 cm on y
    [start_pose[0] - 2*ds, start_pose[1] - 3*ds, start_pose[2]-ds, start_pose[3], start_pose[4], start_pose[5]], #3 Move -5 on z
    [start_pose[0] - 2*ds, start_pose[1] - 3*ds, start_pose[2], start_pose[3], start_pose[4], start_pose[5]], #3 move +5 on z	: #4 begins with x position

    [start_pose[0] - 3*ds, start_pose[1] - 3*ds, start_pose[2], start_pose[3], start_pose[4], start_pose[5]], #4 move to X for next cycle
    [start_pose[0] - 3*ds, start_pose[1] - 3*ds, start_pose[2] - ds, start_pose[3], start_pose[4], start_pose[5]], #4 Move -5 cm along the z
    [start_pose[0] - 3*ds, start_pose[1] - 3*ds, start_pose[2] , start_pose[3], start_pose[4], start_pose[5]], #4 Move +5 cm along the z
    [start_pose[0] - 3*ds, start_pose[1] - 2*ds, start_pose[2] , start_pose[3], start_pose[4], start_pose[5]], #4 Move left on y
    [start_pose[0] - 3*ds, start_pose[1] - 2*ds, start_pose[2] - ds, start_pose[3], start_pose[4], start_pose[5]], #4 Move -5 cm along the z
    [start_pose[0] - 3*ds, start_pose[1] - 2*ds, start_pose[2] , start_pose[3], start_pose[4], start_pose[5]], #4 Move +5 cm along the z
    [start_pose[0] - 3*ds, start_pose[1] - ds, start_pose[2] , start_pose[3], start_pose[4], start_pose[5]], #4 Move left on y
    [start_pose[0] - 3*ds, start_pose[1] - ds, start_pose[2] - ds , start_pose[3], start_pose[4], start_pose[5]], #4 Move -5 cm along the z
    [start_pose[0] - 3*ds, start_pose[1] - ds, start_pose[2] , start_pose[3], start_pose[4], start_pose[5]], #4 move +5 cm on z
    [start_pose[0] - 3*ds, start_pose[1] , start_pose[2] , start_pose[3], start_pose[4], start_pose[5]], #4 move left on y
    [start_pose[0] - 3*ds, start_pose[1] , start_pose[2] - ds , start_pose[3], start_pose[4], start_pose[5]], #4 move -5 cm on z
    [start_pose[0] - 3*ds, start_pose[1] , start_pose[2] , start_pose[3], start_pose[4], start_pose[5]] #4 move +5 cm on z : #5 begins with change in X

]
#cycles 5 and 6
trajectory3 = [
    [start_pose[0] - 4*ds, start_pose[1], start_pose[2], start_pose[3], start_pose[4], start_pose[5]], #5 move to X for next cycle
    [start_pose[0] - 4*ds, start_pose[1], start_pose[2]- ds, start_pose[3], start_pose[4], start_pose[5]],  #5 Move -5 cm along the z
    [start_pose[0] - 4*ds, start_pose[1], start_pose[2], start_pose[3], start_pose[4], start_pose[5]],  #5 Move +5 cm on z
    [start_pose[0] - 4*ds, start_pose[1] - ds, start_pose[2], start_pose[3], start_pose[4], start_pose[5]],  #5 Move right in y
    [start_pose[0] - 4*ds, start_pose[1] - ds, start_pose[2]-ds, start_pose[3], start_pose[4], start_pose[5]], #5 Move -5 cm along the z
    [start_pose[0] - 4*ds, start_pose[1] - ds, start_pose[2], start_pose[3], start_pose[4], start_pose[5]], #5 Move +5 cm on z
    [start_pose[0] - 4*ds, start_pose[1] - 2*ds, start_pose[2], start_pose[3], start_pose[4], start_pose[5]], #5 Move -5 cm on y
    [start_pose[0] - 4*ds, start_pose[1] - 2*ds, start_pose[2]-ds, start_pose[3], start_pose[4], start_pose[5]], #5 Move -5 on z
    [start_pose[0] - 4*ds, start_pose[1] - 2*ds, start_pose[2], start_pose[3], start_pose[4], start_pose[5]], #5 move +5 on z
    [start_pose[0] - 4*ds, start_pose[1] - 3*ds, start_pose[2], start_pose[3], start_pose[4], start_pose[5]], #5 Move -5 cm on y
    [start_pose[0] - 4*ds, start_pose[1] - 3*ds, start_pose[2]-ds, start_pose[3], start_pose[4], start_pose[5]], #5 Move -5 on z
    [start_pose[0] - 4*ds, start_pose[1] - 3*ds, start_pose[2], start_pose[3], start_pose[4], start_pose[5]], #5 move +5 on z	: #6 begins with x position

    [start_pose[0] - 5*ds, start_pose[1] - 3*ds, start_pose[2], start_pose[3], start_pose[4], start_pose[5]], #6 move to X for next cycle
    [start_pose[0] - 5*ds, start_pose[1] - 3*ds, start_pose[2] - ds, start_pose[3], start_pose[4], start_pose[5]], #6 Move -5 cm along the z
    [start_pose[0] - 5*ds, start_pose[1] - 3*ds, start_pose[2] , start_pose[3], start_pose[4], start_pose[5]], #6 Move +5 cm along the z
    [start_pose[0] - 5*ds, start_pose[1] - 2*ds, start_pose[2] , start_pose[3], start_pose[4], start_pose[5]], #6 Move left on y
    [start_pose[0] - 5*ds, start_pose[1] - 2*ds, start_pose[2] - ds, start_pose[3], start_pose[4], start_pose[5]], #6 Move -5 cm along the z
    [start_pose[0] - 5*ds, start_pose[1] - 2*ds, start_pose[2] , start_pose[3], start_pose[4], start_pose[5]], #6 Move +5 cm along the z
    [start_pose[0] - 5*ds, start_pose[1] - ds, start_pose[2] , start_pose[3], start_pose[4], start_pose[5]], #6 Move left on y
    [start_pose[0] - 5*ds, start_pose[1] - ds, start_pose[2] - ds , start_pose[3], start_pose[4], start_pose[5]], #6 Move -5 cm along the z
    [start_pose[0] - 5*ds, start_pose[1] - ds, start_pose[2] , start_pose[3], start_pose[4], start_pose[5]], #6 move +5 cm on z
    [start_pose[0] - 5*ds, start_pose[1] , start_pose[2] , start_pose[3], start_pose[4], start_pose[5]], #6 move left on y
    [start_pose[0] - 5*ds, start_pose[1] , start_pose[2] - ds , start_pose[3], start_pose[4], start_pose[5]], #6 move -5 cm on z
    [start_pose[0] - 5*ds, start_pose[1] , start_pose[2] , start_pose[3], start_pose[4], start_pose[5]] #6 move +5 cm on z

]
# x=2
# #trial trajectory
# trajectory_t = [
#     [start_pose[0] - x*ds, start_pose[1], start_pose[2], start_pose[3], start_pose[4], start_pose[5]], #5 move to X for next cycle
#     [start_pose[0] - x*ds, start_pose[1], start_pose[2]- ds, start_pose[3], start_pose[4], start_pose[5]],  #5 Move -5 cm along the z
#     [start_pose[0] - x*ds, start_pose[1], start_pose[2], start_pose[3], start_pose[4], start_pose[5]],  #5 Move +5 cm on z
#     [start_pose[0] - x*ds, start_pose[1] - ds, start_pose[2], start_pose[3], start_pose[4], start_pose[5]],  #5 Move right in y
#     [start_pose[0] - x*ds, start_pose[1] - ds, start_pose[2]-ds, start_pose[3], start_pose[4], start_pose[5]], #5 Move -5 cm along the z
#     [start_pose[0] - x*ds, start_pose[1] - ds, start_pose[2], start_pose[3], start_pose[4], start_pose[5]], #5 Move +5 cm on z
#     [start_pose[0] - x*ds, start_pose[1] - 2*ds, start_pose[2], start_pose[3], start_pose[4], start_pose[5]], #5 Move -5 cm on y
#     [start_pose[0] - x*ds, start_pose[1] - 2*ds, start_pose[2]-ds, start_pose[3], start_pose[4], start_pose[5]], #5 Move -5 on z
#     [start_pose[0] - x*ds, start_pose[1] - 2*ds, start_pose[2], start_pose[3], start_pose[4], start_pose[5]], #5 move +5 on z
#     [start_pose[0] - x*ds, start_pose[1] - 3*ds, start_pose[2], start_pose[3], start_pose[4], start_pose[5]], #5 Move -5 cm on y
#     [start_pose[0] - x*ds, start_pose[1] - 3*ds, start_pose[2]-ds, start_pose[3], start_pose[4], start_pose[5]], #5 Move -5 on z
#     [start_pose[0] - x*ds, start_pose[1] - 3*ds, start_pose[2], start_pose[3], start_pose[4], start_pose[5]], #5 move +5 on z	: #6 begins with x position
#
#     [start_pose[0] - (x+1)*ds, start_pose[1] - 3*ds, start_pose[2], start_pose[3], start_pose[4], start_pose[5]], #6 move to X for next cycle
#     [start_pose[0] - (x+1)*ds, start_pose[1] - 3*ds, start_pose[2] - ds, start_pose[3], start_pose[4], start_pose[5]], #6 Move -5 cm along the z
#     [start_pose[0] - (x+1)*ds, start_pose[1] - 3*ds, start_pose[2] , start_pose[3], start_pose[4], start_pose[5]], #6 Move +5 cm along the z
#     [start_pose[0] - (x+1)*ds, start_pose[1] - 2*ds, start_pose[2] , start_pose[3], start_pose[4], start_pose[5]], #6 Move left on y
#     [start_pose[0] - (x+1)*ds, start_pose[1] - 2*ds, start_pose[2] - ds, start_pose[3], start_pose[4], start_pose[5]], #6 Move -5 cm along the z
#     [start_pose[0] - (x+1)*ds, start_pose[1] - 2*ds, start_pose[2] , start_pose[3], start_pose[4], start_pose[5]], #6 Move +5 cm along the z
#     [start_pose[0] - (x+1)*ds, start_pose[1] - ds, start_pose[2] , start_pose[3], start_pose[4], start_pose[5]], #6 Move left on y
#     [start_pose[0] - (x+1)*ds, start_pose[1] - ds, start_pose[2] - ds , start_pose[3], start_pose[4], start_pose[5]], #6 Move -5 cm along the z
#     [start_pose[0] - (x+1)*ds, start_pose[1] - ds, start_pose[2] , start_pose[3], start_pose[4], start_pose[5]], #6 move +5 cm on z
#     [start_pose[0] - (x+1)*ds, start_pose[1] , start_pose[2] , start_pose[3], start_pose[4], start_pose[5]], #6 move left on y
#     [start_pose[0] - (x+1)*ds, start_pose[1] , start_pose[2] - ds , start_pose[3], start_pose[4], start_pose[5]], #6 move -5 cm on z
#     [start_pose[0] - (x+1)*ds, start_pose[1] , start_pose[2] , start_pose[3], start_pose[4], start_pose[5]] #6 move +5 cm on z
#
# ]
def move_along_trajectory(trajectory, acceleration=0.05, velocity=0.2): # for the first cycle only
    for pose in trajectory:
        rtde_c.moveL(pose, acceleration, velocity)
        time.sleep(1)  # Wait for 1 second at each pose (optional, for demonstration purposes)
        print(pose)

def move_along_trajectory_t(x,ds,acceleration=0.05, velocity=0.2): # for subsequent cycles
    trajectory_t = [
        [start_pose[0] - x * ds, start_pose[1], start_pose[2], start_pose[3], start_pose[4], start_pose[5]],
        # 5 move to X for next cycle
        [start_pose[0] - x * ds, start_pose[1], start_pose[2] - ds, start_pose[3], start_pose[4], start_pose[5]],
        # 5 Move -5 cm along the z
        [start_pose[0] - x * ds, start_pose[1], start_pose[2], start_pose[3], start_pose[4], start_pose[5]],
        # 5 Move +5 cm on z
        [start_pose[0] - x * ds, start_pose[1] - ds, start_pose[2], start_pose[3], start_pose[4], start_pose[5]],
        # 5 Move right in y
        [start_pose[0] - x * ds, start_pose[1] - ds, start_pose[2] - ds, start_pose[3], start_pose[4], start_pose[5]],
        # 5 Move -5 cm along the z
        [start_pose[0] - x * ds, start_pose[1] - ds, start_pose[2], start_pose[3], start_pose[4], start_pose[5]],
        # 5 Move +5 cm on z
        [start_pose[0] - x * ds, start_pose[1] - 2 * ds, start_pose[2], start_pose[3], start_pose[4], start_pose[5]],
        # 5 Move -5 cm on y
        [start_pose[0] - x * ds, start_pose[1] - 2 * ds, start_pose[2] - ds, start_pose[3], start_pose[4],
         start_pose[5]],  # 5 Move -5 on z
        [start_pose[0] - x * ds, start_pose[1] - 2 * ds, start_pose[2], start_pose[3], start_pose[4], start_pose[5]],
        # 5 move +5 on z
        [start_pose[0] - x * ds, start_pose[1] - 3 * ds, start_pose[2], start_pose[3], start_pose[4], start_pose[5]],
        # 5 Move -5 cm on y
        [start_pose[0] - x * ds, start_pose[1] - 3 * ds, start_pose[2] - ds, start_pose[3], start_pose[4],
         start_pose[5]],  # 5 Move -5 on z
        [start_pose[0] - x * ds, start_pose[1] - 3 * ds, start_pose[2], start_pose[3], start_pose[4], start_pose[5]],
        # 5 move +5 on z	: #6 begins with x position

        [start_pose[0] - (x + 1) * ds, start_pose[1] - 3 * ds, start_pose[2], start_pose[3], start_pose[4],
         start_pose[5]],  # 6 move to X for next cycle
        [start_pose[0] - (x + 1) * ds, start_pose[1] - 3 * ds, start_pose[2] - ds, start_pose[3], start_pose[4],
         start_pose[5]],  # 6 Move -5 cm along the z
        [start_pose[0] - (x + 1) * ds, start_pose[1] - 3 * ds, start_pose[2], start_pose[3], start_pose[4],
         start_pose[5]],  # 6 Move +5 cm along the z
        [start_pose[0] - (x + 1) * ds, start_pose[1] - 2 * ds, start_pose[2], start_pose[3], start_pose[4],
         start_pose[5]],  # 6 Move left on y
        [start_pose[0] - (x + 1) * ds, start_pose[1] - 2 * ds, start_pose[2] - ds, start_pose[3], start_pose[4],
         start_pose[5]],  # 6 Move -5 cm along the z
        [start_pose[0] - (x + 1) * ds, start_pose[1] - 2 * ds, start_pose[2], start_pose[3], start_pose[4],
         start_pose[5]],  # 6 Move +5 cm along the z
        [start_pose[0] - (x + 1) * ds, start_pose[1] - ds, start_pose[2], start_pose[3], start_pose[4], start_pose[5]],
        # 6 Move left on y
        [start_pose[0] - (x + 1) * ds, start_pose[1] - ds, start_pose[2] - ds, start_pose[3], start_pose[4],
         start_pose[5]],  # 6 Move -5 cm along the z
        [start_pose[0] - (x + 1) * ds, start_pose[1] - ds, start_pose[2], start_pose[3], start_pose[4], start_pose[5]],
        # 6 move +5 cm on z
        [start_pose[0] - (x + 1) * ds, start_pose[1], start_pose[2], start_pose[3], start_pose[4], start_pose[5]],
        # 6 move left on y
        [start_pose[0] - (x + 1) * ds, start_pose[1], start_pose[2] - ds, start_pose[3], start_pose[4], start_pose[5]],
        # 6 move -5 cm on z
        [start_pose[0] - (x + 1) * ds, start_pose[1], start_pose[2], start_pose[3], start_pose[4], start_pose[5]]
        # 6 move +5 cm on z

    ]
    for pose in trajectory_t:
        rtde_c.moveL(pose, acceleration, velocity)
        time.sleep(1)  # Wait for 1 second at each pose (optional, for demonstration purposes)
        print(pose)

# Move the robot along the defined trajectory
move_along_trajectory(trajectory1)
time.sleep(1)
count = 1
print ('cycle = ',count,' ,x=', 0)
x=6.6
move_along_trajectory_t(x,ds)
count = count + 1
print ('cycle = ',count,' ,x=', x)
time.sleep(1)

#next cycle
# x=x+2
# move_along_trajectory_t(x,ds)
# count = count + 1
# print ('cycle = ',count,' ,x=', x)
# time.sleep(1)
#
# #next cycle
# x=x+2
# move_along_trajectory_t(x,ds)
# count = count + 1
# print ('cycle = ',count,' ,x=', x)
# time.sleep(1)
# # move_along_trajectory(trajectory3)

rtde_c.moveL(initial_pose,0.05, 0.2)
print('initial pose =', initial_pose)
# Disconnect from the robot
rtde_c.disconnect()
rtde_r.disconnect()
