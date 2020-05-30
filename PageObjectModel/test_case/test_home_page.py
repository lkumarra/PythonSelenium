"""
Created on 28-Apr-2020
@author: Lavendra rajput
"""
import json
from actions.login_page import LoginPage
from test_base.test_base import TestBase


class TestHomePage(TestBase):
    
    fileName = "../test_data/Data.json"
    file = open(fileName)
    data = json.load(file)
    driver = None
    loginPage = None
    homePage = None

    def test_verifyWelcomeMessage(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(self.data["LoginPage"]["userId"], self.data["LoginPage"]["password"])
        actual = self.homePage.verify_welcome_message()
        expected = self.data["HomePage"]["welcomeMessage"]
        assert actual == expected, "Wrong Manager Id is displayed"

    def test_verifyManagerId(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(self.data["LoginPage"]["userId"], self.data["LoginPage"]["password"])
        actual = self.homePage.verify_manager_id()
        expected = self.data["HomePage"]["customerId"]
        assert actual == expected, "Wrong welcome message is displayed"
