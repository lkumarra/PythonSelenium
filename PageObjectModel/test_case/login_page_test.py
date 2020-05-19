'''
Created on 27-Apr-2020

@author: Lavendra rajput
'''
import json
import unittest
from actions.login_page import LoginPage
from test_base.page import Page
import HtmlTestRunner



class TestLoginPage(unittest.TestCase):
    
    fileName = "../test_data/Data.json"
    file = open(fileName)
    data = json.load(file)
    page = Page()
    driver = None
    loginPage = None

    def setUp(self):
        self.driver = self.page.initialization()
    
    def test_Login(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(self.data["LoginPage"]["userId"], self.data["LoginPage"]["password"])
    
    def tearDown(self):
        self.page.quit_session(self.driver)
        
if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output=r"../test_report"))