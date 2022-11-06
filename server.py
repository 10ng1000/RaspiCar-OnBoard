import asyncio
import websockets
import numpy as np
import subprocess
import wheel
import video
import cv2
import time

class FfmpegRtmp:
    def __init__(self, url, cap):
        self.url = url
        self.cap = cap
        width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = 10
        command = ['ffmpeg',
                   '-y',
                   '-f', 'rawvideo',
                   '-vcodec', 'rawvideo',
                   '-pix_fmt', 'bgr24',
                   '-s', "{}x{}".format(width, height),
                   '-r', str(fps),
                   '-i', '-',
                   '-c:v', 'libx264',
                   '-pix_fmt', 'yuv420p',
                   '-preset', 'ultrafast',
                   '-f', 'flv',
                   '-profile:v', 'baseline',
                   '-level', '1',
                   '-flvflags', 'no_duration_filesize',
                   url]
        self.p = subprocess.Popen(command, shell=False, stdin=subprocess.PIPE)


    def send_frame(self, frame):
        self.p.stdin.write(frame.tobytes())

class ControlServer:
    def __init__(self, host):
        self.host = host
        # self.wheel = wheel.Wheel(1, 2, 3, 4)

    async def __recv_and_exec(self, websocket):
        async for msg in websocket:
            msg_list = msg.split(':')
            # wheel.set_speed(msg_list[:4])
            reply = '成功'
            print(msg)
            await websocket.send(reply)

    async def start(self, port):
        async with websockets.serve(self.__recv_and_exec, self.host, port):
            await asyncio.Future()

if __name__ == '__main__':
    '''host_ = 'localhost'
    port_ = 617
    control_server = ControlServer(host_)
    asyncio.run(control_server.start(port_))'''
    video = video.Video()
    # time.sleep(10)
    ffmpeg_rtmp = FfmpegRtmp('rtmp://192.168.137.144:7777/live', video.cap)
    while True:
        frame = video.get_frame()
        if frame is not None:
            ffmpeg_rtmp.send_frame(frame)
        else:
            print('No frame')

