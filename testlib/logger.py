#!/usr/bin/env python3 -tu

import sys
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
        today = datetime.now()
        h = '12'
        if today.hour < 12:
            h = '00'
        resultFolder = today.strftime('%Y%m%d')+ h
        if not os.path.exists(resultFolder):
            os.makedirs(resultFolder)
        self._ReportFile = "{0}/test_report.log".format(resultFolder)
        #fileHandle = logging.FileHandler(filename=self._ReportFile)
        stdoutHandle = logging.StreamHandler(sys.stdout)
        stderrHandle = logging.StreamHandler(sys.stderr)
        #handlers = [ fileHandle, stdoutHandle, stderrHandle]
        handlers = [ stdoutHandle, stderrHandle]
        logging.basicConfig(filename=self._ReportFile, filemode='w',
                        format='[%(asctime)s] {%(filename)s:%(lineno)d} %(levelname)s - %(message)s',
                        handlers=handlers
                        )
        self._logger = logging.getLogger("ChessLogger:")
        self._logger.setLevel(logging.DEBUG)
        self._logger.addHandler(handlers)

    def Info(self, msg):
        logging.info(msg)
        #self._logger.info(msg)

    def Warn(self, msg):
        logging.warn(msg)
        #self._logger.warn(msg)

    def Error(self, msg):
        logging.error(msg)
        #self._logger.error(msg)

    def Debug(self, msg):
        logging.debug(msg)
        #self._logger.debug(msg)
