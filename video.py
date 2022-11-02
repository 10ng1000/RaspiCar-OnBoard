import cv2
import numpy as np

class Video:
    def __init__(self, camera_id=0):
        cap = cv2.VideoCapture(camera_id)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        self.cap = cap

    def get_frame(self):
        ret, frame = self.cap.read()
        if ret:
            return frame
        else:
            return None