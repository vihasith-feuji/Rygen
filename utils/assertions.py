from playwright.sync_api import Locator, Page, expect
import logging

logger = logging.getLogger(__name__)


class Assertions:
    @staticmethod
    def assert_visible(locator: Locator, timeout: float = 30000):
        try:
            expect(locator).to_be_visible(timeout=timeout)
        except Exception as e:
            logger.error(f"Assertion failed: Element is not visible: {e}")
            raise

    @staticmethod
    def assert_enabled(locator: Locator, timeout: float = 30000):
        try:
            expect(locator).to_be_enabled(timeout=timeout)
        except Exception as e:
            logger.error(f"Assertion failed: Element is not enabled: {e}")
            raise

    @staticmethod
    def assert_checked(locator: Locator, timeout: float = 30000):
        try:
            expect(locator).to_be_checked(timeout=timeout)
        except Exception as e:
            logger.error(f"Assertion failed: Element is not checked: {e}")
            raise

    @staticmethod
    def assert_text(locator: Locator, expected_text: str, timeout: float = 30000):
        try:
            expect(locator).to_have_text(expected_text, timeout=timeout)
        except Exception as e:
            logger.error(f"Assertion failed: Element text is not '{expected_text}': {e}")
            raise

    @staticmethod
    def assert_contains_text(locator: Locator, expected_text: str, timeout: float = 30000):
        try:
            expect(locator).to_contain_text(expected_text, timeout=timeout)
        except Exception as e:
            logger.error(f"Assertion failed: Element does not contain text '{expected_text}': {e}")
            raise

    @staticmethod
    def assert_url(page: Page, expected_url: str, timeout: float = 30000):
        try:
            expect(page).to_have_url(expected_url, timeout=timeout)
        except Exception as e:
            logger.error(f"Assertion failed: URL is not '{expected_url}': {e}")
            raise
