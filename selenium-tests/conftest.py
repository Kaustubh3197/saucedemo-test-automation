import os
import pytest
from selenium import webdriver

BASE_URL = "https://www.saucedemo.com"


@pytest.fixture
def driver():
    """Start a fresh Chrome for every test and close it afterwards."""
    options = webdriver.ChromeOptions()
    if os.getenv("HEADLESS", "true").lower() == "true":
        options.add_argument("--headless=new")
    options.add_argument("--window-size=1280,900")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    # Stop Chrome's "change your password" popup from covering the page
    options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False,
    })

    drv = webdriver.Chrome(options=options)  # Selenium Manager finds the driver
    drv.get(BASE_URL)
    yield drv
    drv.quit()
