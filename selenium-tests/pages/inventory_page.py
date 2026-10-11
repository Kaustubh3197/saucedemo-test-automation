from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class InventoryPage(BasePage):
    TITLE = (By.CLASS_NAME, "title")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    @staticmethod
    def _slug(name):
        return name.lower().replace(" ", "-")

    def title(self):
        return self.text_of(self.TITLE)

    def add_to_cart(self, name):
        self.click((By.CSS_SELECTOR, f"[data-test='add-to-cart-{self._slug(name)}']"))

    def remove_from_cart(self, name):
        self.click((By.CSS_SELECTOR, f"[data-test='remove-{self._slug(name)}']"))

    def cart_count(self):
        return self.text_of(self.CART_BADGE)

    def open_cart(self):
        self.click(self.CART_LINK)
