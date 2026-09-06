from playwright.sync_api import Page

from pages.base_page import BasePage


class OrderPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

        self.order_link = page.get_by_role(
            "link",
            name="Order"
        )

        self.new_order_button = page.get_by_test_id(
            "order-list-new-button"
        )

    def click_order(self):
        self.click(self.order_link)

    def click_new_order(self):
        self.wait_for_visible(self.new_order_button, timeout=15000)
        self.click(self.new_order_button)