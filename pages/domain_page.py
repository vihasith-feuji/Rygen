from pages.base_page import BasePage


class DomainPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

        self.search_box = page.get_by_role(
            "searchbox",
            name="Search"
        )

        self.jcb_option = page.get_by_text("JCB")

    def search_domain(self, domain):
        self.fill(self.search_box, domain)

    def select_jcb(self):
        self.click(self.jcb_option)
