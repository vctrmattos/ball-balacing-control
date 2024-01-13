import numpy as np
import cv2
import serial
import time
from webcam import Webcam
    
port = "/dev/ttyUSB0"
ser = serial.Serial(port, 9600, timeout=1)
time.sleep(2)

cam = Webcam(2)
cam.config_blob_detection()

# pos_plate = cam.get_plate_pos()

#Loop
while True:
    ball_pos = cam.get_ball_pos()
    
    if ball_pos != ():
        # rel_ball_poss = pos_plate - ball_pos
        rel_ball_poss = ball_pos

    else:
        rel_ball_poss = (-1, -1)
    
    ser.write(f'<{rel_ball_poss[0]}, {rel_ball_poss[1]}>'.encode()) #Data sent as '<pos_x, pos_y>'
    print(ball_pos)
    if (cv2.waitKey(1) & 0xFF) == ord('q'):
        break

cam.close()