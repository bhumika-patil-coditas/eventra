import logging
from .config import SETTINGS
from pathlib import Path

class Logger(logging.Logger):

    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.setLevel(SETTINGS.LOG_LEVEL)
        self.propagate = False
        console_handler = ConsoleHandler()
        self.addHandler(console_handler)

        file_handler = CustomFileHandler()
        self.addHandler(file_handler)

class ConsoleHandler(logging.StreamHandler):
    def __init__(self, level: str = SETTINGS.LOG_LEVEL) -> None:
        super().__init__()
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%dT%H:%M:%S",
        )
        self.setFormatter(formatter)
        self.setLevel(level)

class CustomFileHandler(logging.FileHandler):
    def __init__(self):
        log_file_path = Path(SETTINGS.LOG_FILE)
        log_file_path.parent.mkdir(parents=True , exist_ok=True)

        super().__init__(log_file_path, encoding="UTF-8")
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%dT%H:%M:%S",
        )
        self.setFormatter(formatter)
        self.setLevel(logging.INFO)

logging.setLoggerClass(Logger)

LOGGER = logging.getLogger("App_logs")
