import re
from playwright.sync_api import Page, expect


def test_valid_user_can_log_in(login_page, page: Page):
    login_page.login("standard_user")
    expect(page).to_have_url(re.compile(r"inventory\.html"))
    expect(page.locator(".title")).to_have_text("Products")


def test_locked_out_user_sees_error(login_page):
    login_page.login("locked_out_user")
    expect(login_page.error).to_contain_text("this user has been locked out")


def test_wrong_password_is_rejected(login_page):
    login_page.login("standard_user", "wrong_password")
    expect(login_page.error).to_contain_text("do not match any user")


def test_logged_out_user_cannot_open_inventory(login_page, page: Page):
    page.goto("/inventory.html")
    expect(login_page.error).to_contain_text("when you are logged in")
