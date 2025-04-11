from datetime import timedelta
from source.util import configure_ffmpeg
from source.audio_splitter import split_into_chunks, export_section

FILENAME = "example_podcast.mp3"
   
SPLIT_LENGTH = 20
START_TIME = timedelta(hours=0, minutes=30, seconds=0)
END_TIME = timedelta(hours=2, minutes=0, seconds=0)

if __name__ == "__main__":
    configure_ffmpeg() 

    split_into_chunks(FILENAME, SPLIT_LENGTH)   

    # export_section(FILENAME, int(start_time.total_seconds() * 1000), int(end_time.total_seconds() * 1000))