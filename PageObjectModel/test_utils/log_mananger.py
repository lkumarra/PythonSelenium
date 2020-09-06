'''
Created on 27-Apr-2020

@author: Lavendra rajput
'''
import inspect
import logging
import queue
import sys
  
class LogManager:
    
    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('../logs/Test.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        ch = logging.StreamHandler(sys.stdout)
        fileHandler.setFormatter(formatter)
        ch.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.addHandler(ch)  # filehandler object
        logger.setLevel(logging.DEBUG)
        return logger
