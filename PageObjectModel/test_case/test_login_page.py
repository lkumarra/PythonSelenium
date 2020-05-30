"""
Created on 27-Apr-2020
@author: Lavendra rajput
"""
import json
from actions.login_page import LoginPage
from test_base.test_base import TestBase


class TestLoginPage(TestBase):
    
    fileName = "../test_data/Data.json"
    file = open(fileName)
    data = json.load(file)
    
    def test_Login(self):
        loginPage = LoginPage(self.driver)
        loginPage.do_login(self.data["LoginPage"]["userId"], self.data["LoginPage"]["password"])
