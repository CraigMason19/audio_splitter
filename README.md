# 🔊 audio_splitter
A python project to split up long podcasts.

Created so I can have a customizable MP3 splitter because I don't like falling asleep and losing track of where I am in long form audio.

This project allows you to process MP3 audio files by:
1. Splitting a long audio file into smaller chunks of a specified duration.
2. Extracting a specific section of an audio file based on start and end times.
3. Splitting a audio file using timestamps.

## 📋 Requirements
- Python 3.x.
- Uses the [pydub](https://github.com/jiaaro/pydub) library for audio processing.
- Requires [FFmpeg](https://ffmpeg.org/) to be installed; its path can be set in `config.json`.

## 🛠️ Installation
- Install dependencies with:
```python
pip install -r requirements.txt
```
- Ensure FFmpeg is installed and correctly set in `config.json`

## 📝 Usage:

### Splitting into chunks
```python
split_into_chunks("my_podcast.mp3", 20)
```
This will create 20-minute chunks from the original file.

### Extracting a specific section
```python
start_time = Timestamp(0, 30, 0)
end_time = Timestamp(1, 0, 0)
export_section("my_podcast.mp3", start_time, end_time)
```

### Splitting using timestamps
```python
timestamps = [
    "0:00",
    "17:00",
    "21:00",
]

split_on_timestamps("my_podcast.mp3", timestamps)
```

## 📁 Output
Exported files will be saved in a directory called `output` next to the `main.py` script (or as set in `config.json`)

Examples:
- output/my_podcast_part_1.mp3
- output/my_podcast_section_0-30-00-1-00-00.mp3