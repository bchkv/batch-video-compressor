import subprocess

BITRATE_LADDER = [
    (720,  "4M"),
    (1080, "6M"),
    (1440, "9M"),
    (2160, "16M"),
]

def choose_bitrate(height):
    for max_h, br in BITRATE_LADDER:
        if height <= max_h:
            return br
    return "20M"

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