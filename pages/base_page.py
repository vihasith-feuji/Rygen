import logging
from playwright.sync_api import Page, Locator, expect

try:
    import allure
except ImportError:
    allure = None

logger = logging.getLogger(__name__)


class BasePage:
    """Base Page class encapsulating common Playwright web element actions,

    navigation, waits, dropdown handling, and Allure reporting attachments.
    """

    def __init__(self, page: Page):
        self.page = page

    def _get_locator(self, target) -> Locator:
        """Helper to convert string selectors or return existing Locator instances."""
        if isinstance(target, str):
            return self.page.locator(target)
        return target

    # =========================================================================
    # Navigation & Page Info
    # =========================================================================

    def navigate(self, url: str):
        """Navigate to a specified URL."""
        self.page.goto(url)

    def get_url(self) -> str:
        """Return the current page URL."""
        return self.page.url

    def get_title(self) -> str:
        """Return the current page title."""
        return self.page.title()

    def reload(self):
        """Reload the current page."""
        self.page.reload()

    # =========================================================================
    # Element Interactions
    # =========================================================================

    def click(self, target, timeout: float = None):
        """Wait for element to be visible/clickable and click it."""
        loc = self._get_locator(target)
        if timeout is not None:
            loc.click(timeout=timeout)
        else:
            loc.click()

    def fill(self, target, value, timeout: float = None):
        """Wait for element and fill it with value (string converted)."""
        loc = self._get_locator(target)
        val = "" if value is None else str(value)
        if timeout is not None:
            loc.fill(val, timeout=timeout)
        else:
            loc.fill(val)

    def type_text(self, target, text: str, delay: float = 0):
        """Sequentially type text into an element."""
        loc = self._get_locator(target)
        loc.press_sequentially(str(text), delay=delay)

    def clear(self, target):
        """Clear text from an input element."""
        loc = self._get_locator(target)
        loc.clear()

    def get_text(self, target) -> str:
        """Get the trimmed inner text of an element."""
        loc = self._get_locator(target)
        return loc.inner_text().strip()

    def get_input_value(self, target) -> str:
        """Get the current value of an input field."""
        loc = self._get_locator(target)
        return loc.input_value()

    # =========================================================================
    # Waiting & Visibility
    # =========================================================================

    def is_visible(self, target, timeout: float = 5000) -> bool:
        """Check if an element is visible within timeout without throwing an exception."""
        try:
            loc = self._get_locator(target)
            loc.wait_for(state="visible", timeout=timeout)
            return True
        except Exception:
            return False

    def wait_for_visible(self, target, timeout: float = 30000) -> Locator:
        """Wait for an element to be visible using Playwright expect."""
        loc = self._get_locator(target)
        expect(loc).to_be_visible(timeout=timeout)
        return loc

    def wait_for_hidden(self, target, timeout: float = 30000) -> Locator:
        """Wait for an element to be hidden/detached."""
        loc = self._get_locator(target)
        expect(loc).to_be_hidden(timeout=timeout)
        return loc

    # =========================================================================
    # Custom Dropdowns & Keyboard Actions
    # =========================================================================

    def select_dropdown_option(
        self,
        dropdown_target,
        option_text: str,
        overlay_selector: str = ".p-select-overlay, .p-dropdown-panel",
        timeout: float = 10000
    ):
        """Click a dropdown trigger, wait for the overlay option, and select it."""
        drop = self._get_locator(dropdown_target)
        drop.click()
        option = self.page.locator(overlay_selector).get_by_role(
            "option",
            name=str(option_text),
            exact=True
        )
        expect(option).to_be_visible(timeout=timeout)
        option.click()

    def press_key(self, key: str):
        """Press a keyboard key (e.g. 'Escape', 'Enter', 'Tab')."""
        self.page.keyboard.press(key)

    def scroll_into_view(self, target):
        """Scroll element into view if needed."""
        loc = self._get_locator(target)
        loc.scroll_into_view_if_needed()

    # =========================================================================
    # Screenshots & Allure Reporting
    # =========================================================================

    def take_screenshot(self, name: str = "screenshot", attach_to_allure: bool = True) -> bytes:
        """Capture screenshot of the active page and optionally attach to Allure."""
        screenshot_bytes = self.page.screenshot()
        if attach_to_allure and allure:
            allure.attach(
                screenshot_bytes,
                name=name,
                attachment_type=allure.attachment_type.PNG
            )
        return screenshot_bytes