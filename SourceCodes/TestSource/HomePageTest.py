from SourceCodes.BaseUtilities.Base import Base
from SourceCodes.PageClasses.HomePage import HomePage
from SourceCodes.PageClasses.SignInPage import SignInPage
import unittest


class HomePageTest (unittest.TestCase):

    def setUp(self):
        self.base = Base()
        self.driver = self.base.getChromeDriver()

    def test_checkCurrentURL(self):
        assert self.driver.current_url == "https://www.ebay.com.au/"

    def test_LoginUser(self):
        home = HomePage(self.driver)
        home.clickSignIn()
        signIn = SignInPage(self.driver)
        signIn.enterUserName("testaubasic")
        signIn.enterPassword("N0wBuy1t!")
        signIn.clickSignInButton()

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
