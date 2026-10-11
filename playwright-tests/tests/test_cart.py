import pytest
from playwright.sync_api import expect


def test_cart_badge_updates(inventory):
    inventory.add_to_cart("Sauce Labs Backpack")
    expect(inventory.cart_badge).to_have_text("1")

    inventory.add_to_cart("Sauce Labs Bike Light")
    expect(inventory.cart_badge).to_have_text("2")

    inventory.remove_from_cart("Sauce Labs Backpack")
    expect(inventory.cart_badge).to_have_text("1")


# One test function, run twice with different data (data-driven testing)
@pytest.mark.parametrize("option, descending", [("lohi", False), ("hilo", True)])
def test_sort_by_price(inventory, option, descending):
    inventory.sort_by(option)
    prices = inventory.prices()
    assert prices == sorted(prices, reverse=descending)


def test_sort_by_name_z_to_a(inventory):
    inventory.sort_by("za")
    names = inventory.names()
    assert names == sorted(names, reverse=True)
