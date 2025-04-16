import json
import os

class Config:
    def __init__(self, config_path="config.json"):
        self._config_path = os.path.abspath(config_path)
        self._load_config()

    def _load_config(self):
        if not os.path.isfile(self._config_path):
            raise FileNotFoundError(f"Config file not found: {self._config_path}")
        
        with open(self._config_path, 'r') as f:
            self._config = json.load(f)

    def get(self, key, default=None):
        return self._config.get(key, default)
    
config = Config()