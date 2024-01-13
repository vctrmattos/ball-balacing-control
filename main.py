import numpy as np
import cv2
import serial
import time
from webcam import Webcam

#Serial communication setup    
port = "/dev/ttyUSB0"
ser = serial.Serial(port, 9600, timeout=1)
time.sleep(2)

#Webcam setup
cam = Webcam(2)
cam.config_blob_detection_ball()
cam.config_blob_detection_plate()

pos_plate = np.array(cam.get_plate_pos())


SP = np.array([100, 100]) #Setpoint

#Loop
while True:
    ball_pos = cam.get_ball_pos()
    if ball_pos != ():
        ball_pos = np.array(ball_pos)
        rel_ball_poss = ball_pos - pos_plate #Shifts the coord systems to the plate's center
        error = SP - rel_ball_poss
    else:
        error = np.array((-1, -1))    

    ser.write(f'<{error[0]}, {error[1]}>'.encode()) #Data sent as '<error_x, error_y>'
    
    print(ball_pos)
    print(error, '\n')
    if (cv2.waitKey(1) & 0xFF) == ord('q'):
        break

cam.close()