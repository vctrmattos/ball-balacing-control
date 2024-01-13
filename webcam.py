import cv2
import numpy as np


class Webcam:
    def __init__(self, port):
        self.cap = cv2.VideoCapture(port)
        self.win_name = 'Camera Preview'
        cv2.namedWindow(self.win_name, cv2.WINDOW_NORMAL)

    def get_plate_pos(self):
        while True:
            # Ler o próximo quadro da webcam
            ret, frame = self.cap.read()

            # Converter para escala de cinza
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Aplicar suavização para reduzir ruído
            gray_blurred = cv2.medianBlur(gray, 3)

            # Parâmetros da detecção de círculos
            circles = cv2.HoughCircles(
                gray_blurred,
                cv2.HOUGH_GRADIENT,
                dp=1,
                minDist=720,
                param1=40,
                param2=30,
                minRadius=10,
                maxRadius=40
            )

            # Se círculos forem encontrados, desenhe-os no quadro
            if circles is not None:
                circles = np.uint16(np.around(circles))
                for i in circles[0, :]:
                    cv2.circle(frame, (i[0], i[1]), i[2], (0, 255, 0), 2)

            # Exibir o quadro resultante
            cv2.imshow('Detecção de Círculos na Webcam', frame)

            # Verificar se o usuário pressionou a tecla 'q' para sair
            if cv2.waitKey(1) & 0xFF == ord('q'):
                return circles[0]
            
    def config_blob_detection(self):
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
        self.detector = cv2.SimpleBlobDetector_create(params) 

    def get_ball_pos(self):
        has_frame, frame = self.cap.read()
        
        if not has_frame:
            return np.array([-1, -1]) #No blob detected
        
        # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                        
        # Detect blobs 
        keypoints = self.detector.detect(frame) 
        
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