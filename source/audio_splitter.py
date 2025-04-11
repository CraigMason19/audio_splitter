import os

from pathlib import Path
from datetime import timedelta

from pydub import AudioSegment


OUTPUT_DIR = "output"


def ms_to_hours_minutes(milliseconds):
    td = timedelta(milliseconds=milliseconds)
    hours, remainder = divmod(td.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{hours} hours, {minutes} minutes, {seconds} seconds"


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


def export_section(filename, start_time, end_time):
    """
    Extracts a section of an audio file and exports it.
    """
    if not Path(filename).exists():
        raise FileNotFoundError(f"File '{filename}' not found.")
    
    Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)

    print(f"Loading file: {filename}")
    audio = AudioSegment.from_mp3(filename)
    print(f"Loaded {filename} successfully. Duration: {ms_to_hours_minutes(len(audio))}")

    # Ensure times are within range
    start_time = max(0, start_time)
    end_time = min(len(audio), end_time)

    if start_time >= end_time:
        raise ValueError("Start time must be less than end time.")

    print("Splitting...")
    section = audio[start_time:end_time]
    
    # Generate output filename
    base_name = Path(filename).stem 
    output_path = os.path.join(OUTPUT_DIR, f"{base_name}_section_{start_time}-{end_time}.mp3")

    section.export(output_path, format="mp3")
    print(f"Exported section: {output_path}")