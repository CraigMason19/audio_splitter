import os

from pathlib import Path
from pydub import AudioSegment

from source.util import ms_to_hms_str, ms_to_timestamp
from source.audio_config import audio_config
from source.timestamp import Timestamp


def load_audio(filename: str):
    if not Path(filename).exists():
        raise FileNotFoundError(f"File '{filename}' not found.")
    
    print(f"Loading file: {filename}")
    audio = AudioSegment.from_mp3(filename)
    print(f"Loaded {filename} successfully. Duration: {ms_to_hms_str(len(audio))}")

    return audio
    

def split_into_chunks(filename: str, chunk_duration: int) -> None:
    """
    Splits a long .mp3 into smaller chunks
    """
    audio = load_audio(filename)

    print(f"Splitting into {chunk_duration} minute chunks...")

    segment_length = chunk_duration * 60 * 1000

    # Split and export
    for i, start in enumerate(range(0, len(audio), segment_length)):
        part = audio[start:start + segment_length]
        output_path = os.path.join(audio_config.output_dir, f"{Path(filename).stem}_part_{i+1}.mp3")
        part.export(output_path, format="mp3")
        print(f"Exported: {output_path}")

    print("Splitting complete!")


def split_on_timestamps(filename: str, timestamps: list[str]) -> None:
    """
    Splits audio from a list of timestamps.
    """
    audio = load_audio(filename)

    print(f"Splitting into {len(timestamps)} parts...")

    stamps = [Timestamp.from_string(ts) for ts in timestamps] + [ms_to_timestamp(len(audio))]

    for i in range(len(stamps)-1):
        start_time = stamps[i]
        end_time = stamps[i+1]

        section = audio[int(start_time.to_timedelta().total_seconds() * 1000) : int(end_time.to_timedelta().total_seconds() * 1000)]

        base_name = Path(filename).stem 
        sanitized_start = str(start_time).replace(":", "-")
        sanitized_end = str(end_time).replace(":", "-")
        output_path = os.path.join(audio_config.output_dir, f"{base_name}_section_{sanitized_start}-{sanitized_end}.mp3")

        section.export(output_path, format="mp3")
        print(f"Exported section: {output_path}")

    print(f"Exported {len(timestamps)} parts")


def export_section(filename: str, start_time: Timestamp, end_time: Timestamp) -> None:
    """
    Extracts a section of an audio file and exports it.
    """
    audio = load_audio(filename)

    print(f"Extracting section from {start_time} to {end_time}...")

    section = audio[int(start_time.to_timedelta().total_seconds() * 1000) : int(end_time.to_timedelta().total_seconds() * 1000)]

    # Generate output filename
    base_name = Path(filename).stem 
    sanitized_start = str(start_time).replace(":", "-")
    sanitized_end = str(end_time).replace(":", "-")
    output_path = os.path.join(audio_config.output_dir, f"{base_name}_section_{sanitized_start}-{sanitized_end}.mp3")

    section.export(output_path, format="mp3")
    print(f"Exported section: {output_path}")