from locators.order_feed_page_locators import OrderFeedPageLocators
from pages.base_page import BasePage


class OrderFeedPage(BasePage):
    def get_total_done_count(self):
        return int(self.get_text(OrderFeedPageLocators.TOTAL_DONE_COUNTER).replace(',', ''))

    def get_today_done_count(self):
        return int(self.get_text(OrderFeedPageLocators.TODAY_DONE_COUNTER).replace(',', ''))

    def get_in_progress_numbers(self):
        elements = self.driver.find_elements(*OrderFeedPageLocators.IN_PROGRESS_ORDER_NUMBERS)
        return [element.text.strip() for element in elements]

    @staticmethod
    def _normalize_order_number(value):
        normalized = value.replace("#", "").strip().lstrip("0")
        return normalized if normalized else "0"

    def wait_for_order_in_progress(self, order_number):
        normalized_target = self._normalize_order_number(order_number)

        def _order_present(_):
            return normalized_target in [
                self._normalize_order_number(number)
                for number in self.get_in_progress_numbers()
            ]

        return self.wait.until(_order_present)
