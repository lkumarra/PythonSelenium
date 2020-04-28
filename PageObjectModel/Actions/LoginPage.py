'''
Created on 27-Apr-2020

@author: Lavendra rajput
'''
from Locators.LoginPageLocators import LoginPageLocators
from TestBase.Page import Page
from TestUtils.Utilities import Utilities
from TestUtils.LogMananger import LogManager
from Actions.HomePage import HomePage


class LoginPage(Page):
    
    util = Utilities()
    log = LogManager()
    def __init__(self, driver):
        self.driver = driver

    def doLogin(self, userName, password):
        '''Do login to login page'''
        self.log.getLogger().debug("DoLogin started")
        loginElements = LoginPageLocators(self.driver)
        self.util.enterTextInElementWithClear(loginElements.userIdLocator(), userName)
        self.log.getLogger().debug("User Name "+userName+" is enterd")
        self.util.enterTextInElementWithClear(loginElements.passwordLocator(), password)
        self.log.getLogger().debug("Password "+password+" is enterd")
        self.util.clickOnElement(loginElements.loginButtonLocator())
        self.log.getLogger().debug("Clicked on submit button")
        return HomePage(self.driver)
