from selenium.common.exceptions import TimeoutException

from locators.account_page_locators import AccountPageLocators
from pages.base_page import BasePage


class AccountPage(BasePage):
    def login(self, email, password):
        self.fill(AccountPageLocators.LOGIN_EMAIL_INPUT, email)
        self.fill(AccountPageLocators.LOGIN_PASSWORD_INPUT, password)
        self.click(AccountPageLocators.LOGIN_SUBMIT_BUTTON)

    def register(self, name, email, password):
        self.fill(AccountPageLocators.REGISTER_NAME_INPUT, name)
        self.fill(AccountPageLocators.REGISTER_EMAIL_INPUT, email)
        self.fill(AccountPageLocators.REGISTER_PASSWORD_INPUT, password)
        self.click(AccountPageLocators.REGISTER_SUBMIT_BUTTON)

    def submit_register_again(self):
        try:
            self.click(AccountPageLocators.REGISTER_SUBMIT_BUTTON)
        except Exception:
            button = self.find_element(AccountPageLocators.REGISTER_SUBMIT_BUTTON)
            self.driver.execute_script("arguments[0].click();", button)

    def get_register_error_text(self):
        try:
            return self.get_text(AccountPageLocators.REGISTER_ERROR_TEXT).strip()
        except TimeoutException:
            return ""
