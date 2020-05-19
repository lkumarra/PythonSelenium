'''
Created on 27-Apr-2020

@author: Lavendra rajput
'''
from selenium.webdriver.remote.webelement import WebElement


class Utilities:
    
    def click_on_element(self, locator:WebElement):
        """
        Perform click action on the element !
        """
        locator.click();
        
    def enter_text_in_element_with_clear(self, locator:WebElement, text:str):
        """
        Enter text with clear !
        """
        locator.clear();
        locator.send_keys(text)
    
    def enter_text_in_element(self, locator:WebElement, text:str):
        """
        Enter text without clear !
        """
        locator.send_keys(text)
        
    def get_element_text(self, locator:WebElement):
        """
        Return the text of webelement !
        """
        return locator.text;
    
    def get_alert_ext(self):
        """
        Return the alert text and accept !
        """
        alert:Alert = self.driver.switch_to().alert()
        alert.accept
        return alert.alert_text