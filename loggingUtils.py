import logging
import sys
import os
from logging.handlers import TimedRotatingFileHandler

FORMATTER = logging.Formatter("%(asctime)s | %(filename)s[line:%(lineno)d] | %(name)s | %(levelname)s | %(message)s")
LOG_FILE = os.path.join("logs", "app.log")

def get_console_handler():
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(FORMATTER)
    return console_handler

def get_file_handler():
    file_handler = TimedRotatingFileHandler(LOG_FILE, when="D", interval=1, backupCount=5)
    file_handler.setFormatter(FORMATTER)
    return file_handler

def get_logger(logger_name):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG) # better to have too much log than not enough
    logger.addHandler(get_console_handler())
    logger.addHandler(get_file_handler())
    logger.propagate = False
    return logger

