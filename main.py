import os

from pydub import AudioSegment
from source.audio_splitter import OUTPUT_DIR, split_into_chunks, export_section


def configure_ffmpeg():
    os.environ["PATH"] += os.pathsep + "E:/FFmpeg/bin"

    AudioSegment.converter = "E:/FFmpeg/bin/ffmpeg.exe"
    AudioSegment.ffprobe = "E:/FFmpeg/bin/ffprobe.exe"


if __name__ == "__main__":
    configure_ffmpeg()
    
    filename = "07 - Lord Edgware Dies - Part 01.mp3"


    split_into_chunks(filename, 20)   


    # start_time = timedelta(hours=0, minutes=30, seconds=0)
    # end_time = timedelta(hours=2, minutes=0, seconds=0)
    # export_section(filename, int(start_time.total_seconds() * 1000), int(end_time.total_seconds() * 1000))