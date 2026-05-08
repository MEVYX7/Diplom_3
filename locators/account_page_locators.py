from selenium.webdriver.common.by import By


class AccountPageLocators:
    LOGIN_FORM = (By.XPATH, "//form[.//button[text()='Войти']]")
    REGISTER_FORM = (By.XPATH, "//form[.//button[text()='Зарегистрироваться']]")

    LOGIN_EMAIL_INPUT = (By.XPATH, "//form[.//button[text()='Войти']]//label[text()='Email']/following-sibling::input")
    LOGIN_PASSWORD_INPUT = (By.XPATH, "//form[.//button[text()='Войти']]//input[@type='password']")
    LOGIN_SUBMIT_BUTTON = (By.XPATH, "//button[text()='Войти']")

    REGISTER_NAME_INPUT = (By.XPATH, "//form[.//button[text()='Зарегистрироваться']]//label[text()='Имя']/following-sibling::input")
    REGISTER_EMAIL_INPUT = (By.XPATH, "//form[.//button[text()='Зарегистрироваться']]//label[text()='Email']/following-sibling::input")
    REGISTER_PASSWORD_INPUT = (By.XPATH, "//form[.//button[text()='Зарегистрироваться']]//input[@type='password']")
    REGISTER_SUBMIT_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    REGISTER_ERROR_TEXT = (By.XPATH, "//form[.//button[text()='Зарегистрироваться']]//p[contains(@class,'input__error')]")

    PROFILE_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")
