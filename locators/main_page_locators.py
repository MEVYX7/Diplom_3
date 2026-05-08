from selenium.webdriver.common.by import By


class MainPageLocators:
    CONSTRUCTOR_TAB = (By.XPATH, "//p[normalize-space()='Конструктор']")
    ORDER_FEED_TAB = (By.XPATH, "//p[normalize-space()='Лента Заказов']")

    INGREDIENT_CARD_BY_NAME = "//a[.//p[normalize-space()='{name}']]"
    INGREDIENT_COUNTER_BY_NAME = "//a[.//p[normalize-space()='{name}']]//p[contains(@class,'counter_counter__num')]"

    MODAL = (By.XPATH, "//section[contains(@class,'Modal_modal_opened')]")
    MODAL_CLOSE_BUTTON = (By.XPATH, "//section[contains(@class,'Modal_modal_opened')]//button")
    MODAL_HEADER = (By.XPATH, "//h2[normalize-space()='Детали ингредиента']")

    TOP_BUN_DROP_ZONE = (
        By.XPATH,
        "//p[contains(.,'Перетащите булк') and contains(.,'(верх)')]/ancestor::section[1]",
    )
    MAIN_DROP_ZONE = (
        By.XPATH,
        "//p[contains(.,'Перетащите начинк')]/ancestor::section[1]",
    )

    CONSTRUCTOR_DROP_FALLBACKS = [
        (By.XPATH, "//section[contains(@class,'BurgerConstructor_basket')]"),
        (By.XPATH, "//section[contains(@class,'BurgerConstructor')]"),
        (By.XPATH, "//button[normalize-space()='Оформить заказ']/ancestor::section[1]"),
    ]

    PLACE_ORDER_BUTTON = (By.XPATH, "//button[normalize-space()='Оформить заказ']")
    LOGIN_BUTTON = (By.XPATH, "//button[normalize-space()='Войти в аккаунт']")

    ORDER_MODAL = (By.XPATH, "//section[contains(@class,'Modal_modal_opened')]//h2[contains(@class,'text_type_digits-large')]")
    ORDER_MODAL_CLOSE_BUTTON = MODAL_CLOSE_BUTTON
