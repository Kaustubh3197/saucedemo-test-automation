from playwright.sync_api import Page


class ProductPage:
    """The details page that opens when you click a product's name."""

    def __init__(self, page: Page):
        self.page = page
        # Things on the page (selectors from Step 2)
        self.name = page.locator(".inventory_details_name")
        self.price = page.locator(".inventory_details_price")
        self.description = page.locator(".inventory_details_desc")
        self.add_button = page.locator("[data-test='add-to-cart']")
        self.remove_button = page.locator("[data-test='remove']")
        self.back_button = page.locator("[data-test='back-to-products']")
        self.cart_badge = page.locator(".shopping_cart_badge")

    # Things you can do on the page
    def add_to_cart(self):
        self.add_button.click()

    def remove_from_cart(self):
        self.remove_button.click()

    def back_to_products(self):
        self.back_button.click()