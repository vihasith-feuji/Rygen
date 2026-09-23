from playwright.sync_api import Page
from pages.base_page import BasePage
from utils.assertions import Assertions
from utils.logger import get_logger

logger = get_logger(__name__)


class LoginPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.assertions = Assertions()

        # Locators
        self.username_field = self.page.get_by_placeholder("Username")
        self.continue_button = self.page.get_by_role("button", name="Continue")
        self.password_field = self.page.get_by_placeholder("Password")
        self.sign_in_button = self.page.get_by_role("button", name="Sign in")
        self.dashboard = self.page.get_by_text("Dashboard", exact=True)

    def navigate(self, url):
        logger.info(f"Navigating to {url}")
        self.page.goto(url)

    def login(self, username, password):
        try:
            logger.info("Entering username")
            self.assertions.assert_visible(self.username_field)
            self.fill(self.username_field, username)

            logger.info("Clicking Continue")
            self.assertions.assert_visible(self.continue_button)
            self.assertions.assert_enabled(self.continue_button)
            self.click(self.continue_button)

            # Wait for password field to appear, fallback with Enter or force click if needed
            try:
                self.password_field.wait_for(state="visible", timeout=5000)
            except Exception:
                if self.continue_button.is_visible():
                    self.username_field.press("Enter")
                try:
                    self.password_field.wait_for(state="visible", timeout=5000)
                except Exception:
                    if self.continue_button.is_visible():
                        self.click(self.continue_button, force=True)
                    self.password_field.wait_for(state="visible", timeout=10000)

            logger.info("Entering password")
            self.assertions.assert_visible(self.password_field)
            self.fill(self.password_field, password)

            logger.info("Clicking Sign In")
            self.assertions.assert_visible(self.sign_in_button)
            self.assertions.assert_enabled(self.sign_in_button)
            self.click(self.sign_in_button)

            try:
                self.page.wait_for_load_state("domcontentloaded", timeout=15000)
            except Exception:
                pass

        except Exception as e:
            logger.error(f"Login failed: {e}")
            raise

