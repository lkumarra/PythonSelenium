'''
Created on 28-Apr-2020

@author: Lavendra rajput
'''
import json
import unittest
from Actions.LoginPage import LoginPage
from TestBase.Page import Page
import HtmlTestRunner


class TestHomePage(unittest.TestCase):
    fileName = "../TestData/Data.json"
    file = open(fileName)
    data = json.load(file)
    page = Page()
    driver = None
    loginPage = None
    homePage = None

    def setUp(self):
        print("setup started")
        self.driver = self.page.initialization()
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.doLogin(self.data["LoginPage"]["userId"], self.data["LoginPage"]["password"])

    def test_verifyWelcomeMessage(self):
        actual = self.homePage.verifyWelcomeMessage()
        expected = self.data["HomePage"]["welcomeMessage"]
        self.assertEqual(actual, expected, "Wrong Manager Id is displayed")

    def test_verifyManagerId(self):
        self.assertEqual(self.homePage.verifyManagerId(), self.data["HomePage"]["customerId"],
                         "Wrong welcome message is displayed")

    def tearDown(self):
        self.page.quitSession(self.driver)


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output=r"../TestReport"))
