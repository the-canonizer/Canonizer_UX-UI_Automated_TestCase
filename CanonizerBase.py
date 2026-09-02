import time

from selenium.common.exceptions import (
    ElementClickInterceptedException,
    InvalidElementStateException,
    StaleElementReferenceException,
    TimeoutException,
)
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

from Config import DEFAULT_BASE_URL


class Page(object):
    def __init__(self, driver, base_url=DEFAULT_BASE_URL):
        self.base_url = base_url
        self.driver = driver
        self.timeout = 30

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def open(self, url):
        url = self.base_url + url
        self.driver.get(url)

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    def hover(self, *locator):
        element = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((locator[0], locator[1]))
        )
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    def get_attribute(self):
        return self.driver.attribute

    def wait_for_loading_overlays(self, timeout=10):
        """Wait until common full-page loaders are no longer blocking interactions."""
        selectors = (
            "div.ant-spin-spinning",
            ".ant-spin-spinning",
        )
        for selector in selectors:
            try:
                WebDriverWait(self.driver, timeout).until(
                    EC.invisibility_of_element_located(("css selector", selector))
                )
            except TimeoutException:
                # Not all screens use every overlay selector.
                pass

    def set_input_value(self, locator, value, clear_first=True, timeout=10):
        """Set an input value with waits/retry to avoid transient UI overlay and stale element failures."""
        for _ in range(2):
            try:
                self.wait_for_loading_overlays(timeout=timeout)
                field = WebDriverWait(self.driver, timeout).until(
                    EC.element_to_be_clickable(locator)
                )
                self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", field)
                if clear_first:
                    field.clear()
                if value:
                    field.send_keys(value)
                return field
            except (
                ElementClickInterceptedException,
                InvalidElementStateException,
                StaleElementReferenceException,
            ):
                time.sleep(0.2)

        self.wait_for_loading_overlays(timeout=timeout)
        field = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
        if clear_first:
            field.clear()
        if value:
            field.send_keys(value)
        return field

    def safe_click(self, locator, timeout=10, hover_first=False):
        """Click an element with wait/retry to survive transient overlays and stale references."""
        for _ in range(2):
            try:
                self.wait_for_loading_overlays(timeout=timeout)
                if hover_first:
                    self.hover(*locator)
                element = WebDriverWait(self.driver, timeout).until(
                    EC.element_to_be_clickable(locator)
                )
                self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
                element.click()
                return element
            except (ElementClickInterceptedException, StaleElementReferenceException):
                time.sleep(0.2)

        self.wait_for_loading_overlays(timeout=timeout)
        element = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
        element.click()
        return element

