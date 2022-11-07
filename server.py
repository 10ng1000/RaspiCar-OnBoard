import asyncio
import websockets
import subprocess
import movement
import video
import cv2


class FfmpegRtmp:
    def __init__(self, url, v):
        self.url = url
        self.video = v
        width = int(self.video.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(self.video.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = int(self.video.cap.get(cv2.CAP_PROP_FPS))
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
        self.p.stdin.write(frame.tostring())

    def start(self):
        while True:
            frame = self.video.get_frame()
            if frame is not None:
                self.send_frame(frame)
            else:
                break


class ControlServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.move = movement.Movement()

    async def __recv_and_exec(self, websocket):
        async for msg in websocket:
                  msg_list = msg.split(':')
                  msg_list = [int(i) for i in msg_list]
                  self.move.set_speed(msg_list[:4])
                  reply = 'ok' + msg
                  print(msg)
                  await websocket.send(reply)

    async def start(self):
        async with websockets.serve(self.__recv_and_exec, self.host, self.port):
            await asyncio.Future()
