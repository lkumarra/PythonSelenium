'''
Created on 27-Apr-2020

@author: Lavendra rajput
'''
import inspect
import logging


class LogManager:
    
    def getLogger(self):
        
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('../Logs/Test.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        ch = logging.StreamHandler()
        fileHandler.setFormatter(formatter)
        ch.setFormatter(formatter)
        logger.addHandler(fileHandler) 
        logger.addHandler(ch)  # filehandler object
        logger.setLevel(logging.DEBUG)
        return logger
