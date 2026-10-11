from playwright.sync_api import Page


class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.title = page.locator(".title")
        self.item_names = page.locator(".inventory_item_name")
        self.item_prices = page.locator(".inventory_item_price")
        self.sort_dropdown = page.locator("[data-test='product-sort-container']")
        self.cart_badge = page.locator(".shopping_cart_badge")
        self.cart_link = page.locator(".shopping_cart_link")

    @staticmethod
    def _slug(name: str) -> str:
        # "Sauce Labs Backpack" -> "sauce-labs-backpack"
        return name.lower().replace(" ", "-")

    def add_to_cart(self, name: str):
        self.page.locator(f"[data-test='add-to-cart-{self._slug(name)}']").click()

    def remove_from_cart(self, name: str):
        self.page.locator(f"[data-test='remove-{self._slug(name)}']").click()

    def sort_by(self, value: str):
        """value: az | za | lohi | hilo"""
        self.sort_dropdown.select_option(value)

    def prices(self) -> list[float]:
        return [float(t.replace("$", "")) for t in self.item_prices.all_text_contents()]

    def names(self) -> list[str]:
        return self.item_names.all_text_contents()

    def open_cart(self):
        self.cart_link.click()

    def open_product(self, name: str):
        """Click a product's name to open its details page."""
        self.item_names.filter(has_text=name).click()
