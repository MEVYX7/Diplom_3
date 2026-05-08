from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    MODAL_OVERLAY = ("css selector", "div[class*='Modal_modal_overlay']")

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self, url):
        self.driver.get(url)

    def find_element(self, locator):
        return self.wait.until(ec.visibility_of_element_located(locator))

    def find_element_with_wait(self, locator):
        return self.find_element(locator)

    def find_elements(self, locator):
        self.wait.until(ec.presence_of_element_located(locator))
        return self.driver.find_elements(*locator)

    def _wait_modal_overlay_disappear(self):
        try:
            self.wait.until(ec.invisibility_of_element_located(self.MODAL_OVERLAY))
        except TimeoutException:
            pass

    def click(self, locator):
        self._wait_modal_overlay_disappear()
        element = self.wait.until(ec.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

        try:
            element.click()
        except ElementClickInterceptedException:
            self._wait_modal_overlay_disappear()
            self.driver.execute_script("arguments[0].click();", element)

    def fill(self, locator, value):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(value)

    def is_visible(self, locator):
        try:
            self.wait.until(ec.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def wait_for_invisible(self, locator):
        self.wait.until(ec.invisibility_of_element_located(locator))

    def wait_for_url_contains(self, value):
        self.wait.until(ec.url_contains(value))

    def wait_for_url_not_contains(self, value):
        self.wait.until_not(ec.url_contains(value))

    def get_current_url(self):
        return self.driver.current_url

    def get_text(self, locator):
        return self.find_element(locator).text

    def drag_and_drop(self, source_locator, target_locator):
        self.find_element_with_wait(source_locator)
        self.wait.until(ec.presence_of_element_located(target_locator))

        element_from = self.driver.find_element(*source_locator)
        element_to = self.driver.find_element(*target_locator)

        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element_from)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element_to)

        self.driver.execute_script(
            """
            var source = arguments[0];
            var target = arguments[1];

            var evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragstart", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            source.dispatchEvent(evt);

            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragenter", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            target.dispatchEvent(evt);

            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragover", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            target.dispatchEvent(evt);

            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("drop", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            target.dispatchEvent(evt);

            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragend", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            source.dispatchEvent(evt);
            """,
            element_from,
            element_to,
        )
