import logging
import os


LOG_FOLDER = "logs"
LOG_FILE = os.path.join(LOG_FOLDER, "titan.log")


if not os.path.exists(LOG_FOLDER):
    os.makedirs(LOG_FOLDER)


logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)


def log_info(message):
    logging.info(message)


def log_error(message):
    logging.error(message)