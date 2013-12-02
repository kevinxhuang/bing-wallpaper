#!/usr/bin/env python3

import logging
import os

class Logger(object):

    def __init__(self, logger_name, log_file=None, log_level=logging.INFO):

        self._logger = logging.getLogger(logger_name)

        log_format = logging.Formatter('[%(asctime)s - %(levelname)s - %(module)s] %(message)s')
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(log_format)
        self._logger.addHandler(stream_handler)

        if not log_file is None:

            file_handler = logging.FileHandler(os.path.join(os.path.dirname(__file__), log_file), 'a', 'utf-8')
            self._logger.addHandler(file_handler)
            file_handler.setFormatter(log_format)

        self._logger.setLevel(log_level)

    def set_log_level(self, log_level):

        if str(log_level).upper() == 'CRITICAL':
            self._logger.setLevel(logging.CRITICAL)
        elif str(log_level).upper() == 'ERROR':
            self._logger.setLevel(logging.ERROR)
        elif str(log_level).upper() == 'WARNING':
            self._logger.setLevel(logging.WARNING)
        elif str(log_level).upper() == 'INFO':
            self._logger.setLevel(logging.INFO)
        elif str(log_level).upper() == 'DEBUG':
            self._logger.setLevel(logging.DEBUG)
        else:
            raise ('No such log level: ', log_level)

    def critical(self, msg, *args, **kwargs):
        self._logger.critical(msg, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        self._logger.error(msg, *args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        self._logger.warning(msg, *args, **kwargs)

    def info(self, msg, *args, **kwargs):
        self._logger.info(msg, *args, **kwargs)

    def debug(self, msg, *args, **kwargs):
        self._logger.debug(msg, *args, **kwargs)


