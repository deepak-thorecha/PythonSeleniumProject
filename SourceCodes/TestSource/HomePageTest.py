from SourceCodes.BaseUtilities.Base import Base
from SourceCodes.PageClasses.HomePage import HomePage
from SourceCodes.PageClasses.SignInPage import SignInPage
import unittest
import pandas as pd
from ddt import ddt, data


#@ddt
class HomePageTest (unittest.TestCase):

    def setUp(self):
        self.base = Base()
        self.driver = self.base.getChromeDriver()

    #@data(pd.DataFrame("/ResourceFiles/ProdUserDetails.xls").iterrows())
    def check_LoginUser(self, test_DATA):
        assert self.driver.current_url == "https://www.ebay.com.au/"
        home = HomePage(self.driver)
        home.clickSignIn()
        signIn = SignInPage(self.driver)
        signIn.enterUserName(test_DATA['ProdUserData.userName'])
        signIn.enterPassword(test_DATA['ProdUserData.password'])
        signIn.clickSignInButton()

    def test_Login(self):
        self.AU_DATA = pd.read_excel("/Users/dthorecha/PycharmProjects/PySeleniumProject/ResourceFiles/ProdUserDetails.xls")
        self.AU_DATA = self.AU_DATA[self.AU_DATA.get('TestObject.TestSite') == 'AU']
        for row in self.AU_DATA.iterrows():
            self.check_LoginUser(row)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
