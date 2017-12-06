from selenium import webdriver


class ElementActions:

    def __init__(self, driver):
        self.driver = driver

    def clickThis(self, locator=""):
        val = locator.split(":")
        if val[0] == 'cssselector':
            element = self.driver.find_element_by_css_selector(val[1])
        elif val[0] == 'xpath':
            element = self.driver.find_element_by_xpath(val[1])
        element.click()

    def enterText(self, locator="", value="testData"):
        val = locator.split(":")
        if val[0] == 'cssselector':
            element = self.driver.find_element_by_css_selector(val[1])
        elif val[0] == 'xpath':
            element = self.driver.find_element_by_xpath(val[1])
        element.send_keys(value)
