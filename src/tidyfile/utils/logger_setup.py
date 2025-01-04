import logging
import platform
import sys
from rich.logging import RichHandler


class LoggerConfig:
    def __init__(self, log_to_file=True, log_to_console=True):
        self.log_to_file = log_to_file
        self.log_to_console = log_to_console
        self.configure_logger()

    def configure_logger(self):
        log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        log_datefmt = "[%X]"
        handlers = []

        if self.log_to_console:
            console_handler = RichHandler(rich_tracebacks=True)
            console_handler.setLevel(logging.INFO)
            handlers.append(console_handler)

        if self.log_to_file:
            file_handler = logging.FileHandler("app.log")
            file_handler.setLevel(logging.DEBUG)
            handlers.append(file_handler)

        # Clear existing handlers to avoid duplicate logs
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)

        logging.basicConfig(
            level=logging.DEBUG,
            format=log_format,
            datefmt=log_datefmt,
            handlers=handlers,
        )

        self.logger = logging.getLogger("rich_logger")
        self.add_system_info()

    def add_system_info(self):
        system_info = f"""
        OS: {platform.system()}
        Version: {platform.version()}
        Platform: {platform.platform()}
        Filesystem Encoding: {sys.getfilesystemencoding()}
        Python Version: {platform.python_version()}
        """
        self.logger.debug(system_info)

    def get_logger(self):
        return self.logger


# Initialize a global logger instance
logger_config = LoggerConfig(log_to_file=True, log_to_console=True)
logger = logger_config.get_logger()
