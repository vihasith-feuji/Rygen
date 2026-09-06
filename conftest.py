import os
import pytest
from playwright.sync_api import Page

try:
    import allure
except ImportError:
    allure = None

from pages.login_page import LoginPage
from pages.domain_page import DomainPage
from pages.order_page import OrderPage
from pages.create_order_page import CreateOrderPage
from utils.test_data_reader import load_test_data


# =============================================================================
# Playwright Browser Context Options
# =============================================================================

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    """Set default browser context parameters: standard 1080p viewport and SSL tolerance."""
    return {
        **browser_context_args,
        "viewport": {"width": 1920, "height": 1080},
        "ignore_https_errors": True,
    }


# =============================================================================
# Test Data Fixtures
# =============================================================================

@pytest.fixture(scope="session")
def order_test_data():
    """Load order test data from test-data/order_data.json."""
    data_path = os.path.join(os.path.dirname(__file__), "test-data", "order_data.json")
    return load_test_data(data_path)


# =============================================================================
# Page Object Fixtures
# =============================================================================

@pytest.fixture
def login_page(page: Page) -> LoginPage:
    """Fixture providing an instance of LoginPage."""
    return LoginPage(page)


@pytest.fixture
def domain_page(page: Page) -> DomainPage:
    """Fixture providing an instance of DomainPage."""
    return DomainPage(page)


@pytest.fixture
def order_page(page: Page) -> OrderPage:
    """Fixture providing an instance of OrderPage."""
    return OrderPage(page)


@pytest.fixture
def create_order_page(page: Page) -> CreateOrderPage:
    """Fixture providing an instance of CreateOrderPage."""
    return CreateOrderPage(page)


# =============================================================================
# Allure Automatic Screenshot Hook on Failure
# =============================================================================

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Automatically capture screenshot and URL if a test step fails and attach to Allure."""
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page")
        if page and allure:
            try:
                screenshot_bytes = page.screenshot()
                allure.attach(
                    screenshot_bytes,
                    name=f"failure_{item.name}",
                    attachment_type=allure.attachment_type.PNG
                )
                allure.attach(
                    page.url,
                    name="failure_url",
                    attachment_type=allure.attachment_type.TEXT
                )
            except Exception as e:
                print(f"[conftest] Warning: Could not capture failure screenshot: {e}")
