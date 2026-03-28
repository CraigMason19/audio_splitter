import os

from source.audio_config import audio_config
from source.audio_splitter import split_into_chunks, split_on_timestamps, export_section
from source.timestamp import Timestamp
from source.util import configure_ffmpeg


if __name__ == "__main__":
    configure_ffmpeg() 

    filename = os.path.join(audio_config.input_dir, "example_podcast.mp3")


    # Split into chunks
    # split_length = 20
    # split_into_chunks(filename, split_length)   


    # Extract section
    # start_time = Timestamp(0, 30, 0)
    # end_time = Timestamp(1, 0, 0)
    # export_section(filename, start_time, end_time)


    # Split on timestamps
    timestamps = [
        "0:00",
        "17:00",
        "21:00",
    ]

    split_on_timestamps(filename, timestamps)