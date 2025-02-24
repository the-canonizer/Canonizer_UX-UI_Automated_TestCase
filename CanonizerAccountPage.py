import time

from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from CanonizerBase import Page
from Identifiers import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from CanonizerValidationCheckMessages import message
from selenium.webdriver.chrome.service import Service
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.remote.webelement import *
from selenium import webdriver


class CanonizerPofilePage(Page):

    def driver(self):
        self.driver = webdriver.Chrome()

    def profile_button(self):
        self.driver.implicitly_wait(30)
        self.driver.get("https://ux-dev.canonizer.com/settings?tab=profile_info")
        return CanonizerPofilePage(self.driver)

    def profile_page_nickname_tab(self):
        self.driver.implicitly_wait(30)
        self.driver.get("https://ux-dev.canonizer.com/settings?tab=nick_name")
        return CanonizerPofilePage(self.driver)

    def profile_page_preferences_tab(self):
        self.driver.implicitly_wait(30)
        self.driver.get("https://ux-dev.canonizer.com/settings?tab=user_preferences")
        return CanonizerPofilePage(self.driver)

    def profile_page_direct_supported_camp_tab(self):
        self.driver.implicitly_wait(30)
        self.driver.get("https://ux-dev.canonizer.com/settings?tab=direct_supported_camps")
        return CanonizerPofilePage(self.driver)

    def profile_page_delegate_supported_camp_tab(self):
        self.driver.implicitly_wait(30)
        self.driver.get("https://ux-dev.canonizer.com/settings?tab=delegate_supported_camp")
        return CanonizerPofilePage(self.driver)
    def profile_page_mysubscription_tab(self):
        self.driver.implicitly_wait(30)
        self.driver.get("https://ux-dev.canonizer.com/settings?tab=subscriptions")
        return CanonizerPofilePage(self.driver)

    def profile_page_account_setting_social_auth_tab(self):
        self.driver.implicitly_wait(30)
        self.driver.get("https://ux-dev.canonizer.com/settings?tab=social_oauth_verification")
        return CanonizerPofilePage(self.driver)

    def profile_page_account_setting_password_tab(self):
        self.driver.implicitly_wait(30)
        self.driver.get("https://ux-dev.canonizer.com/settings?tab=change_password")
        return CanonizerPofilePage(self.driver)
