import logging
import os.path
import time

class logger:
    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.NOTSET)
        rq = time.strftime('%Y%m%d', time.localtime(time.time()))
        logPath = os.path.dirname(os.getcwd()) + '/logs/'
        if not os.path.isdir(logPath):
            os.mkdir(logPath)
        logName = logPath + rq + '.log'
        self.fh = logging.FileHandler(logName, mode='w')
        self.fh.setLevel(logging.DEBUG)
        self.logger.addHandler(self.fh)

    def __del__(self):
        self.logger.removeHandler(self.fh)

    def info(self, str):
        self.logger.info(str)

    def debug(self, str):
        self.logger.debug(str)
