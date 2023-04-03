import asyncio
import websockets
import subprocess
import movement
import video
import cv2
import threading
from obstacleAvoidance import ObstacleAvoidance
from hcsr04 import Hcsr04
from autoMoveWithObstacle import AutoMoveWithObstacle
from circular import CircularMovement


class FfmpegRtmp:
    def __init__(self, url, v):
        self.url = url
        self.video = v
        width = int(self.video.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(self.video.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = int(self.video.cap.get(cv2.CAP_PROP_FPS))
        command = ['ffmpeg',
                   '-y', '-an',
                   '-fflags', 'nobuffer',
                   '-fflags', ' flush_packets',
                   '-f', 'rawvideo',
                   '-vcodec', 'rawvideo',
                   '-r', '10',
                   '-pix_fmt', 'bgr24',
                   '-s', "{}x{}".format(width, height),
                   '-i', '-',
                   '-c:v', 'libx264',
                   '-pix_fmt', 'yuv420p',
                   '-vf', 'fps=fps=10',
                   '-preset', 'ultrafast',
                   '-tune', 'zerolatency',
                   '-max_delay', '10',
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
        self.hcsr = Hcsr04()
        self.obstacle_avoidance = ObstacleAvoidance(self.move)
        self.auto_move = AutoMoveWithObstacle(self.obstacle_avoidance)
        self.circular = CircularMovement(self.obstacle_avoidance)


    async def __recv_and_exec(self, websocket):
        async for msg in websocket:
                  msg_list = msg.split(':')
                  msg_list = [float(i) for i in msg_list]
                  reply = str(self.hcsr.get_distance())
                  if len(msg_list) == 4:
                      self.move.set_speed(msg_list[:4])
                  elif msg_list[0] == 0:
                      if msg_list[1] == 1:
                          threading.Thread(target=self.obstacle_avoidance.start).start()
                      else:
                         self.obstacle_avoidance.stop()
                  elif msg_list[0] == 1:
                      if msg_list[1] == 1:
                        threading.Thread(target = self.auto_move.start).start()
                      else:
                        self.auto_move.stop()
                  elif msg_list[0] == 2:
                      if msg_list[1] == 1:
                        threading.Thread(target = self.circular.start, args=('bend',)).start()
                      else:
                        threading.Thread(target = self.circular.start, args=('axle',)).start()

                  print(msg)
                  await websocket.send(reply)

    async def start(self):
        async with websockets.serve(self.__recv_and_exec, self.host, self.port):
            await asyncio.Future()

