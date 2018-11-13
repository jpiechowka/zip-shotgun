import logging

LOGGING_FORMAT = '%(asctime) | %(level)8s | %(message)s'
LOGGING_TIME_AND_DATE_FORMAT = '%d %b %Y %a %H:%M:S'


def configure_logging():
    logging.basicConfig(format=LOGGING_FORMAT, datefmt=LOGGING_TIME_AND_DATE_FORMAT, level=logging.INFO)
