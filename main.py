import os

from source.audio_config import audio_config
from source.audio_splitter import split_into_chunks, export_section
from source.timestamp import Timestamp
from source.util import configure_ffmpeg


if __name__ == "__main__":
    configure_ffmpeg() 

    filename = os.path.join(audio_config.input_dir, "example_podcast.mp3")


    # split_length = 20
    # split_into_chunks(filename, split_length)   


    start_time = Timestamp(0, 30, 0)
    end_time = Timestamp(1, 0, 0)
    export_section(filename, start_time, end_time)