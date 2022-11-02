import asyncio
import websocket
import cv2
import numpy as np
import ffmpeg
import wheel


class FfmpegRtmp:
    def __init__(self, url):
        self.url = url
        self.stream = ffmpeg.input('pipe:', format='rawvideo', pix_fmt='bgr24', s='{}x{}'.format(640, 480))
        self.stream = ffmpeg.output(self.stream, self.url, vcodec='libx264', pix_fmt='yuv420p', preset='ultrafast', r=30)
        self.stream = ffmpeg.overwrite_output(self.stream)
        self.stream = ffmpeg.compile(self.stream)

    def send_frame(self, frame):
        self.stream.run_async(pipe_stdin=True, pipe_stdout=False, pipe_stderr=False, input_data=frame.tostring())

class ControlServer:
    def __init__(self, url):
        self.url = url
        self.ws = websocket.WebSocket()
        self.ws.connect(url)
        self.wheel = wheel.Wheel(1, 2, 3, 4)

    async def recv_and_exec(self):
        async for msg in self.ws:
            msg_list = msg.split(':')
            wheel.set_speed(msg_list[:4])
            reply = '成功'
            await self.reply(reply)

    async def reply(self, msg):
        await self.ws.send(msg)

    async def start(self):
        async with self.ws:
            await self.recv_and_exec()

