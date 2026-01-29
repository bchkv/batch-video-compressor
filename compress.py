import subprocess

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