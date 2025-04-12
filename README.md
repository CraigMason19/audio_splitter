# audio_splitter
A python script to split up long podcasts.

Created so I can have a customizable mp3 splitter because I don't like falling asleep and losing track of where I was.

This script allows you to process MP3 audio files by:
1. Splitting a long audio file into smaller chunks of a specified duration.
2. Extracting a specific section of an audio file based on start and end times.

## Requirements
- Python 3.x
- Uses the [pydub](https://github.com/jiaaro/pydub) library for audio processing
- Requires [FFmpeg](https://ffmpeg.org/) to be installed; its path can be set in `config.json`

## Instalation
- Install dependencies with:
```python
pip install -r requirements.txt
```
- Ensure FFmpeg is installed and correctly set in config.json

## Usage:
- Ensure FFmpeg is installed and correctly set in config.json
- Call `split_into_chunks` to split an audio file.
- Call `export_section` to extract a section.

### Splitting an audio file
```python
split_into_chunks("my_podcast.mp3", 20)
```
This will create 20-minute chunks from the original file.

### Extracting a specific section

```python
start_time = timedelta(hours=0, minutes=30, seconds=0)
end_time = timedelta(hours=1, minutes=0, seconds=0)
export_section("my_podcast.mp3", start_time, end_time)
```

## 📁 Output
Exported files will be saved in a directory called `output` next to the `main.py` script (or as set in `config.json`)

Examples:
- output/my_podcast_part_1.mp3
- output/my_podcast_section_0-30-00-1-00-00.mp3