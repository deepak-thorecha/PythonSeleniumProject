from selenium import webdriver
from SourceCodes.BaseUtilities.ElementActions import ElementActions
from SourceCodes.PageLocators.SignInPageLocators import SignInPageLocators


class SignInPage (SignInPageLocators):

    def __init__(self, driver):
        self.driver = driver
        self.actions = ElementActions(driver)

    def enterUserName(self, uname):
        self.actions.enterText(SignInPageLocators._userNameField, uname)

    def enterPassword(self, pwd):
        self.actions.enterText(SignInPageLocators._passwordField, pwd)

    def clickSignInButton(self):
        self.actions.clickThis(SignInPageLocators._signInButton)
