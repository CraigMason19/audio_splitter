import os

from datetime import timedelta
from pydub import AudioSegment

from source.audio_config import audio_config

def ms_to_hours_minutes(milliseconds):
    td = timedelta(milliseconds=milliseconds)
    hours, remainder = divmod(td.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{hours} hours, {minutes} minutes, {seconds} seconds"

def configure_ffmpeg():
    AudioSegment.converter = os.path.join(audio_config.ffmpeg_path, "ffmpeg.exe")
    AudioSegment.ffprobe = os.path.join(audio_config.ffmpeg_path, "ffprobe.exe")