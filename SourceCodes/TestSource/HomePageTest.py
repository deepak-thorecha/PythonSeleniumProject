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
        signIn.enterUserName(test_DATA.get('ProdUserData.userName'))
        signIn.enterPassword(test_DATA.get('ProdUserData.password'))
        signIn.clickSignInButton()
        home.clickSignOut()

    def test_Login(self):
        self.AU_DATA = pd.read_excel("/Users/dthorecha/PycharmProjects/PySeleniumProject/ResourceFiles/ProdUserDetails.xls")
        self.AU_DATA = self.AU_DATA[self.AU_DATA.get('TestObject.TestSite') == 'AU']
        self.AU_DATA = self.AU_DATA.get(['ProdUserData.userName', 'ProdUserData.password'])
        for i in range(0, self.AU_DATA.shape[0], 1):
            self.check_LoginUser(self.AU_DATA.loc[i])

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
