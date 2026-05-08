import allure

from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage


@allure.feature("Главная страница")
class TestMainPage:
    @allure.title("Переход по клику на 'Конструктор'")
    def test_open_constructor_tab(self, driver):
        page = MainPage(driver)

        page.click_order_feed_tab()
        page.wait_for_url_contains('/feed')
        page.click_constructor_tab()

        assert '/feed' not in page.get_current_url()

    @allure.title("Переход по клику на раздел 'Лента заказов'")
    def test_open_order_feed_tab(self, driver):
        page = MainPage(driver)

        page.click_order_feed_tab()

        assert '/feed' in page.get_current_url()

    @allure.title("По клику на ингредиент открывается модальное окно с деталями")
    def test_ingredient_details_modal_opens(self, driver):
        page = MainPage(driver)

        page.click_ingredient_card('Флюоресцентная булка R2-D3')

        assert page.is_visible(MainPageLocators.MODAL)

    @allure.title("Модальное окно с деталями закрывается по крестику")
    def test_ingredient_details_modal_closes_by_cross_click(self, driver):
        page = MainPage(driver)

        page.click_ingredient_card('Флюоресцентная булка R2-D3')
        page.close_modal()

        assert not page.is_visible(MainPageLocators.MODAL)

    @allure.title("При добавлении ингредиента счетчик увеличивается")
    def test_ingredient_counter_increases_when_added_to_order(self, driver):
        page = MainPage(driver)

        ingredient_name = 'Флюоресцентная булка R2-D3'
        before = page.get_ingredient_counter(ingredient_name)

        page.add_ingredient_to_constructor(ingredient_name, use_bun_zone=True)
        after = page.get_ingredient_counter(ingredient_name)

        assert after > before
