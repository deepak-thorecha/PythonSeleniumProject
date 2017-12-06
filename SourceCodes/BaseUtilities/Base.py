import platform

from Root import Root
import os
from selenium import webdriver


class Base:

    def __init__(self):
        root = Root()
        if(platform.system().__contains__("Windows")):
            self.chrome_driver_path = os.path.join(root.ROOT_DIR, "ResourceFiles", "")
            self.ff_driver_path = os.path.join(root.ROOT_DIR, "ResourceFiles", "")
        else:
            self.chrome_driver_path = os.path.join(root.ROOT_DIR, "ResourceFiles", "chromedriverMac")
            self.ff_driver_path = os.path.join(root.ROOT_DIR, "ResourceFiles", "geckodriverMAC")
        self.URL = "https://www.ebay.com.au"

    def setupDriverConfigs(self, d):
        d.maximize_window()
        d.implicitly_wait(15)

    def getChromeDriver(self):
        driver = webdriver.Chrome(self.chrome_driver_path)
        self.setupDriverConfigs(driver)
        driver.get(self.URL)
        return driver

    def getFireFoxDriver(self):
        driver = webdriver.Chrome(self.ff_driver_path)
        self.setupDriverConfigs(driver)
        driver.get(self.URL)
        return driver