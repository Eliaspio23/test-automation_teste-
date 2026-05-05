from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ProductsPage(BasePage):
    _PAGE_TITLE = (By.CLASS_NAME, "title")
    _CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    _CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    _ADD_BACKPACK = (By.CSS_SELECTOR, "[data-test='add-to-cart-sauce-labs-backpack']")
    _ADD_BIKE_LIGHT = (By.CSS_SELECTOR, "[data-test='add-to-cart-sauce-labs-bike-light']")

    def is_loaded(self) -> bool:
        return self._find(self._PAGE_TITLE).text == "Products"

    def add_backpack(self):
        self._click(self._ADD_BACKPACK)

    def add_bike_light(self):
        self._click(self._ADD_BIKE_LIGHT)

    def get_cart_count(self) -> str:
        return self._find(self._CART_BADGE).text

    def go_to_cart(self):
        self._click(self._CART_LINK)
