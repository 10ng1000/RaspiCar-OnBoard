import cv2
import numpy as np
import torch

class Video:
    def __init__(self, camera_id=0):
        cap = cv2.VideoCapture(camera_id)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)
        cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('H', '2', '6', '4'))
        self.cap = cap

    def get_frame(self):
        ret, frame = self.cap.read()
        if ret:
            return frame
        else:
            return None

class Yolo:
    def __init__(self):
        self.model = torch.hub.load('ultralytics/yolov5', 'yolov5-tiny', pretrained=True).autoshape()

    def detect(self, frame):
        results = self.model(frame)
        return results


if __name__ == '__main__':
    video = Video(0)
    while True:
        frame = video.get_frame()
        if frame is not None:
            cv2.imshow('frame', frame)
            cv2.waitKey(1)
        else:
            print('No frame')
            break
