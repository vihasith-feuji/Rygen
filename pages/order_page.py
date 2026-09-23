from playwright.sync_api import Page
from utils.assertions import Assertions
from pages.base_page import BasePage
from utils.logger import get_logger

logger = get_logger(__name__)


class OrderPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.assertions = Assertions()

        # Locators
        self.dashboard = self.page.get_by_text("Dashboard", exact=True)
        self.order = self.page.get_by_text("Order", exact=True)
        self.new_order = self.page.get_by_text("New Order", exact=True)
        self.jcb_client = self.page.locator('//span[@class="p-tree-node-label" and text()="JCB"]')
        self.back_to_all_orders = self.page.get_by_text("Back to All Orders", exact=True)

    def click_order(self):
        logger.info("Clicking Order")
        self.wait_for_visible(self.order)
        self.click(self.order)

        self.wait_for_visible(self.new_order)
        self.assertions.assert_visible(self.new_order)
        self.assertions.assert_enabled(self.new_order)
        logger.info("New Order button is visible and enabled")

    def click_new_order(self):
        logger.info("Clicking New Order")
        self.wait_for_visible(self.new_order)
        self.click(self.new_order)

    def close_popup(self):
        logger.info("Closing popup if present")
        try:
            if self.jcb_client.is_visible(timeout=3000):
                self.click(self.jcb_client)
        except Exception:
            pass

    def back_to_all_orders(self):
        logger.info("Going back to all orders")
        self.click(self.back_to_all_orders)