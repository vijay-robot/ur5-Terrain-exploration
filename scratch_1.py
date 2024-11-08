import rtde_receive
import rtde_control
rtde_r = rtde_receive.RTDEReceiveInterface("127.0.0.1")
actual_q = rtde_r.getActualQ()