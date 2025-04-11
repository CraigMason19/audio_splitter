import os

from pathlib import Path
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