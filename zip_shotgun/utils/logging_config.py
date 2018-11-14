import logging

LOGGING_FORMAT = '%(asctime)s | %(levelname)8s | %(message)s'
LOGGING_TIME_AND_DATE_FORMAT = '%d/%b/%Y %a %H:%M:%S %z'


def configure_logging():
    logging.basicConfig(level=logging.INFO, format=LOGGING_FORMAT, datefmt=LOGGING_TIME_AND_DATE_FORMAT)
