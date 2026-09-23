from playwright.sync_api import Page


class DomainPage:

    def __init__(self, page: Page):
        self.page = page

    def search_domain(self, domain_name):
        search_box = self.page.get_by_placeholder("Search Domains")
        search_box.fill(domain_name)

    def select_domain(self, domain_name):
        item = self.page.locator(f'//span[@class="p-tree-node-label" and text()="{domain_name}"] | //span[text()="{domain_name}"]').first
        item.click()
