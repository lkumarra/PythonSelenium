'''
Created on 27-Apr-2020

@author: Lavendra rajput
'''
import json
from selenium import webdriver
from TestUtils.LogMananger import LogManager

class Page():
    
    f = open("E:\Python_Workspace\PageObjectModel\Config\Confing.json")
    data = json.load(f)
    log = LogManager() 
    def initialization(self):
        '''Initialize the webdriver'''
        if(self.data["browser"] == "Chrome"):
            driver = webdriver.Chrome("C:\\Users\\Lavendra rajput\\git\\parabank\\qa.guru99bank.automation.com\\src\\main\\java\\com\\guru99Bank\\qa\\drivers\\chromedriver.exe")
            self.log.getLogger().debug("Chrome is launched")
        elif(self.data["browser"] == "firefox"):
            driver = webdriver.Chrome("C:\\Users\\Lavendra rajput\\git\\parabank\\qa.guru99bank.automation.com\\src\\main\\java\\com\\guru99Bank\\qa\\drivers\\chromedriver.exe")
            self.log.getLogger().debug("Firefox is launched")
        driver.get(self.data["url"])
        self.log.getLogger().debug("Enter the url"+self.data["url"])
        driver.maximize_window()
        self.log.getLogger().debug("Maximize the window")
        return driver
    
    def quitSession(self, driver):
        '''
           Quit the Browser
        '''
        driver.quit()
        self.log.getLogger().debug("Quit the session")
