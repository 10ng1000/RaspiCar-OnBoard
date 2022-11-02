from video import Video
from server import FfmpegRtmp

if __name__ == "__main__":
    rmtp_url = "rtmp://localhost:1935/live"
    video = Video()
    server = FfmpegRtmp(rmtp_url)
    # 发送视频帧
    while True:
        frame = video.get_frame()
        if frame is not None:
            server.send_frame(frame)

