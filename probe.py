# TODO: estimate percieved video quality based on Bittrate Ladder

import subprocess
import json

def probe_video(path):
    cmd = [
        "ffprobe",
        "-v", "error",
        "-select_streams", "v:0",
        "-show_entries", "stream=width,height,r_frame_rate,codec_name",
        "-of", "json",
        str(path)
    ]

    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        check=True
    )

    data = json.loads(result.stdout)
    stream = data["streams"][0]

    return {
        "width": stream["width"],
        "height": stream["height"],
        "fps": eval(stream["r_frame_rate"]),
        "codec": stream["codec_name"],
    }
