import subprocess

BASE_LADDER = [
    (480,  2.0),
    (576,  2.5),
    (720,  3.5),
    (900,  4.5),
    (1080, 6.0),
    (1260, 7.0),
    (1440, 9.0),
    (1620, 11.0),
    (1800, 13.0),
    (2160, 16.0),
]

def choose_bitrate(height, fps=30):
    for max_h, base_mbps in BASE_LADDER:
        if height <= max_h:
            bitrate = base_mbps
            break
    else:
        bitrate = 20.0

    # FPS scaling (gentle, not aggressive)
    if fps > 30:
        bitrate *= 1.25
    if fps > 50:
        bitrate *= 1.4

    return f"{bitrate:.1f}M"

cmd = [
    "ffmpeg",
    "-y",
    "-hide_banner",
    "-fflags", "+genpts",
    "-i", "input.*",
    "-map", "0:v:0",
    "-map", "0:a:0?",
    "-vsync", "cfr",
    "-pix_fmt", "yuv420p",
    "-c:v", "h264_videotoolbox",
    "-b:v", "6M",
    "-maxrate", "7M",
    "-bufsize", "14M",
    "-profile:v", "high",
    "-movflags", "+faststart",
    "-c:a", "aac",
    "-b:a", "160k",
    "-ac", "2",
    "-sn",
    "output.mp4",
]

subprocess.run(cmd, check=True)