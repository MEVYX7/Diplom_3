from locators.order_feed_page_locators import OrderFeedPageLocators
from pages.base_page import BasePage


class OrderFeedPage(BasePage):
    def get_total_done_count(self):
        return int(self.get_text(OrderFeedPageLocators.TOTAL_DONE_COUNTER).replace(',', ''))

    def get_today_done_count(self):
        return int(self.get_text(OrderFeedPageLocators.TODAY_DONE_COUNTER).replace(',', ''))

    def get_in_progress_numbers(self):
        return [element.text.strip() for element in self.find_elements(OrderFeedPageLocators.IN_PROGRESS_ORDER_NUMBERS)]
