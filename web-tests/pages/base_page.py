from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self._wait = WebDriverWait(driver, 20)

    def _find(self, locator):
        return self._wait.until(EC.presence_of_element_located(locator))

    def _click(self, locator):
        self._wait.until(EC.element_to_be_clickable(locator)).click()

    def _type(self, locator, text):
        element = self._find(locator)
        element.clear()
        element.send_keys(text)