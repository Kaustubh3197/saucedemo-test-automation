from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_valid_user_can_log_in(driver):
    LoginPage(driver).login("standard_user")
    assert "inventory.html" in driver.current_url
    assert InventoryPage(driver).title() == "Products"


def test_locked_out_user_sees_error(driver):
    page = LoginPage(driver)
    page.login("locked_out_user")
    assert "locked out" in page.error_text()


def test_wrong_password_is_rejected(driver):
    page = LoginPage(driver)
    page.login("standard_user", "wrong_password")
    assert "do not match any user" in page.error_text()
