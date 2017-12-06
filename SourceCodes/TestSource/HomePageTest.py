from SourceCodes.BaseUtilities.Base import Base

class HomePageTest:

    def openPage(self):
        base = Base()
        driver = base.getChromeDriver()
        driver.close()

