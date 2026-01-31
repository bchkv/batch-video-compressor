import sys
from pathlib import Path
# from compress import process_file

VIDEO_EXTENSIONS = {
    ".mp4", ".mkv", ".avi", ".mov",
    ".webm", ".flv", ".wmv", ".mpg", ".mpeg"
}

def is_video(path: Path) -> bool:
    return path.suffix.lower() in VIDEO_EXTENSIONS

def collect_videos(root: Path):
    if root.is_file():
        if is_video(root):
            return [root]
        return []

    if root.is_dir():
        return [
            p for p in root.rglob("*")
            if p.is_file() and is_video(p)
        ]

    return []

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <path>")
        sys.exit(1)

    root = Path(sys.argv[1]).expanduser().resolve()

    if not root.exists():
        print(f"Path does not exist: {root}")
        sys.exit(1)

    videos = collect_videos(root)

    if not videos:
        print("No video files found.")
        return

    print(f"Found {len(videos)} video files.")

    for video in videos:
        try:
            print(f"Processing: {video}")
#             process_file(video)
        except Exception as e:
            print(f"Failed: {video}")
            print(f"  {e}")

if __name__ == "__main__":
    main()