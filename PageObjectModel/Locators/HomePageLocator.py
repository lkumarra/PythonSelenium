'''
Created on 27-Apr-2020

@author: Lavendra rajput
'''
from seleniumpagefactory.Pagefactory import PageFactory

class HomePageLocators(PageFactory):
    
    def __init__(self,driver):
        # It is necessary to to initialise driver as page class member to implement Page Factory
        self.driver = driver
        
    locators = {
        "welcomeMessage": ('XPATH', "//marquee[@class = 'heading3']"),
        "managerId": ('CSS', "tr.heading3>td:first-child"),
        "newCostumerLink": ('LINK TEXT', 'New Customer'),
        "editCostumerLink": ('LINK TEXT', 'Edit Customer')
     }
    
    def welcomeMessageLocator(self):
        '''Locator of welcome message'''
        return self.welcomeMessage;
    
    def managerIDLocator(self):
        '''Locator of manager Id'''
        return self.managerId;
    
    def newCostumerLinkLocator(self):
        '''Locator of new customer link'''
        return self.newCostumerLink;
    
    def editCostumerLinkLocator(self):
        '''Locator of edit customer link'''
        return self.editCostumerLink;