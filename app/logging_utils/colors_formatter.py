import logging

from colorama import Back, Fore


class ColorFormatter(logging.Formatter):
    blue = Fore.BLUE
    cyan = Fore.CYAN
    yellow = Fore.YELLOW
    red = Fore.RED
    fatal = Fore.WHITE + Back.RED
    reset = Fore.RESET + Back.RESET
    format = "%(levelname)s - %(asctime)s - %(name)s - %(message)s"

    FORMATS = {
        logging.DEBUG: blue + format + reset,
        logging.INFO: cyan + format + reset,
        logging.WARNING: yellow + format + reset,
        logging.ERROR: red + format + reset,
        logging.CRITICAL: fatal + format + reset
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)
