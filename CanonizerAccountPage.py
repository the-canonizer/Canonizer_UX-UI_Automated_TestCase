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
        self.driver.get(ACCOUNT_SETTING_URL)
        return CanonizerPofilePage(self.driver)

    def profile_page_nickname_tab(self):
        self.driver.implicitly_wait(30)
        self.driver.get(NICKNAME_URL)
        return CanonizerPofilePage(self.driver)

    def profile_page_preferences_tab(self):
        self.driver.implicitly_wait(30)
        self.driver.get(USER_PREFERENCE_URL)
        return CanonizerPofilePage(self.driver)

    def profile_page_direct_supported_camp_tab(self):
        self.driver.implicitly_wait(30)
        self.driver.get(SUPPORTED_CAMP_URL)
        return CanonizerPofilePage(self.driver)

    def profile_page_delegate_supported_camp_tab(self):
        self.driver.implicitly_wait(30)
        self.driver.get(DELEGATE_SUPPORT_URL)
        return CanonizerPofilePage(self.driver)
    def profile_page_mysubscription_tab(self):
        self.driver.implicitly_wait(30)
        self.driver.get(SUBSCRIPTION_URL)
        return CanonizerPofilePage(self.driver)

    def profile_page_account_setting_social_auth_tab(self):
        self.driver.implicitly_wait(30)
        self.driver.get(SOCIAL_AUTH)
        return CanonizerPofilePage(self.driver)

    def profile_page_account_setting_password_tab(self):
        self.driver.implicitly_wait(30)
        self.driver.get(CHANGE_PASSWORD)
        return CanonizerPofilePage(self.driver)
