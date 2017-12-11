from selenium import webdriver
from SourceCodes.BaseUtilities.ElementActions import ElementActions
from SourceCodes.PageLocators.SignInPageLocators import SignInPageLocators


class SignInPage (SignInPageLocators, ElementActions):

    def __init__(self, driver):
        self.driver = driver
#        self.actions = ElementActions(driver)

    def enterUserName(self, uname):
        self.enterText(self._userNameField, uname)

    def enterPassword(self, pwd):
        self.enterText(self._passwordField, pwd)

    def clickSignInButton(self):
        self.clickThis(self._signInButton)
