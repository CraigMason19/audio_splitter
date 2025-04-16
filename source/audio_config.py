import os

from source.config import Config

class AudioConfigManager(Config):
    required_keys = ['ffmpeg_path', 'output_dir']

    def __init__(self, config_path="config.json"):
        super().__init__(config_path)
        self._check_required_keys()
        self._setup_environment()

    def _check_required_keys(self):
        missing = [k for k in self.required_keys if not self._config.get(k)]
        if missing:
            raise ValueError(f"Missing config keys: {', '.join(missing)}")

    def _setup_environment(self):
        os.makedirs(self.output_dir, exist_ok=True)
        os.environ['PATH'] += os.pathsep + self.ffmpeg_path

    @property
    def ffmpeg_path(self):
        return self._config['ffmpeg_path']

    @property
    def output_dir(self):
        return self._config['output_dir']

audio_config = AudioConfigManager()