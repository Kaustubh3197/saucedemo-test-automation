from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage


def test_full_checkout(driver):
    LoginPage(driver).login("standard_user")
    inventory = InventoryPage(driver)
    inventory.add_to_cart("Sauce Labs Backpack")
    inventory.open_cart()

    checkout = CheckoutPage(driver)
    checkout.start_checkout()
    checkout.fill_details("Kaustubh", "Patil", "411001")
    checkout.finish()

    assert checkout.confirmation() == "Thank you for your order!"
