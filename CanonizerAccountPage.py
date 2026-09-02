import time

from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from CanonizerBase import Page
from Config import *
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
        self.driver.implicitly_wait(IMPLICIT_WAIT_SECONDS)
        self.driver.get(ACCOUNT_SETTING_URL)
        return CanonizerPofilePage(self.driver)

    def profile_page_nickname_tab(self):
        self.driver.implicitly_wait(IMPLICIT_WAIT_SECONDS)
        self.driver.get(NICKNAME_URL)
        return CanonizerPofilePage(self.driver)

    def profile_page_preferences_tab(self):
        self.driver.implicitly_wait(IMPLICIT_WAIT_SECONDS)
        self.driver.get(USER_PREFERENCE_URL)
        return CanonizerPofilePage(self.driver)

    def profile_page_direct_supported_camp_tab(self):
        self.driver.implicitly_wait(IMPLICIT_WAIT_SECONDS)
        self.driver.get(SUPPORTED_CAMP_URL)
        return CanonizerPofilePage(self.driver)

    def profile_page_delegate_supported_camp_tab(self):
        self.driver.implicitly_wait(IMPLICIT_WAIT_SECONDS)
        self.driver.get(DELEGATE_SUPPORT_URL)
        return CanonizerPofilePage(self.driver)
    def profile_page_mysubscription_tab(self):
        self.driver.implicitly_wait(IMPLICIT_WAIT_SECONDS)
        self.driver.get(SUBSCRIPTION_URL)
        return CanonizerPofilePage(self.driver)

    def profile_page_account_setting_social_auth_tab(self):
        self.driver.implicitly_wait(IMPLICIT_WAIT_SECONDS)
        self.driver.get(SOCIAL_AUTH)
        return CanonizerPofilePage(self.driver)

    def profile_page_account_setting_password_tab(self):
        self.driver.implicitly_wait(IMPLICIT_WAIT_SECONDS)
        self.driver.get(CHANGE_PASSWORD)
        return CanonizerPofilePage(self.driver)

       
    def profile_page_public_crash(self):
        self.driver.implicitly_wait(IMPLICIT_WAIT_SECONDS) 
        self.driver.get(ACCOUNT_SETTING_URL)
        action = ActionChains(self.driver)
        self.driver.find_element(By.XPATH, "/html/body/div[1]/section/section/main/div/div[2]/div[2]/div/div/div/div/form/div[1]/div[1]/div/div/div[2]/div/div/span/span/span[2]/div/div/span[2]").click()
        action.key_down(Keys.DOWN).perform()
        action.key_down(Keys.ENTER).perform()
        self.driver.find_element(By.ID, "profileUpdate").click()
        self.driver.get(USER_PREFERENCE_URL)
        return CanonizerPofilePage(self.driver)   
