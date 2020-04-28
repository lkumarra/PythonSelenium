'''
Created on 27-Apr-2020

@author: Lavendra rajput
'''
from selenium import webdriver
from Locators.HomePageLocator import HomePageLocators
from TestBase.Page import Page
from TestUtils.LogMananger import LogManager
from TestUtils.Utilities import Utilities

class HomePage(Page):
    
    util = Utilities()
    log = LogManager()
    def __init__(self, driver:webdriver):
        self.driver = driver
        self.homePageLocator = HomePageLocators(self.driver)
        
    def verifyWelcomeMessage(self):
        '''Return the welcome message after login'''
        text = self.util.getElementText(self.homePageLocator.welcomeMessageLocator())
        self.log.getLogger().debug("Welcome message is "+text)
        return text
    
    
    def verifyManagerId(self):
        '''Return the manager Id After login'''
        text = self.util.getElementText(self.homePageLocator.managerIDLocator())
        self.log.getLogger().debug("Welcome message is "+text)
        return text
    
