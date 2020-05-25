'''
Created on 27-Apr-2020

@author: Lavendra rajput
'''
import json
from actions.login_page import LoginPage
from test_base.page import Page
import pytest



class TestLoginPage():
    
    fileName = "../test_data/Data.json"
    file = open(fileName)
    data = json.load(file)
    page = Page()
    driver = None
    loginPage = None
    
    @pytest.fixture()
    def setUp(self):
        self.driver = self.page.initialization()
        yield
        self.page.quit_session(self.driver)
        
    
    def test_Login(self, setUp):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(self.data["LoginPage"]["userId"], self.data["LoginPage"]["password"])
