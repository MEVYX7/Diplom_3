import allure

from data.data import BASE_URL
from pages.account_page import AccountPage
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage


@allure.feature("Лента заказов")
class TestOrderFeedPage:
    @staticmethod
    def _normalize_order_number(value):
        normalized = value.replace("#", "").strip().lstrip("0")
        return normalized if normalized else "0"

    def _login(self, driver, user):
        driver.get(f"{BASE_URL}/login")
        account_page = AccountPage(driver)
        account_page.login(user["email"], user["password"])
        account_page.wait_for_url_not_contains("/login")

    def _create_order(self, driver):
        main_page = MainPage(driver)
        main_page.add_ingredient_to_constructor("Флюоресцентная булка R2-D3", use_bun_zone=True)
        main_page.add_ingredient_to_constructor("Мясо бессмертных моллюсков Protostomia")
        main_page.click_place_order()

        order_number = main_page.get_order_number_from_modal()
        main_page.close_modal()
        main_page.wait_order_modal_closed()
        return order_number

    @allure.title("После создания заказа счетчик 'Выполнено за все время' увеличивается")
    def test_total_done_counter_increases_after_new_order(self, driver, registered_user):
        self._login(driver, registered_user)

        main_page = MainPage(driver)
        main_page.click_order_feed_tab()
        feed_page = OrderFeedPage(driver)
        before = feed_page.get_total_done_count()

        main_page.click_constructor_tab()
        self._create_order(driver)

        main_page.click_order_feed_tab()
        after = feed_page.get_total_done_count()

        assert after >= before + 1

    @allure.title("После создания заказа счетчик 'Выполнено за сегодня' увеличивается")
    def test_today_done_counter_increases_after_new_order(self, driver, registered_user):
        self._login(driver, registered_user)

        main_page = MainPage(driver)
        main_page.click_order_feed_tab()
        feed_page = OrderFeedPage(driver)
        before = feed_page.get_today_done_count()

        main_page.click_constructor_tab()
        self._create_order(driver)

        main_page.click_order_feed_tab()
        after = feed_page.get_today_done_count()

        assert after >= before + 1

    @allure.title("Номер нового заказа появляется в разделе 'В работе'")
    def test_created_order_number_is_visible_in_progress_block(self, driver, registered_user):
        self._login(driver, registered_user)

        order_number = self._normalize_order_number(self._create_order(driver))

        main_page = MainPage(driver)
        main_page.click_order_feed_tab()

        feed_page = OrderFeedPage(driver)
        in_progress_numbers = [
            self._normalize_order_number(number)
            for number in feed_page.get_in_progress_numbers()
        ]

        assert order_number in in_progress_numbers
