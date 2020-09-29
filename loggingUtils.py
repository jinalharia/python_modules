import logging
import sys
import os
from logging.handlers import TimedRotatingFileHandler

class Logger(object):
    level_relations = {
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'critical': logging.CRITICAL
    }

    def __init__(self, logger_name, level="debug", fmt="%(asctime)s | %(filename)s[line:%(lineno)d] | %(name)s | %(levelname)s | %(message)s",
                 log_file=None, when="D", interval=1, backupCount=5):
        self.FORMATTER = logging.Formatter(fmt)
        self.logger_name = logger_name
        self.level = level

        self.log_file = log_file
        self.when = when
        self.interval = interval
        self.backupCount = backupCount

        # create logger and set the logging level
        self.logger = logging.getLogger(self.logger_name)
        self.logger.setLevel(self.level_relations.get(self.level))

        # create the console handler and add to logger
        self.logger.addHandler(self.get_console_handler())

        # create the file handler if specified and add to logger
        if self.log_file is not None:
            self.logger.addHandler(self.get_file_handler(self.log_file, self.when, self.interval, self.backupCount))

        # with this pattern it is rarely necessary to propogate the error up to the parent
        self.logger.propagate = False

    def get_console_handler(self):
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(self.FORMATTER)
        return console_handler

    def get_file_handler(self, log_file, when, interval, backupCount):
        file_handler = TimedRotatingFileHandler(log_file, when=when, interval=interval, backupCount=backupCount)
        file_handler.setFormatter(self.FORMATTER)
        return file_handler