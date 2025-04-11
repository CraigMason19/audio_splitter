import os

from datetime import timedelta
from pydub import AudioSegment

def ms_to_hours_minutes(milliseconds):
    td = timedelta(milliseconds=milliseconds)
    hours, remainder = divmod(td.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{hours} hours, {minutes} minutes, {seconds} seconds"

def configure_ffmpeg():
    os.environ["PATH"] += os.pathsep + "E:/FFmpeg/bin"

    AudioSegment.converter = "E:/FFmpeg/bin/ffmpeg.exe"
    AudioSegment.ffprobe = "E:/FFmpeg/bin/ffprobe.exe"