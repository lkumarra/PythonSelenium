'''
Created on 27-Apr-2020

@author: Lavendra rajput
'''
from seleniumpagefactory.Pagefactory import PageFactory

class LoginPageLocators(PageFactory):
    
    def __init__(self,driver):
        # It is necessary to to initialise driver as page class member to implement Page Factory
        self.driver = driver
        
    locators = {
        "userId": ('NAME', 'uid'),
        "password": ('NAME', 'password'),
        "loginButton": ('NAME', 'btnLogin'),
        "resetButton": ('XPATH', 'btnReset')
     }
    
    def userIdLocator(self):
        return self.userId;
    
    def passwordLocator(self):
        return self.password;
    
    def loginButtonLocator(self):
        return self.loginButton;
    
    def resetButtonLocato(self):
        return self.resetButton;
