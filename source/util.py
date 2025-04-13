import os

from datetime import timedelta
from pydub import AudioSegment

from source.config import FFMPEG_PATH

def ms_to_hours_minutes(milliseconds):
    td = timedelta(milliseconds=milliseconds)
    hours, remainder = divmod(td.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{hours} hours, {minutes} minutes, {seconds} seconds"

def configure_ffmpeg():
    os.environ["PATH"] += os.pathsep + FFMPEG_PATH

    AudioSegment.converter =  os.path.join(FFMPEG_PATH, "ffmpeg.exe")
    AudioSegment.ffprobe = os.path.join(FFMPEG_PATH, "ffprobe.exe")