#!/usr/bin/env python3 -tu

import os
import logging
from logging.config import dictConfig
from datetime import datetime

class ChessLogger:
    def __init__(self):
        logging_config = dict(
                            version = 1,
                            formatters = { 'f': {'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'} },
                            handlers = {'h': {'class': 'logging.StreamHandler', 'formatter': 'f', 'level': logging.DEBUG} },
                            root = { 'handlers': ['h'], 'level': logging.DEBUG, },)
        dictConfig(logging_config)
        now = datetime.now()
        resultFolder = now.strftime("%d/%m/%Y %H:%M:%S")
        resultFolder = "report"
        os.makedirs(resultFolder)
        self._ReportFile = "{0}/test_report.log".format(resultFolder)
        fileHandle = logging.FileHandler(filename=self._ReportFile)
        stdoutHandle = logging.StreamHandler(sys.stdout)
        stderrHandle = logging.StreamHandler(sys.stderr)
        handlers = [ fileHandle. stdoutHandle. stderrHandle]
        logging.basicConfig(level=logging.DEBUG,
                        format='[%(asctime)s] {%(filename)s:%(lineno)d} %(levelname)s - %(message)s',
                        handlers=handlers
                        )
        self._logger = logging.getLogger("ChessLogger:")
        self._logger.setLevel(logging.DEBUG)
        self._logger.addHandler(handlers)

    def Info(self, msg):
        self._logger.Info(msg)

    def Warn(self, msg):
        self._logger.Warn(msg)

    def Error(self, msg):
        self._logger.error(msg)

    def Debug(self, msg):
        self._logger.debug(msg)
