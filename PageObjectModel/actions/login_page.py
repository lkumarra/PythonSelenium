"""
Created on 27-Apr-2020
@author: Lavendra rajput
"""
from locators.login_page_locators import LoginPageLocators
from test_base.page import Page
from test_utils.log_mananger import LogManager
from test_utils.utilities import Utilities
from actions.home_page import HomePage;
from selenium import webdriver

class LoginPage(Page):
    
    util = Utilities()
    log = LogManager()
    
    def __init__(self, driver:webdriver):
        self.driver = driver
        self.loginElements = LoginPageLocators(self.driver)

    def do_login(self, userName, password):
        """
        Do login to login page !
        """
        self.log.getLogger().debug("DoLogin started")
        self.util.enter_text_in_element_with_clear(self.loginElements.get_user_id_locator(), userName)
        self.log.getLogger().debug("User Name "+userName+" is enterd")
        self.util.enter_text_in_element_with_clear(self.loginElements.get_password_locator(), password)
        self.log.getLogger().debug("Password "+password+" is enterd")
        self.util.click_on_element(self.loginElements.get_login_button_locator())
        self.log.getLogger().debug("Clicked on submit button")
        return HomePage(self.driver)
