from playwright.sync_api import Page
from utils.logger import get_logger

logger = get_logger(__name__)


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def click(self, locator, force=False):
        try:
            locator.scroll_into_view_if_needed()
            try:
                locator.click(timeout=7000, force=force)
            except Exception:
                locator.click(force=True)
        except Exception as e:
            logger.error(f"Failed to click element: {e}")
            raise

    def fill(self, locator, text):
        try:
            locator.scroll_into_view_if_needed()
            locator.fill(str(text))
        except Exception as e:
            logger.error(f"Failed to fill element: {e}")
            raise

    def wait_for_visible(self, locator, timeout=30000):
        try:
            locator.wait_for(state="visible", timeout=timeout)
        except Exception as e:
            logger.error(f"Element did not become visible: {e}")
            raise

    def check(self, locator):
        try:
            locator.scroll_into_view_if_needed()
            if not locator.is_checked():
                try:
                    locator.check(timeout=5000)
                except Exception:
                    locator.click(force=True)
        except Exception as e:
            logger.error(f"Check failed: {e}")
            raise

    def uncheck(self, locator):
        try:
            locator.scroll_into_view_if_needed()
            if locator.is_checked():
                try:
                    locator.uncheck(timeout=5000)
                except Exception:
                    locator.click(force=True)
        except Exception as e:
            logger.error(f"Uncheck failed: {e}")
            raise

    def select_option(self, locator, value):
        try:
            locator.scroll_into_view_if_needed()
            locator.select_option(value)
        except Exception as e:
            logger.error(f"Select option '{value}' failed: {e}")
            raise

    def select_dropdown(self, dropdown_locator, option_text):
        try:
            self.click(dropdown_locator)
            overlay = self.page.locator(
                ".p-dropdown-panel:visible, .p-select-overlay:visible, [role='listbox']:visible, .p-overlay:visible, .p-popover:visible"
            ).last
            option = overlay.locator(
                f'li[role="option"]:has-text("{option_text}"), '
                f'.p-dropdown-item:has-text("{option_text}"), '
                f'[role="option"]:has-text("{option_text}")'
            ).first
            try:
                option.wait_for(state="visible", timeout=3000)
            except Exception:
                self.click(dropdown_locator)
                option.wait_for(state="visible", timeout=5000)
            self.click(option)
        except Exception as e:
            logger.error(f"Failed to select dropdown option '{option_text}': {e}")
            raise

    def get_text(self, locator):
        try:
            locator.scroll_into_view_if_needed()
            return locator.inner_text()
        except Exception as e:
            logger.error(f"Failed to get element text: {e}")
            raise

    def is_visible(self, locator):
        try:
            return locator.is_visible()
        except Exception as e:
            logger.error(f"Failed to check visibility: {e}")
            raise