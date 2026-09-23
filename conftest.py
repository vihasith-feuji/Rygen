import os
import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.domain_page import DomainPage
from pages.order_page import OrderPage
from pages.create_order_page import CreateOrderPage
from utils.test_data_read import load_order_data

# Page Object Fixtures 

@pytest.fixture
def login_page(page: Page) -> LoginPage:
    return LoginPage(page)


@pytest.fixture
def domain_page(page: Page) -> DomainPage:
    return DomainPage(page)


@pytest.fixture
def order_page(page: Page) -> OrderPage:
    return OrderPage(page)


@pytest.fixture
def create_order_page(page: Page) -> CreateOrderPage:
    return CreateOrderPage(page)


# Test Data Fixtures

@pytest.fixture(scope="session")
def order_data():
    return load_order_data()




@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    # Allow Pytest to execute the test first
    outcome = yield

    # Get the test result
    report = outcome.get_result()

    # Take screenshot only when the actual test fails
    if report.when == "call" and report.failed:

        page = item.funcargs.get("page")
        if not page:
            for fixture_name in ["create_order_page", "order_page", "domain_page", "login_page"]:
                obj = item.funcargs.get(fixture_name)
                if obj and hasattr(obj, "page"):
                    page = obj.page
                    break

        if page:
            try:
                
                # Create screenshot folder if it doesn't exist
                os.makedirs("reports/screenshots", exist_ok=True)

                # Get test name
                test_name = item.name.split("[")[0]

                # Screenshot path
                screenshot_path = f"reports/screenshots/{test_name}.png"

                # Take screenshot
                screenshot_bytes = page.screenshot(path=screenshot_path, full_page=True)

                print(f"\nFailure screenshot saved: {screenshot_path}")

                # Attach screenshot to Allure Report
                try:
                    import allure
                    allure.attach(
                        screenshot_bytes,
                        name=f"failure_screenshot_{test_name}",
                        attachment_type=allure.attachment_type.PNG
                    )
                    allure.attach(
                        page.url,
                        name="failed_page_url",
                        attachment_type=allure.attachment_type.TEXT
                    )
                except Exception:
                    pass
            except Exception as e:
                print(f"Failed to capture failure screenshot: {e}")
