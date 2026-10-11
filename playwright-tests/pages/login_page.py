from playwright.sync_api import Page


class LoginPage:
    """Page Object: everything about the login page lives here."""

    def __init__(self, page: Page):
        self.page = page
        self.username = page.locator("#user-name")
        self.password = page.locator("#password")
        self.login_button = page.locator("#login-button")
        self.error = page.locator("[data-test='error']")

    def goto(self):
        self.page.goto("/")

    def login(self, username: str, password: str = "secret_sauce"):
        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()
