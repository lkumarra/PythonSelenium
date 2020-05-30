'''
Created on 27-Apr-2020

@author: Lavendra rajput
'''
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement


class Utilities:
    
    def click_on_element(self, element:WebElement):
        """
        Perform click action on the element !
        """
        element.click();
        
    def enter_text_in_element_with_clear(self, element:WebElement, text:str):
        """
        Enter text with clear !
        """
        element.clear();
        element.send_keys(text)
    
    def enter_text_in_element(self, element:WebElement, text:str):
        """
        Enter text without clear !
        """
        element.send_keys(text)
        
    def get_element_text(self, element:WebElement):
        """
        Return the text of webelement !
        """
        return element.text;
    
    def get_alert_text(self):
        """
        Return the alert text and accept !
        """
        alert:Alert = self.driver.switch_to().alert()
        alert.accept
        return alert.alert_text
    
    def press_enter(self, element:WebElement):
        """
        Perfor enter operation on elements.
        """
        element.send_keys(Keys.ENTER)
        
