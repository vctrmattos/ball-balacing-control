import cv2
import numpy as np


class Webcam:
    def __init__(self, port):
        self.cap = cv2.VideoCapture(port)
        self.win_name = 'Camera Preview'
        cv2.namedWindow(self.win_name, cv2.WINDOW_NORMAL)
                    
    def config_blob_detection_ball(self):
        params = cv2.SimpleBlobDetector_Params() 
        # Set Area filtering parameters 
        params.filterByArea = True
        params.minArea = 100
        # params.maxArea = 1280*720
        
        # Set Circularity filtering parameters 
        params.filterByCircularity = True 
        params.minCircularity = 0.7

        # Set Convexity filtering parameters 
        params.filterByConvexity = True
        params.minConvexity = 0.7
            
        # Set inertia filtering parameters 
        params.filterByInertia = True
        params.minInertiaRatio = 0.01
        
        # Create a detector with the parameters 
        self.detector_ball = cv2.SimpleBlobDetector_create(params) 

    def config_blob_detection_plate(self):
        params = cv2.SimpleBlobDetector_Params() 
        # Set Area filtering parameters 
        params.filterByArea = True
        params.minArea = 100000
        params.maxArea = 1280*720
        
        params.filterByColor = True
        params.blobColor = 255

        # Set Circularity filtering parameters 
        params.filterByCircularity = True
        params.minCircularity = 0.35
        
        # Set Convexity filtering parameters 
        params.filterByConvexity = True
        params.minConvexity = 0.7
            
        # Set inertia filtering parameters 
        params.filterByInertia = True
        params.minInertiaRatio = 0.05
        
        # Create a detector with the parameters 
        self.detector_plate = cv2.SimpleBlobDetector_create(params) 

    def get_plate_pos(self):
        while True: #Waiting for Enter
            has_frame, frame = self.cap.read()
            # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                            
            # Detect blobs 
            keypoints = self.detector_plate.detect(frame) 
            
            # Draw blobs on our image as red circles 
            blank = np.zeros((1, 1))  
            blobs = cv2.drawKeypoints(frame, keypoints, blank, (0, 0, 255), 
                                    cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS) 

            text = "Number of Circular Blobs: " + str(len(keypoints)) 
            cv2.putText(blobs, text, (20, 550), 
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 100, 255), 2) 
            
            # Show blobs 
            cv2.imshow("Plate detection", blobs) 

            if keypoints != () and (cv2.waitKey(1) & 0xFF) == 13:
                plate_pos = keypoints[0].pt
                return plate_pos

    def get_ball_pos(self):
        has_frame, frame = self.cap.read()
        
        if not has_frame:
            return np.array([-1, -1]) #No blob detected
        
        # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                        
        # Detect blobs 
        keypoints = self.detector_ball.detect(frame) 
        
        # Draw blobs on our image as red circles 
        blank = np.zeros((1, 1))  
        blobs = cv2.drawKeypoints(frame, keypoints, blank, (0, 0, 255), 
                                cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS) 

        text = "Number of Circular Blobs: " + str(len(keypoints)) 
        cv2.putText(blobs, text, (20, 550), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 100, 255), 2) 
        
        # Show blobs 
        cv2.imshow("Filtering Circular Blobs Only", blobs) 

        if keypoints != ():
            ball_pos = keypoints[0].pt
        else:
            ball_pos = keypoints

        return ball_pos
        
    def close(self):
        self.cap.release()
        cv2.destroyWindow(self.win_name)