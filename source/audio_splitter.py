import os

from pathlib import Path
from datetime import timedelta
from pydub import AudioSegment
from source.util import ms_to_hours_minutes

OUTPUT_DIR = "output"



def split_into_chunks(filename, chunk_duration):
    """
    Splits a long .mp3 into smaller chunks
    """

    if not Path(filename).exists():
        raise FileNotFoundError(f"File '{filename}' not found.")

    Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)

    print(f"Loading file: {filename}")
    audio = AudioSegment.from_mp3(filename)
    print(f"Loaded {filename} successfully. Duration: {ms_to_hours_minutes(len(audio))}")

    segment_length = chunk_duration * 60 * 1000

    # Split and export
    for i, start in enumerate(range(0, len(audio), segment_length)):
        part = audio[start:start + segment_length]
        output_path = os.path.join(OUTPUT_DIR, f"{Path(filename).stem}_part_{i+1}.mp3")
        part.export(output_path, format="mp3")
        print(f"Exported: {output_path}")

    print("Splitting complete!")


def export_section(filename, start_time: timedelta, end_time: timedelta) -> None:
    """
    Extracts a section of an audio file and exports it.
    """
    if not Path(filename).exists():
        raise FileNotFoundError(f"File '{filename}' not found.")
    
    Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)

    print(f"Loading file: {filename}")
    audio = AudioSegment.from_mp3(filename)
    print(f"Loaded {filename} successfully. Duration: {ms_to_hours_minutes(len(audio))}")

    print(f"Extracting section from {start_time} to {end_time}")


    print("Splitting...")
    section = audio[int(start_time.total_seconds() * 1000) : int(end_time.total_seconds() * 1000)]

    # Generate output filename
    base_name = Path(filename).stem 
    sanitized_start = str(start_time).replace(":", "-")
    sanitized_end = str(end_time).replace(":", "-")
    output_path = os.path.join(OUTPUT_DIR, f"{base_name}_section_{sanitized_start}-{sanitized_end}.mp3")

    section.export(output_path, format="mp3")
    print(f"Exported section: {output_path}")