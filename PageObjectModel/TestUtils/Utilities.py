'''
Created on 27-Apr-2020

@author: Lavendra rajput
'''
from selenium.webdriver.remote.webelement import WebElement


class Utilities():
    
    def clickOnElement(self, locator:WebElement):
        '''Perform click action on the element'''
        locator.click();
        
    def enterTextInElementWithClear(self, locator:WebElement, text:str):
        '''Enter text with clear'''
        locator.clear();
        locator.send_keys(text)
    
    def enterTextInElement(self, locator:WebElement, text:str):
        '''Enter text without clear'''
        locator.send_keys(text)
        
    def getElementText(self, locator:WebElement):
        '''Return the text of webelement'''
        return locator.text;
    
    def getAlertText(self):
        '''Return the alert text and accept'''
        alert:Alert = self.driver.switch_to().alert()
        alert.accept
        return alert.alert_text
    
    
        
    
        