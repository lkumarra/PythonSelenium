"""
Created on 27-Apr-2020
@author: Lavendra rajput
"""
import json
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from test_utils.log_mananger import LogManager

class Page:
    
    fileName = "../config/Confing.json"
    file = open(fileName)
    data = json.load(file)
    log = LogManager() 
    
    def initialization(self):
        """
        Initialize the webdriver !
        """
        if(self.data["browser"] == "Chrome"):
            driver = webdriver.Chrome(ChromeDriverManager().install())
            self.log.getLogger().debug("Chrome is launched")
        elif(self.data["browser"] == "firefox"):
            driver = webdriver.Chrome(GeckoDriverManager().install())
        self.log.getLogger().debug("Firefox is launched")
        driver.get(self.data["url"])
        self.log.getLogger().debug("Enter the url" + self.data["url"])
        driver.maximize_window()
        self.log.getLogger().debug("Maximize the window")
        return driver
    
    def quit_session(self, driver:webdriver):
        """
           Quit the Browser !
        """
        driver.quit()
        self.log.getLogger().debug("Quit the session")
