from selenium import webdriver


class ElementActions:

    def __init__(self, driver):
        """
        :WebDriver driver: object
        """
        self.driver = driver

    def __findElement(self, locator=''):
        val = locator.split(":")
        if val[0] == 'cssselector':
            element = self.driver.find_element_by_css_selector(val[1])
        elif val[0] == 'xpath':
            element = self.driver.find_element_by_xpath(val[1])
        elif val[0] == 'id':
            element = self.driver.find_element_by_id(val[1])
        elif val[0] == 'name':
            element = self.driver.find_element_by_name(val[1])
        elif val[0] == 'class':
            element = self.driver.find_element_by_class_name(val[1])

        return element

    def clickThis(self, locator=""):
        self.__findElement(locator).click()

    def enterText(self, locator="", value="testData"):
        self.__findElement(locator).send_keys(value)

    def getWebElement(self, locator=""):
        return self.__findElement(locator)
