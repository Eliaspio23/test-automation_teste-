from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckoutPage(BasePage):
    _FIRST_NAME = (By.ID, "first-name")
    _LAST_NAME = (By.ID, "last-name")
    _ZIP_CODE = (By.ID, "postal-code")
    _CONTINUE_BUTTON = (By.ID, "continue")
    _FINISH_BUTTON = (By.ID, "finish")
    _CONFIRMATION_HEADER = (By.CLASS_NAME, "complete-header")

    def fill_shipping_info(self, first_name: str, last_name: str, zip_code: str):
        self._type(self._FIRST_NAME, first_name)
        self._type(self._LAST_NAME, last_name)
        self._type(self._ZIP_CODE, zip_code)
        self._click(self._CONTINUE_BUTTON)

    def finish_purchase(self):
        self._click(self._FINISH_BUTTON)

    def get_confirmation_message(self) -> str:
        return self._find(self._CONFIRMATION_HEADER).text
