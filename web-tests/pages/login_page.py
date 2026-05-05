from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    URL = "https://www.saucedemo.com/"

    _USERNAME_INPUT = (By.ID, "user-name")
    _PASSWORD_INPUT = (By.ID, "password")
    _LOGIN_BUTTON = (By.ID, "login-button")
    _ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    def open(self):
        self.driver.get(self.URL)

    def login(self, username: str, password: str):
        self._type(self._USERNAME_INPUT, username)
        self._type(self._PASSWORD_INPUT, password)
        self._click(self._LOGIN_BUTTON)

    def get_error_message(self) -> str:
        return self._find(self._ERROR_MESSAGE).text
