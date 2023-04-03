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
        self.fps = self.cap.get(5)
        self.yolo = None
        self.cap = cap

    def create_yolo(self):
        # self.yolo = torch.hub.load('ultralytics/yolov5', 'yolov5s')
        # self.yolo = torch.load('/home/pi/git/yolov3/yolov3-tiny.pt')
        self.yolo = torch.hub.load('ultralytics/yolov5', 'yolov5s')

    def get_frame_with_yolo(self):
        frame = self.get_frame()
        if frame is None:
            return None
        else:
            frame = self.yolo(frame)
            return frame

    def get_frame(self):
        #抽帧处理
        ret, frame = self.cap.read()
        if not ret :
            return None
        tstep = self.cap.get(1)
        iloop = self.fps / 5
        while iloop:
            self.cap.grab()
            iloop = iloop - 1
            if iloop < 1 or (cv2.waitKey(1) & 0xFF == ord('q')):
                break
        return frame


if __name__ == '__main__':
    video = Video(0)
    while True:
        f = video.get_frame()
        if f is not None:
            cv2.imshow('frame', f)
            cv2.waitKey(1)
        else:
            print('No frame')
            break