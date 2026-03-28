import os

from datetime import timedelta
from pydub import AudioSegment

from source.audio_config import audio_config
from source.timestamp import Timestamp

  
def ms_to_hms_str(milliseconds) -> str:
    td = timedelta(milliseconds=milliseconds)
    hours, remainder = divmod(td.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    return f"{hours} hours, {minutes} minutes, {seconds} seconds"

def ms_to_timestamp(milliseconds) -> str:
    td = timedelta(milliseconds=milliseconds)
    hours, remainder = divmod(td.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    return Timestamp(hours, minutes, seconds)

def configure_ffmpeg():
    AudioSegment.converter = os.path.join(audio_config.ffmpeg_path, "ffmpeg.exe")
    AudioSegment.ffprobe = os.path.join(audio_config.ffmpeg_path, "ffprobe.exe")