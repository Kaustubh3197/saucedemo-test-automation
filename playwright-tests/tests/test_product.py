import re

import pytest
from playwright.sync_api import expect


# Test 1: run with 3 different products (data-driven)
@pytest.mark.parametrize(
    "name, price",
    [
        ("Sauce Labs Backpack", "$29.99"),
        ("Sauce Labs Bike Light", "$9.99"),
        ("Sauce Labs Fleece Jacket", "$49.99"),
    ],
)
def test_product_page_shows_correct_details(inventory, product_page, name, price):
    # Act
    inventory.open_product(name)

    # Assert
    expect(inventory.page).to_have_url(re.compile(r"inventory-item\.html"))
    expect(product_page.name).to_have_text(name)
    expect(product_page.price).to_have_text(price)
    expect(product_page.description).not_to_be_empty()


# Tests 2 & 3: add, then remove, from the details page
def test_add_and_remove_from_product_page(inventory, product_page):
    inventory.open_product("Sauce Labs Backpack")

    product_page.add_to_cart()
    expect(product_page.cart_badge).to_have_text("1")
    expect(product_page.remove_button).to_be_visible()

    product_page.remove_from_cart()
    expect(product_page.cart_badge).to_have_count(0)
    expect(product_page.add_button).to_be_visible()


# Test 4: back button
def test_back_to_products(inventory, product_page):
    inventory.open_product("Sauce Labs Backpack")

    product_page.back_to_products()

    expect(inventory.title).to_have_text("Products")