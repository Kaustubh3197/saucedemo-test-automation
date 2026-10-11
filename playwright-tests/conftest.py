import pytest
from playwright.sync_api import Page

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage
from pages.product_page import ProductPage

# pytest-playwright already gives every test a fresh `page` (browser tab).
# These fixtures build page objects on top of it.


@pytest.fixture
def login_page(page: Page) -> LoginPage:
    login = LoginPage(page)
    login.goto()
    return login


@pytest.fixture
def inventory(login_page: LoginPage) -> InventoryPage:
    """A logged-in user on the products page."""
    login_page.login("standard_user")
    return InventoryPage(login_page.page)


@pytest.fixture
def checkout(inventory: InventoryPage) -> CheckoutPage:
    return CheckoutPage(inventory.page)

@pytest.fixture
def product_page(inventory: InventoryPage) -> ProductPage:
    """Logged-in user, with tools for the product details page."""
    return ProductPage(inventory.page)