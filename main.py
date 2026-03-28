import os

from source.audio_config import audio_config
from source.audio_splitter import split_into_chunks, export_section
from source.timestamp import Timestamp
from source.util import configure_ffmpeg


FILENAME = os.path.join(audio_config.input_dir, "example_podcast.mp3")
   
SPLIT_LENGTH = 20
START_TIME = Timestamp(0, 30, 0)
END_TIME = Timestamp(1, 0, 0)


if __name__ == "__main__":
    configure_ffmpeg() 

    # split_into_chunks(FILENAME, SPLIT_LENGTH)   

    export_section(FILENAME, START_TIME, END_TIME)