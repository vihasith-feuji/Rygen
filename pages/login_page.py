from pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

        self.username_input = page.locator("//input[@id='signInName']")
        self.password_input = page.get_by_role(
            "textbox",
            name="Password"
        )
        self.continue_btn = page.locator("//button[@id='continue']")
        self.login_button = page.get_by_role(
            "button",
            name="Sign in"
        )

    def enter_username(self, username):
        self.fill(self.username_input, username)

    def enter_password(self, password):
        self.fill(self.password_input, password)

    def click_continue(self):
        self.click(self.continue_btn)

    def click_login(self):
        self.click(self.login_button)

    def login(self, username, password):
        self.enter_username(username)
        self.click_continue()
        self.enter_password(password)
        self.click_login()
