from selenium.webdriver.common.by import By


class OrderFeedPageLocators:
    FEED_SECTION = (By.XPATH, "//main")

    TOTAL_DONE_COUNTER = (
        By.XPATH,
        "//p[contains(.,'Выполнено за все время')]/following-sibling::p[contains(@class,'OrderFeed_number')]",
    )
    TODAY_DONE_COUNTER = (
        By.XPATH,
        "//p[contains(.,'Выполнено за сегодня')]/following-sibling::p[contains(@class,'OrderFeed_number')]",
    )

    IN_PROGRESS_LIST = (By.XPATH, "//ul[contains(@class,'OrderFeed_orderListReady')]")
    IN_PROGRESS_ORDER_NUMBERS = (
        By.XPATH,
        "//p[contains(normalize-space(),'В работе')]/following-sibling::ul[1]//li[contains(@class,'text_type_digits-default')]",
    )
