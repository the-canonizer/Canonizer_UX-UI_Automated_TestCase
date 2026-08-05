from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from CanonizerBase import Page
from Config import DEFAULT_BASE_URL
from Identifiers import SearchPageIdentifiers


class CanonizerSearchPage(Page):
    """Search results navigation, filter routes, and pagination checks."""

    def _search_url(self, path, query, extra=""):
        suffix = f"{path}?q={query}"
        if extra:
            suffix = f"{suffix}&{extra}"
        return f"{DEFAULT_BASE_URL.rstrip('/')}{suffix}"

    def open_all_results(self, query):
        self.driver.get(self._search_url("/search", query))
        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(SearchPageIdentifiers.ALL_RESULTS_SECTION)
        )
        return self

    def open_topic_results(self, query, extra=""):
        self.driver.get(self._search_url("/search/topic", query, extra))
        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(SearchPageIdentifiers.TOPIC_HEADING)
        )
        return self

    def open_camp_results(self, query, extra=""):
        self.driver.get(self._search_url("/search/camp", query, extra))
        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(SearchPageIdentifiers.CAMP_HEADING)
        )
        return self

    def open_camp_statement_results(self, query, extra=""):
        self.driver.get(self._search_url("/search/camp_statement", query, extra))
        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(SearchPageIdentifiers.CAMP_STATEMENT_HEADING)
        )
        return self

    def open_nickname_results(self, query):
        self.driver.get(self._search_url("/search/nickname", query))
        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(SearchPageIdentifiers.NICKNAME_HEADING)
        )
        return self

    def click_sidebar_tab(self, tab_name):
        locator = (By.XPATH, f'//a[contains(@href, "{tab_name}")]//button')
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator)).click()
        return self

    def is_pagination_visible(self):
        elements = self.driver.find_elements(*SearchPageIdentifiers.PAGINATION)
        return len(elements) > 0 and elements[0].is_displayed()
