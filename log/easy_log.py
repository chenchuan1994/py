# !/usr/bin python3
# -*- coding: UTF-8 -*-

'''
Auth: cc
Date: 2023-5-21
Func: Packageing logging for more earlier using.
'''

import logging
from datetime import datetime
import os
import sys

PATHSPLIT = '/'
if sys.platform == 'win32':
    PATHSPLIT = '\\'


class easyLog(object):
    def __init__(self, log_path=None) -> None:
        """
        @param: log_path, 日志存储路径，会生成一个log文件夹用以存储日志
        """
        self._now: datetime = datetime.now()
        self._logPath = log_path
        self._log = logging.getLogger(__name__)
        self._fmt = logging.Formatter(
            "%(asctime)s - %(module)s - %(levelname)s - %(message)s")
        self._level = 'DEBUG'

    def init_handle(self):
        """
        init file and stream for outputing log to file and terminal
        """
        if self._logPath is not None:
            logFolder = PATHSPLIT.join([self._logPath, 'log'])
            if not os.path.exists(logFolder):
                os.mkdir(logFolder)

            ymdStr = f"{self._now.year:04}-{self._now.month:02}-{self._now.day:02}"
            hmsStr = f"{self._now.hour:02}_{self._now.minute:02}_{self._now.second:02}"

            logFolder = PATHSPLIT.join([logFolder, ymdStr])
            if not os.path.exists(logFolder):
                os.mkdir(logFolder)
            logFile = PATHSPLIT.join([logFolder, hmsStr])
            logFile += '.log'

            fileHandle = logging.FileHandler(
                logFile, mode='a', encoding='utf-8', errors='ignore')
            fileHandle.setLevel(self._level )
            fileHandle.setFormatter(self._fmt)
            self._log.addHandler(fileHandle)

        
        streamHandle = logging.StreamHandler()
        streamHandle.setFormatter(self._fmt)
        streamHandle.setLevel(self._level)
        self._log.addHandler(streamHandle)

    def getLogger(self) -> logging:
        self.init_handle()
        self._log.setLevel(self._level)
        return self._log

if __name__ == "__main__":
    path = '/Users/chuan/Software/ccpy/py/log/test'
    elog = easyLog(path)
    l = elog.getLogger()
    l.info('info')
