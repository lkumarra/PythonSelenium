"""
Created on 28-Apr-2020
@author: Lavendra rajput
"""
import json
from actions.login_page import LoginPage
from test_base.page import Page
import pytest

@pytest.mark.usefixtures("setUp")
class TestHomePage():
    
    fileName = "../test_data/Data.json"
    file = open(fileName)
    data = json.load(file)
    page = Page()
    driver = None
    loginPage = None
    homePage = None

    @pytest.fixture()
    def setUp(self):
        self.driver = self.page.initialization()
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(self.data["LoginPage"]["userId"], self.data["LoginPage"]["password"])
        yield
        self.page.quit_session(self.driver)

    def test_verifyWelcomeMessage(self):
        actual = self.homePage.verify_welcome_message()
        expected = self.data["HomePage"]["welcomeMessage"]
        assert actual == expected, "Wrong Manager Id is displayed"

    def test_verifyManagerId(self):
        actual = self.homePage.verify_manager_id()
        expected = self.data["HomePage"]["customerId"]
        assert actual == expected, "Wrong welcome message is displayed"
