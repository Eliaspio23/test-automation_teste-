import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

VALID_USERNAME = "standard_user"
VALID_PASSWORD = "secret_sauce"


def test_login_with_valid_credentials(driver):
    login = LoginPage(driver)
    login.open()
    login.login(VALID_USERNAME, VALID_PASSWORD)

    products = ProductsPage(driver)
    assert products.is_loaded(), "Página de produtos não carregou após login"


def test_login_with_invalid_credentials(driver):
    login = LoginPage(driver)
    login.open()
    login.login("invalid_user", "wrong_pass")

    error = login.get_error_message()
    assert "Username and password do not match" in error


def test_add_products_to_cart(driver):
    login = LoginPage(driver)
    login.open()
    login.login(VALID_USERNAME, VALID_PASSWORD)

    products = ProductsPage(driver)
    products.add_backpack()
    products.add_bike_light()

    assert products.get_cart_count() == "2", "Carrinho deve conter 2 itens"


def test_complete_purchase_flow(driver):
    login = LoginPage(driver)
    login.open()
    login.login(VALID_USERNAME, VALID_PASSWORD)

    products = ProductsPage(driver)
    products.add_backpack()
    products.add_bike_light()
    products.go_to_cart()

    cart = CartPage(driver)
    assert cart.get_item_count() == 2, "Carrinho deve exibir 2 produtos"
    cart.proceed_to_checkout()

    checkout = CheckoutPage(driver)
    checkout.fill_shipping_info("Test", "User", "64000-000")
    checkout.finish_purchase()

    confirmation = checkout.get_confirmation_message()
    assert confirmation == "Thank you for your order!"
