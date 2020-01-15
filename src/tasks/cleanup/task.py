import os
import glob

paths = [
    "./thumbnails/*.png",
    "./video_data/*.mp4",
    "./audio_data/*.mp3",
]

def cleanup(context):
    for path in paths:
        files = glob.glob(path)
        for f in files:
            os.remove(f)
