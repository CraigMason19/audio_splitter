import json
import os
import sys

# Get the absolute path to config.json relative to this file
CONFIG_FILE = os.path.join(os.path.dirname(__file__), "..", "config.json")
CONFIG_FILE = os.path.abspath(CONFIG_FILE)

try:
    with open(CONFIG_FILE, "r") as f:
        _config = json.load(f)

except FileNotFoundError:
    print(f"[ERROR] Config file '{CONFIG_FILE}' not found.")
    sys.exit(1)

except json.JSONDecodeError as e:
    print(f"[ERROR] Failed to parse JSON in '{CONFIG_FILE}': {e}")
    sys.exit(1)

FFMPEG_PATH = _config.get("ffmpeg_path")
OUTPUT_DIR = _config.get("output_dir")

# Fail if required keys are missing
if not FFMPEG_PATH:
    print("[ERROR] 'ffmpeg_path' not found in config.")
    sys.exit(1)

if not OUTPUT_DIR:
    print("[ERROR] 'output_dir' not found in config.")
    sys.exit(1)

os.makedirs(OUTPUT_DIR, exist_ok=True)