from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from CanonizerBase import Page
from Config import (
    NOTIFICATION_URL,
    SUPPORTED_CAMP_URL,
    DELEGATE_SUPPORT_URL,
    USER_PREFERENCE_URL,
    SOCIAL_AUTH,
)
from Identifiers import AdvancedSettingsIdentifiers


class CanonizerAdvancedSettingsPage(Page):
    """Advanced settings workflows for notifications, support, preferences, and social auth."""

    def open_notifications(self):
        self.driver.get(NOTIFICATION_URL)
        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(AdvancedSettingsIdentifiers.NOTIFICATIONS_TITLE)
        )
        return self

    def notifications_apply_filters(self):
        self.find_element(*AdvancedSettingsIdentifiers.FILTER_UNREAD).click()
        self.find_element(*AdvancedSettingsIdentifiers.FILTER_READ).click()
        self.find_element(*AdvancedSettingsIdentifiers.FILTER_ALL).click()
        return self

    def open_mark_all_read_modal(self):
        self.find_element(*AdvancedSettingsIdentifiers.MARK_ALL_READ).click()
        return self

    def cancel_mark_all_read_modal(self):
        self.find_element(*AdvancedSettingsIdentifiers.MARK_ALL_READ_CANCEL).click()
        return self

    def open_delete_all_modal(self):
        self.find_element(*AdvancedSettingsIdentifiers.DELETE_ALL_NOTIFICATIONS).click()
        return self

    def cancel_delete_all_modal(self):
        self.find_element(*AdvancedSettingsIdentifiers.DELETE_ALL_GO_BACK).click()
        return self

    def click_load_more_if_available(self):
        try:
            button = WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable(AdvancedSettingsIdentifiers.LOAD_MORE_BUTTON)
            )
            button.click()
            return True
        except TimeoutException:
            return False

    def open_direct_supported(self):
        self.driver.get(SUPPORTED_CAMP_URL)
        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(AdvancedSettingsIdentifiers.DIRECT_TABLE)
        )
        return self

    def search_direct_supported(self, text):
        field = self.set_input_value(AdvancedSettingsIdentifiers.DIRECT_SEARCH, text)
        field.send_keys(Keys.ENTER)
        return self

    def open_direct_remove_modal(self):
        self.find_element(*AdvancedSettingsIdentifiers.DIRECT_REMOVE_ICON).click()
        return self

    def cancel_support_remove_modal(self):
        self.find_element(*AdvancedSettingsIdentifiers.SUPPORT_MODAL_CANCEL).click()
        return self

    def open_delegated_supported(self):
        self.driver.get(DELEGATE_SUPPORT_URL)
        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(AdvancedSettingsIdentifiers.DELEGATED_TABLE)
        )
        return self

    def search_delegated_supported(self, text):
        field = self.set_input_value(AdvancedSettingsIdentifiers.DELEGATED_SEARCH, text)
        field.send_keys(Keys.ENTER)
        return self

    def open_delegated_remove_modal(self):
        self.find_element(*AdvancedSettingsIdentifiers.DELEGATED_REMOVE_ICON).click()
        return self

    def open_preferences(self):
        self.driver.get(USER_PREFERENCE_URL)
        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(AdvancedSettingsIdentifiers.PREFERENCES_SECTION)
        )
        return self

    def search_preference_tags(self, text):
        self.set_input_value(AdvancedSettingsIdentifiers.PREFERENCE_TAG_SEARCH, text)
        return self

    def open_social_auth(self):
        self.driver.get(SOCIAL_AUTH)
        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(AdvancedSettingsIdentifiers.SOCIAL_AUTH_CONTAINER)
        )
        return self

    def social_link_button_count(self):
        return len(self.driver.find_elements(*AdvancedSettingsIdentifiers.SOCIAL_LINK_BUTTONS))
