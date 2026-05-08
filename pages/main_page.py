from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    def click_constructor_tab(self):
        self.click(MainPageLocators.CONSTRUCTOR_TAB)

    def click_order_feed_tab(self):
        self.click(MainPageLocators.ORDER_FEED_TAB)

    def click_ingredient_card(self, ingredient_name):
        locator = (By.XPATH, MainPageLocators.INGREDIENT_CARD_BY_NAME.format(name=ingredient_name))
        element = self.wait.until(ec.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

        try:
            self.wait.until(ec.element_to_be_clickable(locator)).click()
        except Exception:
            self.driver.execute_script("arguments[0].click();", element)

    def get_ingredient_counter(self, ingredient_name):
        locator = MainPageLocators.INGREDIENT_COUNTER_BY_NAME.format(name=ingredient_name)
        elements = self.driver.find_elements("xpath", locator)
        if not elements:
            return 0
        value = elements[0].text.strip()
        return int(value) if value else 0

    def close_modal(self):
        try:
            self.click(MainPageLocators.MODAL_CLOSE_BUTTON)
        except Exception:
            close_btn = self.find_element(MainPageLocators.MODAL_CLOSE_BUTTON)
            self.driver.execute_script("arguments[0].click();", close_btn)

    def add_ingredient_to_constructor(self, ingredient_name, use_bun_zone=False):
        source_locator = (By.XPATH, MainPageLocators.INGREDIENT_CARD_BY_NAME.format(name=ingredient_name))

        preferred_target = MainPageLocators.TOP_BUN_DROP_ZONE if use_bun_zone else MainPageLocators.MAIN_DROP_ZONE
        target_candidates = [preferred_target, *MainPageLocators.CONSTRUCTOR_DROP_FALLBACKS]

        last_error = None
        for target_locator in target_candidates:
            try:
                self.drag_and_drop(source_locator, target_locator)
                return
            except TimeoutException as exc:
                last_error = exc

        if last_error:
            raise last_error

    def click_place_order(self):
        self.click(MainPageLocators.PLACE_ORDER_BUTTON)

    def get_order_number_from_modal(self):
        def _order_number_ready(driver):
            text = self.get_text(MainPageLocators.ORDER_MODAL).strip()
            return text if text.isdigit() and text != "9999" else False

        return self.wait.until(_order_number_ready)

    def wait_order_modal_closed(self):
        self.wait_for_invisible(MainPageLocators.ORDER_MODAL)
