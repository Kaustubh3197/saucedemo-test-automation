import pytest
from playwright.sync_api import expect


def test_full_purchase(inventory, checkout):
    inventory.add_to_cart("Sauce Labs Backpack")
    inventory.open_cart()
    checkout.start()
    checkout.fill_details("Kaustubh", "Patil", "411001")
    checkout.finish()
    expect(checkout.complete_header).to_have_text("Thank you for your order!")


def test_order_total_is_item_total_plus_tax(inventory, checkout):
    inventory.add_to_cart("Sauce Labs Backpack")    # $29.99
    inventory.add_to_cart("Sauce Labs Bike Light")  # $9.99
    inventory.open_cart()
    checkout.start()
    checkout.fill_details("Kaustubh", "Patil", "411001")

    item_total = checkout.money(checkout.item_total.text_content())
    tax = checkout.money(checkout.tax.text_content())
    total = checkout.money(checkout.total.text_content())

    assert item_total == pytest.approx(29.99 + 9.99)
    assert total == pytest.approx(item_total + tax)


def test_first_name_is_required(inventory, checkout):
    inventory.add_to_cart("Sauce Labs Backpack")
    inventory.open_cart()
    checkout.start()
    checkout.fill_details("", "Patil", "411001")
    expect(checkout.error).to_contain_text("First Name is required")
