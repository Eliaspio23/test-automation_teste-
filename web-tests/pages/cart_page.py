from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):
    _CART_ITEMS = (By.CLASS_NAME, "cart_item")
    _CHECKOUT_BUTTON = (By.ID, "checkout")

    def get_item_count(self) -> int:
        return len(self.driver.find_elements(*self._CART_ITEMS))

    def proceed_to_checkout(self):
        self._click(self._CHECKOUT_BUTTON)
