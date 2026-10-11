from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_cart_badge_updates(driver):
    LoginPage(driver).login("standard_user")
    inventory = InventoryPage(driver)

    inventory.add_to_cart("Sauce Labs Backpack")
    assert inventory.cart_count() == "1"

    inventory.add_to_cart("Sauce Labs Bike Light")
    assert inventory.cart_count() == "2"

    inventory.remove_from_cart("Sauce Labs Backpack")
    assert inventory.cart_count() == "1"
