import numpy as np
import time
from webcam import *

def move_servos(u):
    pass

SP = np.array([0, 0]).T #SETPOINT

#PID gains for x and y
Kp = np.array([1, 1])
Ki = np.array([1, 1])
Kd = np.array([1, 1])

error_cum = 0
pos_plate = plate_position()
last_time = time.time()
ball_pos_plate = 0
while True: #Chang condition
    
    ball_pos_abs = ball_position()
    pos = pos_plate - ball_pos_abs  #The origin is on the plate center

    e = SP - pos 
    
    actual_time = time.time()
    dt = time.time() - last_time

    error_cum += e
    error_dt = e/dt

    u = Ki*e + Ki*error_cum + Kd*error_dt

    move_servos(u)

    last_time = actual_time