"""
Created on 27-Apr-2020
@author: Lavendra rajput
"""
from selenium import webdriver
from locators.home_page_locator import HomePageLocators
from test_base.page import Page
from test_utils.log_mananger import LogManager
from test_utils.utilities import Utilities

class HomePage(Page):
    
    util = Utilities()
    log = LogManager()
    
    def __init__(self, driver:webdriver):
        self.driver = driver
        self.homePageLocator = HomePageLocators(self.driver)
        
    def verify_welcome_message(self):
        """
        Return the welcome message after login !
        """
        text = self.util.get_element_text(self.homePageLocator.get_welcome_message_locator())
        self.log.getLogger().debug("Welcome message is "+text)
        return text
    
    def verify_manager_id(self):
        """
        Return the manager Id After login !
        """
        text = self.util.get_element_text(self.homePageLocator.get_manager_id_locator())
        self.log.getLogger().debug("Welcome message is "+text)
        return text