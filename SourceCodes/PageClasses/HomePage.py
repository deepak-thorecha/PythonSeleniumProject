from selenium import webdriver
from SourceCodes.PageLocators.HomePageLocators import HomePageLocators
from SourceCodes.BaseUtilities.ElementActions import ElementActions


class HomePage (HomePageLocators, ElementActions):

    def __init__(self, driver):
        self.driver = driver
#        self.actions = ElementActions(driver)

    def clickSignIn(self):
        self.clickThis(self._signInLink)
