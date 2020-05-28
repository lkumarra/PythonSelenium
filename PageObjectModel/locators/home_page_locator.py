"""
Created on 27-Apr-2020
@author: Lavendra rajput
"""
from seleniumpagefactory.Pagefactory import PageFactory

class HomePageLocators(PageFactory):
    
    def __init__(self,driver):
        # It is necessary to to initialise driver as page class member to implement Page Factory
        self.driver = driver
        
    locators = {
        "welcomeMessage": ('XPATH', "//marquee[@class = 'heading3']"),
        "managerId": ('XPATH', "//td[contains(text(),'Manger Id :')]"),
        "newCostumerLink": ('LINK TEXT', 'New Customer'),
        "editCostumerLink": ('LINK TEXT', 'Edit Customer')
     }
    
    def get_welcome_message_locator(self):
        """
        Return Locator of welcome message !
        """
        return self.welcomeMessage;
    
    def get_manager_id_locator(self):
        """
        Return Locator of manager Id !
        """
        return self.managerId;
    
    def get_new_costumer_link_locator(self):
        """
        Return Locator of new customer link !
        """
        return self.newCostumerLink;
    
    def edit_costumer_link_locator(self):
        """
        Return Locator of edit customer link
        """
        return self.editCostumerLink;