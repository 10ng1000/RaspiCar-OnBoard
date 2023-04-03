from video import Video
from server import FfmpegRtmp, ControlServer
import threading
import asyncio

if __name__ == "__main__":
    host = "192.168.223.162"
    rtmp_url = "rtmp://{}:7777/live".format(host)
    try:
        video = Video(0)
        rtmp_server = FfmpegRtmp(rtmp_url, video)
        print('Starting rtmp server from:' + rtmp_url)
        control_server = ControlServer(host, 617)
        print('Starting control server from:' + 'ws://' + host + ':617')
        rtmp_thread = threading.Thread(target=rtmp_server.start)
        control_thread = threading.Thread(target=asyncio.run, args=(control_server.start(),))
        rtmp_thread.start()
        control_thread.start()
    except Exception as e:
        print(e)
        exit(1)


