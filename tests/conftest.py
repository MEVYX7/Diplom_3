from pathlib import Path

import pytest
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService

from data.data import BASE_URL, generate_user_payload
from pages.account_page import AccountPage


def _resolve_driver_binary(path, binary_name):
    p = Path(path)
    if p.is_file() and p.name.lower() == binary_name.lower():
        return str(p)

    root = p.parent if p.is_file() else p
    matches = list(root.rglob(binary_name))
    if not matches:
        raise FileNotFoundError(f"Cannot find {binary_name} in {root}")
    return str(matches[0])


def _build_chrome():
    options = ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    try:
        return webdriver.Chrome(options=options)
    except Exception:
        chrome_path = _resolve_driver_binary(ChromeDriverManager().install(), "chromedriver.exe")
        return webdriver.Chrome(service=ChromeService(chrome_path), options=options)


def _build_firefox():
    options = FirefoxOptions()

    try:
        return webdriver.Firefox(options=options)
    except Exception:
        gecko_path = _resolve_driver_binary(GeckoDriverManager().install(), "geckodriver.exe")
        return webdriver.Firefox(service=FirefoxService(gecko_path), options=options)


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        choices=["chrome", "firefox"],
        help="Browser for UI tests",
    )


@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")


    browser_driver = _build_firefox() if browser == "firefox" else _build_chrome()
    browser_driver.get(BASE_URL)

    yield browser_driver
    browser_driver.quit()


@pytest.fixture
def registered_user(driver):
    payload = generate_user_payload()

    driver.get(f"{BASE_URL}/register")
    account_page = AccountPage(driver, timeout=20)
    account_page.register(payload["name"], payload["email"], payload["password"])

    try:
        account_page.wait_for_url_contains("/login")
    except TimeoutException:
        account_page.submit_register_again()
        try:
            account_page.wait_for_url_contains("/login")
        except TimeoutException:
            error_text = account_page.get_register_error_text()
            pytest.fail(
                "UI registration did not redirect to /login. "
                f"Current URL: {driver.current_url}; user email: {payload['email']}; "
                f"form error: {error_text or 'no visible form error'}"
            )

    return {
        "email": payload["email"],
        "password": payload["password"],
        "access_token": None,
    }
