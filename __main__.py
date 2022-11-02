import logging

class CustomFormatter(logging.Formatter):
    """Logging Formatter to add colors and count warning / errors"""

    grey = "\x1b[38;20m"
    cyan = "\033[96m"
    yellow = "\033[33;21m"
    red = "\033[31;21m"
    bold_red = "\x1b[31;1m"
    reset = "\033[0m"

    time = '%(asctime)s '
    level = '%(levelname)s '
    message = '%(message)s (%(filename)s:%(lineno)d)'

    FORMATS = {
        logging.DEBUG: time + grey + level + reset + "   " + message,
        logging.INFO: time + cyan + level + reset + "    " + message,
        logging.WARNING: time + yellow + level + " " + reset + message,
        logging.ERROR: time + red + level + "   " + reset + message,
        logging.CRITICAL: time + bold_red + level + "" + reset + message
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt, datefmt="%Y-%m-%d %H:%M:%S")
        return formatter.format(record)

LOGGER = logging.getLogger("my_app")
LOGGER.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(CustomFormatter())
LOGGER.addHandler(ch)

LOGGER.debug('1')
LOGGER.info('2')
LOGGER.warning('3')
LOGGER.error('4')
LOGGER.critical('5')