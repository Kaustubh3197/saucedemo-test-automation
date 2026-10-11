from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckoutPage(BasePage):
    CHECKOUT_BTN = (By.CSS_SELECTOR, "[data-test='checkout']")
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BTN = (By.CSS_SELECTOR, "[data-test='continue']")
    FINISH_BTN = (By.CSS_SELECTOR, "[data-test='finish']")
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")

    def start_checkout(self):
        self.click(self.CHECKOUT_BTN)

    def fill_details(self, first, last, zip_code):
        self.type(self.FIRST_NAME, first)
        self.type(self.LAST_NAME, last)
        self.type(self.POSTAL_CODE, zip_code)
        self.click(self.CONTINUE_BTN)

    def finish(self):
        self.click(self.FINISH_BTN)

    def confirmation(self):
        return self.text_of(self.COMPLETE_HEADER)
